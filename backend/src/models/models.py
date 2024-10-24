from typing import Annotated
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Boolean, ForeignKey, Integer, String, Column,MetaData,Date
from schemas.schemas import UserReadSchema, HistoryCancerInfo

intpk = Annotated[int, mapped_column(index = True,primary_key=True)]


metadata = MetaData()

class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int],Base):
    __tablename__= "users"
    id:Mapped[intpk] = mapped_column(
        index=True
    )
    username: Mapped[str] = mapped_column(
        nullable=False
    )
    email:Mapped[str] = mapped_column(
        nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    def to_read_model(self) -> UserReadSchema:
        return UserReadSchema(
            id = self.id,
            username=self.username,
            email=self.email,
        )

class HistoryCancer(Base):
    __tablename__ = 'history_cancer'
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id',ondelete='CASCADE')
    )
    created_date = Column(Date)

    def to_read_model(self) -> HistoryCancerInfo:
        return HistoryCancerInfo(
            id = self.id,
            user_id = self.user_id,
            created_date= self.created_date,
        )