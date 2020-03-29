import requests
import time

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt
#基于地址解析
origin = '17z35xHz19KcdnxDGH9awSsqxSYSLeu35T'
dic = requests.get("https://blockchain.info/address/"+origin+"?format=json").json()

print('')
txs=dic['txs']
print('address:'+dic['address'])
print('n_tx:'+str(dic['n_tx']))
print('total_received:'+str(dic['total_received']))
print('total_sent:'+str(dic['total_sent']))
print('final_balance:'+str(dic['final_balance']))
count=0;
for tx in txs:
    print('========'+'tx:'+str(count)+'========')
    count+=1
    print("block_height:"+str(tx['block_height']))
    print("vin_sz:"+str(tx['vin_sz']))
    print("vout_sz:"+str(tx['vout_sz']))
    print("unix_time:"+str(tx['time']))
    print("time:"+timestamp_datetime(tx['time']))
    n_input=0
    for input in tx['inputs']:
        print('---'+'input:'+str(n_input)+'----')
        n_input+=1
        print('input_addr:'+input['prev_out']['addr'])
        print('input_value:'+str(input['prev_out']['value']))

    n_output=0
    for output in tx['out']:
        print('---'+'output:'+str(n_output)+'----')
        n_output+=1
        print('output_addr:'+output['addr'])
        print('output_value:'+str(output['value']))
