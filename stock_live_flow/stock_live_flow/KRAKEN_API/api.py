from typing import List, Dict, Any, Union, Optional
import json
import logging


from websocket import create_connection

from .types import Trade


logger =logging.getLogger()


class KrakenAPI():
    API_URL = "wss://ws.kraken.com"

    def __init__(
        self,
        product_ids: Optional[List[str]]=["XBT/EUR"],
        log_enabled: bool  = True,
    ):

        self._ws = None
        self.product_ids = product_ids
        self._log_enabled = log_enabled

    
    

