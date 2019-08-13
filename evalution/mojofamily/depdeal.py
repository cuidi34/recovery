
import io



def change(temp):
	temp="contain"+temp[7:]
	return temp
#print "cuidi"

temp="depends cuidi"
temp=change(temp)
#print temp

f=open("dep.rsf","r")

lines=f.readlines()

f.close()


lines=map(change,lines)
#print lines

f1=open("dep.rsf","w")
f1.writelines(lines)
f1.close()
