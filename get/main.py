from fastapi import FastAPI , Request
from mockData import products
from dtos import ProductDTO

app=FastAPI()

@app.get('/')
def home():
    return "Welcome to fastapi"


# How to have path and qurey params in faat api route

@app.get('/products')
def getProductions():
    return products


@app.get('/products/{productId}')
def getProductById(productId:int):
    # if product available with id return product el    se return error
    for i in products:
        if i.get('id')==productId:
            return i

    return {
        "error":f"product not found for this id {productId}"
    }

# query param in fastapi 
@app.get("/greet")
def greet_user(name:str | None= None):
    return "Hello, how are you? {name}".format(name=name)

# Or we can  also do it below way 

@app.get("/say-hello")
def greet_user(request:Request):
    return "Hello, how are you? {name}".format(name=request.query_params.get("name"))


# How to have different type of http methods 
# how to validate data

@app.post('/products')
def create_product(data:ProductDTO):
    products.append(data.model_dump())
    return {    
        "status":"Product created successfully",
        "data":data
    }

@app.put('/products/{productId}')
def update_product(productId:int,product:ProductDTO):
    for index,i in enumerate(products):
        if i.get('id')==productId:
            products[index]=product.model_dump()    
            return {
                "status":"Product updated successfully",
                "data":products[index]
            }
    return {
        "status":"Product not found for this id {productId}",
        
    }
# pydantic is used for data validation in fastapi
# it helps us to define the structure of the data we want to receive in the request body and validate it before processing it.