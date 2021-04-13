from services.client import Client

client_rpc = Client()

print(" [x] Requesting")
body_put = {'value_min':10.0,'value_max':90.0}
#body, status = client_rpc.call('/api/v1/sensors','GET','')

body, status = client_rpc.call('/api/v1/sensors/pir1/limiares','PUT', body_put)
print("Response_Status = %s" % status)
print("Response_Body = %s" % body)
