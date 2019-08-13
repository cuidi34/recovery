#Turbo Modularization Quality
#first file should be  classgraph.dot
#second file should be  detected.rsf

#example: python  TurboMQ.py   classgraph.dot  detected.rsf

import io
import sys


f=open(sys.argv[1],"r")
lines=f.readlines()
f.close()

edgelist=[]
for line in lines:
	templist=line.strip()
	templist=templist.split(" ")
	#print templist
	edgelist.append((templist[2],templist[4]))
	# if "->" in templist:
	# 	templist=templist.split("\"")
	# 	#print templist
	# 	edgelist.append((templist[1],templist[3]))

# for temp in edgelist:
# 	print temp


clusterlist={}
f1=open(sys.argv[2],"r")
lines=f1.readlines()
f1.close()

for line in lines:
	templist=line.strip().split(" ")
	#print templist
	if templist[1] in clusterlist:
		clusterlist[templist[1]].append(templist[2])
		pass
	else:
		clusterlist[templist[1]]=[]
		clusterlist[templist[1]].append(templist[2])
		pass


#edgelist is a list contains every list
#clusterlist is  a block

CF_list=[]
for key,value in clusterlist.items():
	u=0           #   represent the number of intra-relationsheips
	e=0           #   represent the number of inter-relationships
	for temp in edgelist:
		if temp[0] in value and temp[1] in value:
			u+=1
			pass
		if temp[0] in value and temp[1] not in value:
			e+=1
			pass
		if temp[0] not in value and temp[1]  in value:
			e+=1
			pass
		pass
	if u==0:
		CF_list.append(0)
		pass
	else:
		CFtemp=float(u)/(float(u)+0.5*float(e))
		CF_list.append(CFtemp)
		pass

#print CF_list
print sum(CF_list)