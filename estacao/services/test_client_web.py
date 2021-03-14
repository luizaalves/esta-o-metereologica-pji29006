from services.client import Client

client_rpc = Client()

print(" [x] Requesting")
body_put = {'value_min':30.0,'value_max':45.0}
response = client_rpc.call('/api/v1/sensors/estufa','GET','')

#response = client_rpc.call('/api/v1/sensors/estufa-bmp280/limiares','PUT', body_put)
print("Response = %s" % response)
