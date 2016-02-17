#include<stdio.h>
#include<string.h>

int main(int argc, char **argv, char** envp)
{
  char** env;
  for (env = envp; *env != 0; env++)
  {
    char* thisEnv = *env;

	if(strstr(thisEnv,"SHELLCODE")!=NULL)
		printf("%s -- %p\n", thisEnv, thisEnv);    
 }
  return(0);
}
