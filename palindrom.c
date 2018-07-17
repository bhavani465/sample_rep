#include<stdio.h>
void main()
{
	//this is palindrom program
	//this is my second edit
	int data=2343,rev=0,temp;
	temp=data;
	while(temp)
	{
		rev=rev*10+(temp%10);
		temp=temp/10;
	}
	if(rev==data)
		printf("%d is palindrom\n",data);
	else
		printf("%d is not palindrom\n",data);

}

