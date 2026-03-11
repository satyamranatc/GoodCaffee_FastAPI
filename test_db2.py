from database import connect
from models import MenuDB

connect(host="localhost", user="root", password="satyamrana", database="goodcaffee_db")
m = MenuDB.find_one(id=1)
if hasattr(m, 'exec_one'):
    print("find_one returns QuerySet:", type(m))
else:
    print("find_one returns Model directly:", type(m))
