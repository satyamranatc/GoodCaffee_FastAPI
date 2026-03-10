from fastapi import FastAPI
from models import Menu,Order

app = FastAPI()

menuList = []

orders = []


@app.get("/")
def root():
    return {"message": "Server is Up and Running...."}


@app.get("/api/menu/all")
def allMenu():
    return {"allItems": menuList}


@app.get("/api/menu/{id}")
def menu(id: int):
    items = [i for i in menuList if i["id"] == id]
    if not items:
        return {"message": "Item Not Found"}
    return {"item": items[0]}


@app.post("/api/menu/addItem")
def addItem(m : Menu):
    menuList.append(m.model_dump())
    return {"message": "Item Added Successfully"}




@app.post("/api/order/addOrder")
def addOrder(o : Order):
    orders.append(o.model_dump())
    return {"message": "Order Added Successfully"}


@app.get("/api/order/all")
def allOrders():
    return {"allOrders": orders}