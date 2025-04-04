from abc import ABC,abstractmethod
from database.database import async_session_maker
from sqlalchemy import insert,select,delete,update,func,column,join,desc,distinct
from sqlalchemy.orm import selectinload,load_only


class AbstractRepository(ABC):

    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError

    @abstractmethod
    async def delete_one():
        raise NotImplementedError

    @abstractmethod
    async def update():
        raise NotImplementedError


    @abstractmethod
    async def find_filter():
        raise NotImplementedError

    @abstractmethod
    async def find_count():
        raise NotImplementedError

    



class SQLAlchemyRepository(AbstractRepository):

    model = None


    async def add_one(self, data : dict) -> int:
        async with async_session_maker() as session:
            stmt = (
                insert(self.model).
                values(**data).
                returning(self.model.id)
            )
            res = await session.execute(stmt)
            await session.commit()
            return res.one()
    


    async def find_all(self):
      async with async_session_maker() as session:
            stmt = (
                select(self.model)
            )
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    
    async def delete_one(self,id):
        async with async_session_maker() as session:
            stmt = (
                delete(self.model).
                where(self.model.id == id)
            )
            await session.execute(stmt)
            await session.commit()
            return id


    async def update(self,id,values: dict):
        async with async_session_maker() as session:
            stmt = (
                update(self.model).
                where(self.model.id == id).
                values(**values).
                returning(self.model.id)
            )
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()




    async def find_filter(self,filters: list):
        async with async_session_maker() as session:
            stmt =(
                select(self.model).filter(*filters)
            )
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res



    async def find_count(self):
        async with async_session_maker() as session:  
            query = (
                select(
                    func.count()
                )
                .select_from(self.model)
            )

            res = await session.execute(query)
            return res.all()
        
    





