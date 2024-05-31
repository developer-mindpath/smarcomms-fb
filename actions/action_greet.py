from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from common.constants.actions import ACTION_GREET
from common.constants.buttons import MENU_BUTTONS
from common.constants.messages import  GREET_MESSAGE
from services.button import ButtonService


class ActionGreet(Action):

    def __init__(self) -> None:
        self.__button_service = ButtonService()

    def name(self) -> Text:
        return ACTION_GREET

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        menu_buttons = await self.__button_service.button_service(buttons=MENU_BUTTONS)
        dispatcher.utter_message(text=GREET_MESSAGE, buttons=menu_buttons)
        return []
