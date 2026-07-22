from fastapi import APIRouter,Depends
from schemas.name import NameIn, NameOut
from core.agent import generate_names
from core.auth import AuthHandler
auth_hander=AuthHandler()
router = APIRouter(prefix="/name")


@router.post("/", response_model=NameOut)
async def take_ainame(data: NameIn,user_id:int=Depends(auth_hander.auth_access_dependency)):
    name_result = await generate_names(data)
    return NameOut(names=name_result.names)