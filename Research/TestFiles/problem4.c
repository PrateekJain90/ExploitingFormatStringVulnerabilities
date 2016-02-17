#include <stdio.h>
#include <string.h>

#define BUF_SIZE 1024

int main(int argc, char **argv) {
    char buf[BUF_SIZE];
    if(argc < 2) return 1;

    strncpy(buf, argv[1], BUF_SIZE-1);
    printf(buf);

    return 0;
}
