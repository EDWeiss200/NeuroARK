from utils.repository import AbstractRepository
from fastapi import UploadFile
from random import randint
import os
from datetime import *

class CancerServices:

    def __init__(self,cancer_repo: AbstractRepository) -> None:
        self.cancer_repo: AbstractRepository = cancer_repo()


    async def upload_photo(self,file: UploadFile,user_id):

        filename = f'{file.filename}'

        x = os.path.join(r'backend\src\services\txt_for_neuro', filename)

        with open(x, "wb") as file_object:
            file_object.write(file.file.read())
        #result = neural_get_answer(x)
        result = randint(0,1)
        os.remove(x)
        print(result)
        if result == 1:
            cancer_id = await self.add_history_cancer(user_id)
            return cancer_id
        else:
            return result


    async def add_history_cancer(self,user_id):
        
        history_cancer = {}
        history_cancer['user_id'] = user_id
        created_date = datetime.now()
        history_cancer['created_date'] = created_date

        history_id = await self.cancer_repo.add_one(history_cancer)
        return history_id[0]
