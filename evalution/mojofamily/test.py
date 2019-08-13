import csv


csvfile=file("cuidi.csv","w")
writer=csv.writer(csvfile)

writer.writerow(["name","age","telephone"])

data=[
("cuidi","22","1234"),
("wyc","21","1234"),
]

writer.writerows(data)
csvfile.close()

#use writerows to write data
