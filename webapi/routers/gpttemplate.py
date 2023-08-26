# gpttemplate.py
import string
from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel, Field
# from .functions import convert_templates as templates
from ..assets import gpt_templates

class Template():
    """
    指定されたテンプレートの情報・ヘルパー関数を保持する。

    Attributes
    ----------
    type : str
        プロンプト雛形の名称

    Attributes
    ----------
    type : str
        プロンプト雛形の名称
    template : string.Template
        テンプレートの雛形情報
    data01 ～ data05 : str
        雛形に与える文字列。
    num_args : int
        雛形に与える文字列の数
    """
    def __init__(self, type):
        self.type = type

        self.template = None
        self.num_args = 0
        self.data01 = None
        self.data02 = None
        self.data03 = None
        self.data04 = None
        self.data05 = None
        if self.type in gpt_templates.templates:
            t = gpt_templates.templates[self.type]
            self.template = t["template"]
            self.num_args = t["num_args"]
        else:
            self.template = None
            self.num_args = 0

    def exist_template(self):
        if self.template != None:
            return True
        else:
            return False

    def conver_template(self):
        t = string.Template(self.template)
        if self.num_args == 1:
            return t.substitute(data01=str(self.data01))
        if self.num_args == 2:
            return t.substitute(
                data01=str(self.data01),
                data02=str(self.data02)
            )



"""
API定義：
"""
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
    t = Template(item.type)

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
