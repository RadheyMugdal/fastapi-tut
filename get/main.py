from fastapi import FastAPI , Request
from mockData import products

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