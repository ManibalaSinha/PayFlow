from app.core.kafka_topics import ORDER_CREATED
from app.kafka.producer import publish_event

publish_event(
    topic=ORDER_CREATED,
    message=order_data
)
'''class OrderService:

    create_order()

    cancel_order()

    modify_order()

    get_order()

    validate_order()'''