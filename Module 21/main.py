from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"hi world"}

@app.get("/items/")
def return_items():
    return {"items":["K1","K2","K3","K4"]}

@app.get("/items/{item_id}")
def read_items(item_id:int):
    return {"item_id":item_id,"name":"K1"}

@app.put("/items/{item_id}")
def update_items(item_id:int,name:str,price:float):
    return {"item_id":item_id,"item_name":name,"item_price":price}

@app.delete("/items/{item_id}")
def update_items(item_id:int):
    return {"message":"Item sucssesfully deleted."}



