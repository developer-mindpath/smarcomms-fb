from typing import Dict

from common.constants.common import TYPE, URL
from common.enum.message import MessageType


class ButtonService:

    async def button_service(self, buttons: list[Dict] = None) -> list:
        new_button = []
        for button in buttons:
            if URL in button:
                button = {TYPE: MessageType.WEB_URL.value, **button}
                new_button.append(button)
            else:
                button = {TYPE: MessageType.POSTBACK.value, **button}
                new_button.append(button)
        return new_button
