from app.core.kafka_topics import TRADE_SETTLED

publish_event(
    topic=TRADE_SETTLED,
    message=settlement
)
'''settle_trade()

update_cash_balance()

generate_confirmation()'''