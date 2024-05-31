from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from common.constants.actions import ACTION_ASK_QUESTION
from common.constants.messages import ASK_QUESTION


class ActionAskQuestion(Action):

    def name(self):
        return ACTION_ASK_QUESTION

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=ASK_QUESTION)
        return []
