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



print getMoJoFM("distra.rsf","distrb.rsf")