#include <stdio.h>
#include <stdlib.h>

static void cleanupc(void) __attribute__ ((constructor));
static void cleanupd(void) __attribute__ ((destructor));


void cleanupc(void) {

  printf("Step 0x1: Inside in the cleanupc function attributed to constructor.\n");
}


int main() {

  printf("Step 0x2: Inside main function.\n");
}


void cleanupd(void) {

  printf("Step 0x3: Inside in the cleanupd function attributed to destructor.\n");
}
