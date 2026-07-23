from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException
from app.kafka.producer import publish_event
from app.core.kafka_topics import ORDER_CREATED

router = APIRouter()
#app = FastAPI()


@router.post("/")
def create_order():

    order = {
        "order_id":1001,
        "symbol":"AAPL",
        "quantity":10,
        "price":220
    }


    publish_event(ORDER_CREATED,order)


    return {
        "message":"Order created",
        "order":order
    }