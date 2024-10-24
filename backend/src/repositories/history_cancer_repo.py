from utils.repository import SQLAlchemyRepository

from models.models import HistoryCancer

class HistoryCancerRepository(SQLAlchemyRepository):

    model = HistoryCancer

    