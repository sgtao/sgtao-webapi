# gpttemplate.py
from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel, Field
from .functions import convert_templates as templates

router = APIRouter(prefix="/api/gpttemplate")

@router.get("/")
async def get_allinone():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"message": "hello from gpttemplate."}

class Item(BaseModel):
    type: str = Field(min_length=4, max_length=30) # 文字数制限を追加
    data01: Optional[str] = None
    data02: Optional[str] = None
    data03: Optional[str] = None
    data04: Optional[str] = None
    data05: Optional[str] = None

    def is_not_available_type(self) -> bool:
        if (self.type == "011_summarise"):
            return False
        else:
            return True

@router.post('/prompt/')
async def create_prompt(item: Item):
    # return item
    if (item.is_not_available_type()):
        return { "message": f"'{item.type}' is not supported" }
    else:
        response = {
            "message": f"PromptType : ${item.type}",
            "prompt": templates.convert011_summarise(item.data01)
        }
        return response
