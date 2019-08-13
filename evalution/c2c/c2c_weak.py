#cluster to cluster coverage --- C2Ccvg

#first file should be  origin.rsf
#second file should be  detected.rsf
#example: python  c2c.py   origin.rsf  detected.rsf


import io
import sys


clustera={}
clusterb={}
f1=open(sys.argv[1],"r")
lines=f1.readlines()
f1.close()

for line in lines:
	templist=line.strip().split(" ")
	#print templist
	if clustera.__contains__(templist[1]):
		clustera[templist[1]].append(templist[2])
		pass
	else:
		clustera[templist[1]]=[]
		clustera[templist[1]].append(templist[2])
		pass

#print clustera




f2=open(sys.argv[2],"r")
lines=f2.readlines()
f2.close()

for line in lines:
	templist=line.strip().split(" ")
	#print templist
	if clusterb.__contains__(templist[1]):
		clusterb[templist[1]].append(templist[2])
		pass
	else:
		clusterb[templist[1]]=[]
		clusterb[templist[1]].append(templist[2])
		pass

#print clusterb

# for key,value in clusterb.items():
# 	print key
# 	print value

#ci,cj is a list
def c2c(ci,cj):
	ci=set(ci)
	cj=set(cj)
	#print ci&cj
	return float(len(ci&cj))/float(max(len(ci),len(cj)))
	pass




def C2Ccvg(A1,A2,threshold):
	counter=0
	for key_a1,value_a1 in A1.items():
		for key_a2,value_a2 in A2.items():
			# print "value_a1 is :"
			# print value_a1
			# print "value_a2 is :"
			# print value_a2
			# print c2c(value_a1,value_a2)
			if c2c(value_a1,value_a2) > threshold:
				counter+=1
				#print "break"
				break
		pass
	A2C=len(A2)
	# print "length of A1"
	# print len(A1)
	# print "length of A2"
	# print len(A2)
	# print "counter is"
	# print counter
	# print "A2C is"
	# print A2C
	if float(counter)/float(A2C) <1:
		return float(counter)/float(A2C) 
	else:
		return float(counter)/float(A2C) 
	#return float(counter)/float(A2C) 
	pass


A1={1:[4,5,6],2:[7,8,9],3:[10,11,12]}
A2={1:[7,8],2:[4,5],3:[6,9,10,11,12]}



#MAJORITY 0.5
#MODERATE 0.33
#WEAK 0.1

majority=0.5
moderate=0.33
weak=0.1


#print "majority"
#print max(C2Ccvg(clustera,clusterb,majority),C2Ccvg(clusterb,clustera,majority))

#print "moderate"
#print max(C2Ccvg(clustera,clusterb,moderate),C2Ccvg(clusterb,clustera,moderate))


#print "weak"
print max(C2Ccvg(clustera,clusterb,weak),C2Ccvg(clusterb,clustera,weak))

#weak is not suitable