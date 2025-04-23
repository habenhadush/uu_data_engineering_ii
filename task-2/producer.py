import pulsar
client = pulsar.Client("pulsar://192.168.2.54:6650")

producer = client.create_producer("DEtopic")
producer.send(('Welcome to Data Engineering Course!').encode('utf-8'))
producer.close()
client.close()
