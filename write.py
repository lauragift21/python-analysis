# writing data to files
import csv

with open('mydata.csv', 'w') as f:
    stocks = ["appl", "f"]
    for stk in stocks:
      myfile=open("finance-" + stk + ".csv", "r")
      reader = csv.reader(myfile)
      headers = next(reader, None) # column headers
      #print(headers)
      count = 0
      for x in reader:
        # date. open, close, volume
        f.write(stk + "," + x[0] + "," + x[1] + "," + x[4] + ","  + x[6] + "\n")
        count = count + 1
    print (count)
    myfile.close()
f.close()
print("done")