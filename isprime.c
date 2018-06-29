#include<stdio.h>
int isprime(int data)
{
	int i;
	for(i=2;i<(data/2);i++)
		if(data%i==0)
		{
			printf("not prime\n");
			return 0;
		}
	printf("prime num\n");
	return 1;

}
