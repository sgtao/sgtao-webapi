# gpttemplate.py
from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel, Field
from .functions import convert_templates as templates

router = APIRouter(prefix="/api/gpttemplate")

@router.get("/")
async def hello_gpttemplate():
    """_for access check_

    Returns:
        dict: { "message": "<hello message>" }
    """
    return {"message": "hello from gpttemplate."}

class Item(BaseModel):
    type: str = Field(min_length=4, max_length=30) # 文字数制限を追加
    data01: Optional[str] = None
    data02: Optional[str] = None
    data03: Optional[str] = None
    data04: Optional[str] = None
    data05: Optional[str] = None


@router.post("/prompt")
async def create_prompt(item: Item):
    """
    プロンプトを生成して返答する

    Arguments:
        RequestBody (Item):
            - "type": <プロンプト雛形の名称>,
            - "data01"～"data05": <雛形に与える文字列>

    Returns:
        ResponseBody (dict):
            - "message": <雛形情報>,
            - "prompt": <プロンプト生成の結果>
    """
    # return item
    t = templates.Template(item.type)

    if t.exist_template():
        if t.num_args >= 1:
            t.data01 = item.data01
        if t.num_args >= 2:
            t.data02 = item.data02

        response = {
            "message": f"PromptType : {item.type}",
            "prompt": t.conver_template()
        }
        return response

    else:
        return { "message": f"'{item.type}' is not supported" }
