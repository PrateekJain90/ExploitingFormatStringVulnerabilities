# Automating format string exploits

####*Problem Domain: Format string exploits*
A number of binary exploitation challenges in CTFs require an attacker to alter the control
ow of a program and make it do things which it should not. Format string vulnerabilities
are one such class of problems. A format string vulnerability can be exploited by feeding
specially crafted user-inputs to the program which can help the attacker to perform attacks
ranging from viewing the stack contents to writing arbitrary data at arbitrary locations.

Exploiting a format string vulnerability is generally simple and straightforward. A number
of basic problems in this area can be solved by following similar steps. The main task for
the attacker is to identify if the program has such a vulnerability. Sometimes this can be
very obvious, but at other times it might take the attacker a long time to find one.


####*Example problems:*

Though there are a not a lot of problems related to format string vulnerabilities, I tested
it on problems like "Game of Tables" and "Protostar Format 4". Apart from that, I tested
the tool on other format string vulnerable problems that I found online. In almost all the
cases, the tool was able to save some amount of time which is generally required to solve
such problems.

**Prostar 4**
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int target;

void hello()
{
 printf("code execution redirected! you win\n");
 _exit(1);
}

void vuln(char* str)
{
 char buffer[512];
 strncpy(buffer, str, sizeof(buffer)-1);
 buffer[sizeof(buffer)]='\0';
 printf(buffer);

 exit(1);
}

int main(int argc, char **argv)
{
 vuln(argv[1]);
}

```

####*Existing Research:*

1. **Taint Checking:** Done at runtime, the basic concept behind taint analysis is to
ag
anything that has been input by a user and consider the input as something which poses
a potential risk. Any other value, which is derived from this user input, is also
agged or
monitored. If any of these variables can be used to execute a dangerous command, the taint
checker lets the user, in this case the attacker, know of the potentially dangerous tainted
variables which he can control.

    This can be used in CTF problems having for finding which format function is being supplied a tainted first arguement.

2. **Pierre Bourdon. Python GDB tutorial for reverse engineering:** This is a nice article which explains how to write a python plugin for GDB. The plugin helps
find vulnerable format functions by dynamically analyzing calls to various format functions.

    This could be used to find the vulnerable format functions in the CTF problems by checking if the address of the first arguement passed to a function like printf is in the read/write memory.


3. **Thyago Silva. Format Strings (Gotfault Security Community):** This article explains nicely about format string concepts including direct parameter
accesses, format string vulnerabilities and the different ways that they can be exploited in.
E.g., writing to memory addresses, overwriting the Dtors Section, Overwriting the Global Offset table entries etc.
The article also shows how to develop a format string builder which can again be used to generate exploits for format strings.


####*What I did:*

1. Used dynamic analysis on format function such as printf. Prepared a shared library and set it with the help of the LD_PRELOAD environment variable. It intercepts calls to the printf function and stores the address of the first arguement. Later, it checks if this address is present in the read/write memory by comparing the address with those mentioned in the /proc/pid/maps file.
2. The tool does multiple executions of the program to find the distance between the format string and its address.
3. Generates an exploit string when provided with the address to overwrite, the address to write and the offset in words.
4. Generates exploit strings by using GOT addresses as addresses to overwrite. In this case, the user just has to provide the address to write and the offset.


####*Demo - Prostar 4*
