//Details:

#include<iostream>
using namespace std;

int main(void)
{
	int n,k;
	cin>>n>>k;
	n=n+2;
	int a[n]={0};
	int p[n]={0};
	for(int i=1;i<n-1;i++)
	{
		cin>>a[i];
		p[i]=a[i];
	}

	for(int i=0;i<k;i++)
	{
		for(int j=1;j<n-1;j++)
		{
			if(p[j-1]==p[j+1])
				a[j]=0;
			else
				a[j]=1;
		}
		for(int j=0;j<n;j++)
			p[j]=a[j];
	}
	for(int i=1;i<n-1;i++)
		cout<<a[i]<<" ";
 	return 0;
}

