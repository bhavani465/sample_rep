outfile:sample.o ispalindrom.o isprime.o
	cc sample.o ispalindrom.o isprime.o -o outfile
sample.o:sample.c
	cc -c sample.c
ispalindrom.o:ispalindrom.c
	cc -c ispalindrom.c
isprime.o:isprime.c
	cc -c isprime.c
