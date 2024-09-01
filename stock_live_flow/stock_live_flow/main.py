from quixstreams import Application
import os
from datetime import timedelta

# Communcation with Kafka
app = Application(
    broker_address=os.environ["BROKER_ADDRESS"],
    consumer_group="json__trade_to_ohlc_consumer_group",

)

#Application Input and Output Topics
input_topic = app.topic("raw_trade",value_deserializer="json")
output_topic = app.topic("stock",value_serializer="json")

#Feature Engineering Topic 
sdf = app.dataframe(input_topic)

#10 seconds window aggregation using a Pandas-like API
sdf = sdf.tumbling_window(timedelta(seconds=10),0).reduce(reduce_price,init_reduce_price).final()

sdf = sdf.to_topic(output_topic)


app.run(sdf)