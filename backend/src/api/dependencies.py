from services.user_services import UserServices
from repositories.user_repo import UserRepository

from services.cancer_service import CancerServices
from repositories.history_cancer_repo import HistoryCancerRepository

from services.news_service import NewsService


def user_service() -> UserServices:
    return UserServices(UserRepository)

def cancer_service() -> CancerServices:
    return CancerServices(HistoryCancerRepository)

def news_service() -> NewsService:
    return NewsService()