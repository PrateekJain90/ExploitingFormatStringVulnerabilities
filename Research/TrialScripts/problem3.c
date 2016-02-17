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
