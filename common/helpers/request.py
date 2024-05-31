import requests
from typing import Optional, Dict

class RequestHelper:

    @staticmethod
    async def get(url: str, **kwargs: Dict) -> Optional[requests.Response]:
        try: 
            response = requests.get(url=url, **kwargs)
        except Exception as error:
            raise error
        finally:
            return response

    @staticmethod
    async def post(url: str, data: dict , **kwargs: Dict) -> Optional[requests.Response]:
        try:
            response = requests.post(url=url, data=data, **kwargs)
        except Exception as error:
            raise error
        finally:
            return response
    
    @staticmethod
    async def put(url: str, data: dict, **kwargs: Dict) -> Optional[requests.Response]:
        try: 
            response = requests.put(url=url, data=data, **kwargs)
        except Exception as error:
            raise error
        finally:
            return response
