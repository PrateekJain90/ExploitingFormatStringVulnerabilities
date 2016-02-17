#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif

#include <stdio.h>
#include <dlfcn.h>

static int (*orig_printf)(const char *format, ...) = NULL;

int printf(const char *format, ...)
{
	
	if (orig_printf == NULL)
	{
		orig_printf = (int (*)(const char *format, ...))dlsym(RTLD_NEXT, "printf");
	}

	FILE *fp;
	fp = fopen("address.txt", "a+");
	fprintf(fp,"%p\n",format);
	fclose(fp);

	return orig_printf(format);
}

