from app.core.kafka_topics import TRADE_EXECUTED

publish_event(
    topic=TRADE_EXECUTED,
    message=trade
)
'''class TradeService:

    execute_trade()

    get_trade()

    trade_history()

    publish_trade_event()'''