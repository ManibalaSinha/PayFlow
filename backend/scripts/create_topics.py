from kafka.admin import KafkaAdminClient, NewTopic

topics = [
    "order.created",
    "order.validated",
    "trade.executed",
    "trade.settled",
    "portfolio.updated",
    "position.updated",
    "risk.checked",
    "market.price.updated",
]

admin = KafkaAdminClient(
    bootstrap_servers="kafka:9092"
)

admin.create_topics([
    NewTopic(name=t, num_partitions=3, replication_factor=1)
    for t in topics
])