from services.messages import MessageService
from services.client import Client

rpc = MessageService()
rpc.start()

client_rpc = Client()

print(" [x] Requesting")
response = client_rpc.call(5)
print(" [.] Got %r" % response)

print(" [x] Requesting")
response = client_rpc.call(response)
print(" [.] Got %r" % response)