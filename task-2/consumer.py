import pulsar

client = pulsar.Client("pulsar://192.168.2.54:6650")
consumer = client.subscribe(topic="DEtopic", subscription_name="DE-sub")
msg = consumer.receive()

try:
    print("Recieved message : '%s'" %msg.data())

    consumer.acknowledge(msg)

except:
    consumer.negative_acknowledge(msg)

finally:
    consumer.close()
    client.close()
