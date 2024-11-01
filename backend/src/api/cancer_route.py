from fastapi import APIRouter,Depends, UploadFile
from .dependencies import cancer_service
from auth.auth import current_user
from services.cancer_service import CancerServices
from models.models import User


router = APIRouter(
    prefix='/cancers',
    tags=['cancers'],
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


@router.get('/days/{days}')
async def count_cancer_by_days(
    days: int,
    user: User = Depends(current_user),
    cancer_service: CancerServices = Depends(cancer_service),
):

    cancer_history = await cancer_service.get_cancer_by_days(days)

    return cancer_history

@router.get('')
async def get_all(
    user: User = Depends(current_user),
    cancer_service: CancerServices = Depends(cancer_service),
):

    cancer_history = await cancer_service.get_all_history_cancer()

    return cancer_history