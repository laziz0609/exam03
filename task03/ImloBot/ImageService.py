from .APIClient import APIClient


class ImageService:

    def __init__(self):
        self.apiclienv = APIClient()

    
    async def  fetch_random_image(self, animal: str) -> str:
        if animal == "cat":
            return await self.apiclienv.get_cat_image_url()
        
        elif animal == "dog":
            return await self.apiclienv.get_dog_image_url()
        
        elif animal == "fox":
            return await self.apiclienv.get_fox_image_url()