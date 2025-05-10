from fastapi import APIRouter,Depends
from services.news_service import NewsService
from .dependencies import news_service



router = APIRouter(
    prefix='/news',
    tags=['news'],
)

@router.get('/get_news')
async def get_news(
    news_service: NewsService = Depends(news_service)
):
    news = await news_service.get_news_cancer()
    return news