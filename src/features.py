import requests
import time

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt

#基于地址解析
origin = '1LDbBEqndip1dhPMszjT6n3CzuD768R5aR'
dic = requests.get("https://blockchain.info/address/"+origin+"?format=json").json()


txs=dic['txs']

# 1 address of features extracting
address=dic['address']
#print('address:'+address)

# 2 the number of transactions
num_tx=dic['n_tx']
#print('n_tx:'+str(num_tx))

# 3
num_spent_tx=0;
# 4
num_received_tx=0;
# 5
num_payback_tx=0;

# 6
total_received=dic['total_received']
#print('total_received:'+str(total_received))

# 7
total_sent=dic['total_sent']
#print('total_sent:'+str(total_sent))

# 8
balance=dic['final_balance']
#print('final_balance:'+str(balance))


count=0;
sum_tx_input=0
sum_tx_output=0
# 9
aver_tx_input=0
# 10
aver_tx_output=0

# 11
sum_input_value=0
# 12
sum_output_value=0
# 13
aver_input_value=0
# 14
aver_output_value=0

sum_ad_fee=0


for tx in txs:
    #print('========'+'tx:'+str(count)+'========')
    count+=1
    if count==1:
        start_time=tx['time']
    lifetime=start_time-tx['time']
    #print("block_height:"+str(tx['block_height']))

    sum_tx_input+=tx['vin_sz']
    #print("vin_sz:"+str(tx['vin_sz']))
    sum_tx_output+=tx['vout_sz']
    #print("vout_sz:"+str(tx['vout_sz']))

    #print("unix_time:"+str(tx['time']))
    #print("time:"+timestamp_datetime(tx['time']))
    n_input=0
    flag=0
    per_tx_input_value=0
    per_tx_output_value=0
    for input in tx['inputs']:
        #print('---'+'input:'+str(n_input)+'----')
        n_input+=1
        input_addr=input['prev_out']['addr']
        if input_addr==address:
            num_spent_tx+=1
            flag=1
        #print('input_addr:'+input_addr)
        #print('input_value:'+str(input['prev_out']['value']))
        sum_input_value+=input['prev_out']['value']
        per_tx_input_value+=input['prev_out']['value']

    n_output=0
    for output in tx['out']:
        #print('---'+'output:'+str(n_output)+'----')
        n_output+=1
        output_addr=output['addr']
        if output_addr==address:
            num_received_tx+=1
        #print('output_addr:'+output_addr)
        #print('output_value:'+str(output['value']))
        sum_output_value+=output['value']
        per_tx_output_value+=output['value']
    
    if flag==1:
        sum_ad_fee+=per_tx_input_value-per_tx_output_value


num_payback_tx=num_received_tx+num_spent_tx-num_tx
num_received_tx=num_received_tx-num_payback_tx
num_spent_tx=num_spent_tx-num_payback_tx

aver_tx_input=sum_tx_input/num_tx
aver_tx_output=sum_tx_output/num_tx

aver_input_value=sum_input_value/num_tx
aver_output_value=sum_output_value/num_tx
 
sum_tx_fee=sum_input_value-sum_output_value

# 15 fee for per tx
aver_tx_fee=sum_tx_fee/num_tx

# 16 fee for ad as input
aver_ad_fee=sum_ad_fee/num_spent_tx

# 17 value for per spent tx
aver_spent_value=total_sent/num_spent_tx

# 18 value for per received tx
aver_received_value=total_received/num_received_tx

# 19 lifetime  second


# 20 average interval of tx
if num_tx-1>0:
    aver_interval=lifetime/(num_tx-1)
else:
    aver_interval=lifetime

# 21 average interval of spent tx
if num_spent_tx-1>0:
    aver_spent_interval=lifetime/(num_spent_tx-1)
else:
    aver_spent_interval=lifetime

# 22 average interval of received tx
if num_received_tx-1>0:
    aver_received_interval=lifetime/(num_received_tx-1)
else:
    aver_received_interval=lifetime
    
# 23 the number of tx in a week
if lifetime>(3600*24*7):
    num_tx_week=num_tx/(lifetime/(3600*24*7))
else:
    num_tx_week=num_tx



print("1.address:"+address)
print("2.num_tx:"+str(num_tx))
print("3.num_spent_tx:"+str(num_spent_tx))
print("4.num_received_tx:"+str(num_received_tx))
print("5.num_payback_tx:"+str(num_payback_tx))
print("6.total_received:"+str(total_received))
print("7.total_sent:"+str(total_sent))
print("8.balance:"+str(balance))
print("9.average num tx input:"+str(aver_tx_input))
print("10.average num tx output:"+str(aver_tx_output))
print("11.sum_input_value:"+str(sum_input_value))
print("12.sum_output_value:"+str(sum_output_value))
print("13.aver_input_value:"+str(aver_input_value))
print("14.aver_output_value:"+str(aver_output_value))
print("15.fee for per tx:"+str(aver_tx_fee))
print("16.fee for ad as input:"+str(aver_ad_fee))
print("17.aver_spent_value:"+str(aver_spent_value))
print("18.aver_received_value:"+str(aver_received_value))
print("19.lifetime:"+str(lifetime))
print("20.average interval of tx:"+str(aver_interval))
print("21.average interval of spent tx:"+str(aver_spent_interval))
print("22.average interval of received tx:"+str(aver_received_interval))
print("23.the number of tx in a week:"+str(num_tx_week))


