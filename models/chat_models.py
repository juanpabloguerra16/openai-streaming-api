from pydantic import BaseModel
from datetime import datetime
from typing import List

class ChatInteraction(BaseModel):
    prompt_request: str
    prompt_response: str
    formattedResponse: str
    
class ChatSession(BaseModel):
    id: str
    user_id: str
    title: str
    date: str
    deleted: bool = False
    interactions: List[ChatInteraction] = None
    

