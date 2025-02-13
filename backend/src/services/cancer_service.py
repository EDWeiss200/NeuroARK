from utils.repository import AbstractRepository
from fastapi import UploadFile
from random import randint
import os
from datetime import *
from utils.neuro.neuro_ark import neuro_check

class CancerServices:

    def __init__(self,cancer_repo: AbstractRepository) -> None:
        self.cancer_repo: AbstractRepository = cancer_repo()


    async def upload_photo(self,file: UploadFile):

        filename = f'{file.filename}'

        x = os.path.join(r'backend\src\services\txt_for_neuro', filename)
        return x

        with open(x, "wb") as file_object:
            file_object.write(file.file.read())
        #result = neural_get_answer(x)
        result = neuro_check(x)
        os.remove(x)
        return result
        

    async def add_history_cancer(self,user_id):
        
        history_cancer = {}
        history_cancer['user_id'] = user_id
        created_date = datetime.now()
        history_cancer['created_date'] = created_date

        history_id = await self.cancer_repo.add_one(history_cancer)
        return history_id[0]

    async def get_cancer_by_days(self,days: int):

        history_cancer = await self.cancer_repo.find_all()

        res_cancer = []
        for cancer in history_cancer:
            now_time = datetime.now()
            deadline: timedelta = cancer.created_date + timedelta(days=days)
            if deadline > now_time:
                res_cancer.append(cancer)
        
        return res_cancer

    async def get_cancer_by_user_id(self,days: int):

        history_cancer = await self.cancer_repo.find_all()

        res_cancer = []
        for cancer in history_cancer:
            now_time = datetime.now()
            deadline: timedelta = cancer.created_date + timedelta(days=days)
            if deadline > now_time:
                res_cancer.append(cancer)
        
        return res_cancer

    async def get_all_history_cancer(self):

        cancers = await self.cancer_repo.find_all()

        return cancers