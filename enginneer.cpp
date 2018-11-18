//Details:

#include<bits/stdc++.h>
#include<math.h>
using namespace std;

int main(void)
{
	int t;
	cin>>t;
	while(t--)
	{
		unsigned long long n,b,m;
		cin>>n>>b>>m;
		unsigned long long tt=0;
		int i=0;
		while(i<n)
		{
			unsigned long long j=ceil((float)(n-i)/2);
			i+=j;
			tt=tt+(unsigned long long)j*m+b;
			m*=2;
//			cout<<i<<" "<<j<<" "<<tt<<" "<<m<<endl;
		}
		cout<<tt-b<<endl;
	}
 	return 0;
}

