addressToWrite = "aaaa"
length = 8 - len(addressToWrite); 
print length;

addressToWrite = length*'0' + addressToWrite;

print addressToWrite

'''
while True:
    print("\n\
1. Auto find if vulnerable.\n\
2. Auto find distance between format string and its address in words.\n\
3. Provide addToWrite,addToOverwrite and distance in words to get exploit string.\n\
4. Provide addToWrite and distance in words to auto create potential exploit strings using GOT addresses.\n\
5. Quit");
	
    choice = raw_input("> ").lower().rstrip()
    if choice=="1":
        print 1;
    elif choice=="2":
        print 2;
    elif choice=="3":
        print 3;
    elif choice=="4":
        print 4;
    elif choice=="5":
        break;
    else:
        print("Invalid choice, please choose again\n")
'''
