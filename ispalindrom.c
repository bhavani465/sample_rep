#include<stdio.h>
int ispalindrom(int data)
{
	int temp,rev=0;
	temp=data;
	while(temp)
	{
		rev=rev*10+(temp%10);
		temp/=10;
	}
	if(rev==data)
	{
		printf("palindrom\n");
		return 1;
	}
	else
	{
		printf("not palindrom\n");
		return 0;
	}
}
