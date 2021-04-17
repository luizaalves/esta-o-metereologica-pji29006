from services.client import Client
import sys, json

client_rpc = Client()

if len(sys.argv) < 3:
    print('Uso: python %s "Method" "/endpoint" "data_json (if PUT in method)"' % sys.argv[0])
    sys.exit()

method = sys.argv[1]
endpoint = sys.argv[2]
body = ''

if len(sys.argv) > 3:
    body = json.loads(str(sys.argv[3]))

print(body)

print(" [x] Requesting")
#body_put = {'value_min':10.0,'value_max':90.0}
#body, status = client_rpc.call(method,'GET','')

body, status = client_rpc.call(endpoint, method, body)
print("Response_Status = %s" % status)
print("Response_Body = %s" % body)