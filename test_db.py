from database import connect
from models import MenuDB

connect(host="localhost", user="root", password="satyamrana", database="goodcaffee_db")
qs = MenuDB.find()
print(type(qs))
print(dir(qs))
