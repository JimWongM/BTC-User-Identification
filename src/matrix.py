import csv


size=6347
matrix=[[] for i in range(size)]
tx=[[] for i in range(size)]

for i in range(size):
    for j in range(size):
        matrix[i].append(0)

csvFile1=open("F:\ics_lab\Addresses\\tx.csv","r")
reader =csv.reader(csvFile1)
for item in reader:
    if reader.line_num>size:
        continue
    print("文本第"+str(reader.line_num)+"行")
    current=reader.line_num-1   #从0开始记录列表角标
    tx[current]=item
    for j in range(len(tx[current])-2):
        #print(tx[current][j+2])
        for i in range(current):               
            if tx[current][j+2] in tx[i]:
                matrix[i][current]=matrix[current][i]=1

#print (matrix)

csvFile2=open("F:\ics_lab\Addresses\\matrix.csv","a+",newline="")
writer=csv.writer(csvFile2)
for i in range(len(matrix)):
    writer.writerow(matrix[i])

csvFile1.close()
csvFile2.close()
    
# 数据规模为6347时，有828个节点时独立的，即与其他几点没有任何连接
