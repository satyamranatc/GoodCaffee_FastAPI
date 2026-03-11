from fastapi import FastAPI
from models import Menu, Order, MenuDB, OrderDB
from database import connect  # Ensures connection is established when app starts

app = FastAPI()

# Synchronize tables when the application starts
MenuDB.init_table()
OrderDB.init_table()


@app.get("/")
def root():
    return {"message": "Server is Up and Running...."}


@app.get("/api/menu/all")
def allMenu():
    # Fetch all items using pydb
    items = MenuDB.find().exec()
    
    # Extract only the model data since find() returns a list of PyDB Model objects
    # Note: Depending on pydb implementation, we may need to convert to dict
    # Assuming standard ORM behavior or an explicit to_dict method
    return {"allItems": [dict(id=item.id, name=item.name, price=item.price, description=item.description, image=item.image) for item in items]}


@app.get("/api/menu/{id}")
def menu(id: int):
    item = MenuDB.find_one(id=id)
    if not item:
        return {"message": "Item Not Found"}
    return {"item": dict(id=item.id, name=item.name, price=item.price, description=item.description, image=item.image)}


@app.post("/api/menu/addItem")
def addItem(m: Menu):
    # PyDB save logic
    # Note: We omit 'id' since PyDB auto increments it typically
    new_item = MenuDB(
        name=m.name,
        price=m.price,
        description=m.description,
        image=m.image
    ).save()
    return {"message": "Item Added Successfully", "id": new_item.id}




@app.post("/api/order/addOrder")
def addOrder(o: Order):
    new_order = OrderDB(
        item=o.item,
        qty=o.qty
    ).save()
    return {"message": "Order Added Successfully", "id": new_order.id}


@app.get("/api/order/all")
def allOrders():
    orders = OrderDB.find().exec()
    return {"allOrders": [dict(id=o.id, item=o.item, qty=o.qty) for o in orders]}