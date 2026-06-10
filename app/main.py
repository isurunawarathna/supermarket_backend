from fastapi import FastAPI
from app.routers.user_router import routers as user_router
from app.routers.product_router import routers as product_router
from app.routers.supplier_router import routers as supplier_router
from app.routers.customer_router import routers as customer_router
from app.routers.auth_router import routers as auth_router
from app.routers.order_router import routers as order_router
from app.config import create_table

app = FastAPI(title="SuperMarket Management System",version="1.0.0")

@app.on_event("startup")
def startup():
    create_table()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(customer_router)
app.include_router(order_router)