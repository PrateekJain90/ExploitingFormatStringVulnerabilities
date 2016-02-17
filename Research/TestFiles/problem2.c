#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {

  char          buffer[64];
  static int    value = 50;

  if(argc != 2)
    return -1;

  strcpy(buffer, argv[1]);

  printf("Right way:\n");
  printf("%s\n", buffer);

  printf("Wrong way:\n");
  printf(buffer);

  printf("\n");

  printf("(-) value @ 0x%08x = %d 0x%08x\n",
         &value, value, value);

  return 0;
}

