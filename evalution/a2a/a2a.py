import io
import igraph
import sys

f=open(sys.argv[1],"r")
lines=f.readlines()
f.close()

a1={}
for line in lines:
	templist=line.strip().split(" ")
	#print templist
	if not a1.has_key(templist[1]):
		a1[templist[1]]=[]
		pass
	a1[templist[1]].append(templist[2])

# for temp1,temp2 in a1.items():
# 	print temp1
# 	print temp2

# print len(a1)

f=open(sys.argv[2],"r")
lines=f.readlines()
f.close()

a2={}
for line in lines:
	templist=line.strip().split(" ")
	#print templist
	if not a2.has_key(templist[1]):
		a2[templist[1]]=[]
		pass
	a2[templist[1]].append(templist[2])

# for temp1,temp2 in a2.items():
# 	print temp1
# 	print temp2

# print len(a2)


match_type=[]
for i in range(0,len(a1)):
	match_type.append(0)
	pass

for i in range(0,len(a2)):
	match_type.append(1)
	pass

#print len(match_type)



edge_dict={}

for temp1 in range(0,len(a1)):
	for temp2 in range(0,len(a2)):
		edge_dict[(temp1,temp2+len(a1))]=len(set(a1.values()[temp1])&set(a2.values()[temp2]))
		pass



g=igraph.Graph()
g.add_vertices(len(a1)+len(a2))

g.add_edges(edge_dict.keys())

# for temp in edge_dict.keys():
# 	g.add_edges(temp)

matching=g.maximum_bipartite_matching(match_type,edge_dict.values())

removeA=[]
moveAB=[]
addB=[]



for i in range(0,len(a1)+len(a2)):
	if i<len(a1):
		if matching.match_of(i)==None:
			removeA.append(i)
			pass
		else:
			moveAB.append((i,matching.match_of(i)))
			pass
		pass
	else:
		if matching.match_of(i)==None:
			addB.append(i)
		pass
	pass

# print removeA
# print moveAB
# print addB

mto=0

for i in removeA:
	mto+=len(a1.values()[i])
	mto+=1
	pass
for i in addB:
	mto+=len(a2.values()[i-len(a1)])
	mto+=1
	pass
for temp in moveAB:
	mto+=len(a1.values()[temp[0]])-edge_dict[temp]+len(a2.values()[temp[1]-len(a1)])-edge_dict[temp]
	pass

# print mto

aco1=sum(map(len,a1.values()))+len(a1)
aco2=sum(map(len,a2.values()))+len(a2)

# print aco1
# print aco2

a2a=1-float(mto)/(float(aco1)+float(aco2))

print a2a