from fastapi import APIRouter,Depends
from .dependencies import user_service
from auth.auth import current_user
from services.user_services import UserServices
from models.models import User


router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@router.get('/get_current_user')
async def get_user_by_id(
    user: User = Depends(current_user),
    user_service: UserServices = Depends(user_service)

):
    user = await user_service.get_user_by_id(user.id)
    return user


@router.get('/check')
async def check_current_user(
    user: User = Depends(current_user)
):
    return user.id