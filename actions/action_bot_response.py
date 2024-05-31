import asyncio
import multiprocessing
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from common.constants.actions import ACTION_BOT_RESPONSE
from common.constants.buttons import BOT_RESPONSE_BUTTON
from common.constants.common import ASSISTANT, BOT, CONTENT, EMPTY_STRING, ROLE, TEXT, USER
from common.constants.messages import CONTACT_US, PROMPT, SOMETHING_WENT_WRONG
from common.helpers.logger import logger
from services.button import ButtonService
from services.openai import OpenaiService
from services.typing import Typing


class ActionBotResponse(Action):

    def name(self) -> Text:
        return ACTION_BOT_RESPONSE

    def __init__(self) -> None:
        self.__openai_service = OpenaiService()
        self.__button_service = ButtonService()

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            bot_response_button = await self.__button_service.button_service(buttons=BOT_RESPONSE_BUTTON)
            user_query = tracker.latest_message.get(TEXT)
            search_results = await self.__openai_service.search_embedding(prompt=user_query)
            context = "\n\n".join([result.answer for result in search_results])
            prompt = f"{PROMPT}\nInformation: {context}"
            await Typing().show_typing(id=tracker.sender_id)
            conversation_history = chat_history(tracker=tracker)
            queue = multiprocessing.Queue()
            multiprocess(
            tracker=tracker, 
            queue=queue, 
            prompt=prompt, 
            user_query=user_query, 
            conversation_history=conversation_history
            )
            bot_response = queue.get()
            logger.info(bot_response)
            sentence_list = (f"{bot_response} ").split('. ')
            new_response = EMPTY_STRING
            for sentence in sentence_list:
                if len(new_response + sentence) <= 500:
                    new_response += sentence + ". "
                else:
                    dispatcher.utter_message(text=new_response)
                    new_response = sentence
            dispatcher.utter_message(text=new_response)
            dispatcher.utter_message(text=CONTACT_US, buttons=bot_response_button)
        except Exception as error:
            dispatcher.utter_message(text=SOMETHING_WENT_WRONG, buttons=bot_response_button)
            logger.exception(error)
        return []

def chat_process(queue: multiprocessing.Queue, prompt: str, message: str = None, conversation_history: list[dict] = []) -> None:
    final_response =  asyncio.run(OpenaiService().chat_completion(prompt=prompt, message=message, history=conversation_history))
    queue.put(final_response)
    return 

def typing_on(id: str) -> None:
    while True:
        asyncio.run(Typing().show_typing(id=id))

def chat_history(tracker: Tracker) -> list[dict]:
    user_event = tracker.get_last_event_for(USER)
    bot_event = tracker.get_last_event_for(BOT)
    if user_event and bot_event:
        user_message = user_event.get(TEXT)
        bot_response = bot_event.get(TEXT)
        return [{ROLE: USER, CONTENT: user_message}, {ROLE: ASSISTANT, CONTENT: bot_response}]
    return []

def multiprocess(tracker: Tracker, queue: multiprocessing.Queue, prompt: str, user_query: str, conversation_history: list[dict] = []) -> None:
    open_ai_process = multiprocessing.Process(target=chat_process, args=(queue, prompt, user_query, conversation_history))
    facebook_typing_process = multiprocessing.Process(target=typing_on, args=(tracker.sender_id,)) 
    open_ai_process.start()
    facebook_typing_process.start()
    open_ai_process.join()
    facebook_typing_process.kill()
    return 
