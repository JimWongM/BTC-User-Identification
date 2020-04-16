import csv

csvFile1=open("F:\ics_lab\Addresses\\features.csv","r")
csvFile2=open("F:\ics_lab\Addresses\\simplified_features.csv","a+",newline="")

reader=csv.reader(csvFile1)
writer=csv.writer(csvFile2)

for item in reader:
    print(reader.line_num)
    for i in range(5,8):
        item[i]=int(float(item[i])/1000000)
    
    item[8]=int(float(item[8]))
    item[9]=int(float(item[9]))
    for i in range(10,18):
        item[i]=int(float(item[i])/1000000)
    for i in range(18,22):
        item[i]=int(float(item[i])/3600)
    item[22]=round(float(item[22]),1)
    writer.writerow(item)
   