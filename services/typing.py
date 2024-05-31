import json

from common.constants.common import ACCESS_TOKEN, APPLICATION_JSON, CONTENT_TYPE, ID, MESSAGING_TYPE, NOTIFICATION_TYPE, RECIPIENT, REGULAR, RESPONSE, SENDER_ACTION, TYPING_ON
from common.constants.url import FACEBOOK_URL
from common.helpers.logger import logger
from common.helpers.request import RequestHelper
from config.dot_env import FB_TOKEN


class Typing:

    def __init__(self) -> None:
        self.__header =  {
        CONTENT_TYPE: APPLICATION_JSON
        }
        self.__url = f"{FACEBOOK_URL}?{ACCESS_TOKEN}={FB_TOKEN}"

    async def show_typing(self, id: str) -> None:
        payload = json.dumps({
        MESSAGING_TYPE: RESPONSE,
        NOTIFICATION_TYPE: REGULAR,
        RECIPIENT: {ID: id},
        SENDER_ACTION: TYPING_ON
        })
        response = await RequestHelper.post(
            url=self.__url, 
            headers=self.__header, 
            data=payload
        )
        logger.info(response.text)
        return 
