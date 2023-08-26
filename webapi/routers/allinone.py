# allinone.py
from fastapi import APIRouter
from fastapi import HTTPException

from ..assets import aio_assets

router = APIRouter(prefix="/api/allinone")

@router.get("/")
async def get_allinone():
    """_for access check_

    Returns:
        dict: { "message": "<hello message>" }
    """
    return {"message": "hello from allinone."}

@router.get("/category")
async def get_aio_category():
    """_allinone category list_

    Returns:
        dict: { "number": int, "categories": List }
    """
    obj = aio_assets.aio_category()
    # obj is list of bellow
    # obj = {
    #     "category": [
    #         {
    #             "categoryNo": 1,
    #             "number": 17,
    #             "startFrom": 1,
    #             "endTo": 17,
    #             "category": "01_時制"
    #         },
    #         ...
    #     ]
    # }

    category_list = []
    for obj_item in obj['category']:
        category_list.append(obj_item['category'])
    return {
            "number": len(obj['category']),
            "categories": category_list
    }

@router.get("/category/item")
async def get_category_item(id: int = 1):
    """_detail category item_

    Returns:
        dict: { "number": int, "categories": List }
    """
    obj = aio_assets.aio_category()
    if id >= 1 and id <= len(obj['category']):
        return obj['category'][(id - 1)]
    else:
        raise HTTPException(status_code=404, detail="id is out ob range")


@router.get("/contents")
async def get_num_contents():
    """_number of contents_

    Returns:
        { "number": int }
    """
    obj = aio_assets.aio_contents()
    # obj is list of bellow
    # obj = {
    #     "contents": [
    #         {
    #             "no": 1,
    #             "index": "[001]",
    #             "category": "01_時制",
    #             "category_index": "[01]",
    #             "englishText": "He grinned and said, “I make lots of money.  On weekdays I receive an average of 50 orders a day from all over the globe via the Internet.” ",
    #             "translation_slashed": "彼はにっこり笑った／そして言った／「私は稼いでいる・たくさんのお金を。平日に／私は受け取っている・平均で50の注文を／一日当たり／地球の至る所から／インターネット経由で」 ",
    #             "translation_natural": "彼はにっこり笑って「とても儲かっていますよ。平日はインターネット経由で世界中から１日平均５０件の注文があるんです」と言った。 "
    #         },
    #         ...
    #     ]
    # }

    return {
            "number": len(obj['contents'])
    }


@router.get("/contents/item")
async def get_aio_item(id: int = 1):
    """_detail contents item_

    Returns:
        { Object }
    """
    obj = aio_assets.aio_contents()
    if id >= 1 and id <= len(obj['contents']):
        return obj['contents'][(id - 1)]
    else:
        raise HTTPException(status_code=404, detail="id is out ob range")
