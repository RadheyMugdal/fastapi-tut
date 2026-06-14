from pydantic import BaseModel

class ProductDTO(BaseModel):
    id:int
    title:str
    price:float
    description:str
    count:int=0 
