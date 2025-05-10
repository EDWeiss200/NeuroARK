from utils.news_parser import get_news

class NewsService(self):


    async def get_news_cancer(self):


        news = await get_news()

        return news


    