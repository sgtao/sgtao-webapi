# gpttemplate.py
from fastapi import APIRouter

router = APIRouter(prefix="/api/gpttemplate")

@router.get("/")
async def get_allinone():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"message": "hello from gpttemplate."}
