#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 512

void getShell()
{
  gid_t gid = getegid();
  setresgid(gid, gid, gid);  	
  system("/bin/sh -i");
}

int main(int argc, char *argv[]) {

  char name[MAX_LENGTH+1];

  if(argc != 2)
    return -1;

  strncpy(name, argv[1], MAX_LENGTH);
  name[MAX_LENGTH] = '\0';
 
  printf("Welcome back: ");
  printf(name);
  printf("\nToday's quote is:\nWith great power comes great responsibility\n");

  exit(0);
}
