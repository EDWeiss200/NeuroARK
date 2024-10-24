from fastapi import APIRouter,Depends, UploadFile
from .dependencies import cancer_service
from auth.auth import current_user
from services.cancer_service import CancerServices
from models.models import User


router = APIRouter(
    prefix='/cancer',
    tags=['cancer'],
)



@router.post('/send_photo')
async def send_photo(
    file: UploadFile,
    user: User = Depends(current_user),
    cancer_service: CancerServices = Depends(cancer_service)
):

    history_id = await cancer_service.upload_photo(file,user.id)
    print(history_id)
    return history_id