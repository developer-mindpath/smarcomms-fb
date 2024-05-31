from enum import Enum


class MessageType(Enum):
    BASICFORM_1 = "basicform_1"
    POSTBACK = "postback"
    PHONE_NUMBER = "phone_number"
    QUERY = "query"
    CALENDER = "calender"
    EMAIL_TYPE = "email"
    TEMPLATE = "template"
    GENERIC = "generic"
    WEB_URL = "web_url"
