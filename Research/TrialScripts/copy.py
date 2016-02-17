import os
import sys
from subprocess import Popen,PIPE,call

binaryName = "/home/prateekj/Desktop/ResearchProject/Research/FinalFiles/binaries/format"
filename = binaryName + "-gdb.py";
components = binaryName.split("/");
renameFile = "/".join(components[0:-1]) + "/*gdb.py";

print filename;
print renameFile;

Popen(["mv" + renameFile + " " + filename],stdout=PIPE,close_fds=True,shell=True).communicate()[0].strip()

