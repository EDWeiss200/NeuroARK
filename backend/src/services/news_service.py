from utils.news_parser import get_news

class NewsService():


    async def get_news_cancer(self):


        news = await get_news()

        return news


    