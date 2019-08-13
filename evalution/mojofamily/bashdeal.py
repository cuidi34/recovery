import os
import csv
from subprocess import Popen , PIPE




def getMoJo(filename1,filename2):
	cmd="java mojo.MoJo  "+filename1+"  "+filename2+" -fm"
	p=Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
	out,err=p.communicate()
	#print "out:"
	results=out.strip()
	return results

def getMoJoFM(filename1,filename2):
	return max(getMoJo(filename1,filename2),getMoJo(filename2,filename1))



#print getMoJoFM("distra.rsf","distrb.rsf")





project_name="archstudio"
clusteringlist=[]

groundtruth="./"+project_name+"/groundtruth/"+os.listdir("./"+project_name+"/groundtruth")[0]
print groundtruth



for item in os.listdir(project_name):
	if ".rsf" in item:
		#print item
		clusteringlist.append("./"+project_name+"/"+item)

#print "ACDC".lower() in "acdc_clustering".lower() 

csvfile=file(project_name+"_mojo_result.csv","w")
writer=csv.writer(csvfile)

writer.writerow([project_name,"g2c","c2g"])

data=[]
for item1 in clusteringlist:
	print item1
	data.append((item1.split("/")[2],getMoJo(groundtruth,item1),getMoJo(item1,groundtruth)))

writer.writerows(data)
csvfile.close()




