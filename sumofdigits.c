#include<stdio.h>
int sumofdigits(int data)
{
	int sum=0;
	while(data)
	{
		sum=sum+(data%10);
		data=data/10;
	}
	printf("sum is %d\n",sum);
	return sum;
}
