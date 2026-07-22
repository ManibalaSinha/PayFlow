from app.core.kafka_topics import RISK_CHECKED

publish_event(
    topic=RISK_CHECKED,
    message=result
)
'''check_buying_power()

check_position_limit()

check_daily_limit()

validate_risk()'''