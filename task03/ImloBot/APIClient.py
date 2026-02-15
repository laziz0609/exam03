import aiohttp


class APIClient:
    def __init__(self):
        self.cat_url = "https://api.thecatapi.com/v1/images/search"
        self.dog_url = "https://dog.ceo/api/breeds/image/random"
        self.fox_url = "https://randomfox.ca/floof/"


    async def get_cat_image_url(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.cat_url) as response:
                if response.status == 200:
                    content = await response.json()
                    return content[0].get("url")       


    async def  get_dog_image_url(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.dog_url) as response:
                if response.status == 200:
                    content = await response.json()
                    return content.get("message")   
        

    async def get_fox_image_url(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.fox_url) as response:
                if response.status == 200:
                    content = await response.json()
                    return content.get("image") 
