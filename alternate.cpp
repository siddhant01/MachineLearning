#include<iostream>
#include<string>
using namespace std;

int main()
{
	int t=0;
	cin>>t;
	while(t--)
	{
		string s;
		cin>>s;
		if(s.length()%2==1)
		{
			cout<<"NO"<<endl;
			continue;
		}
		int flag=0;
		for(int i=0;i<s.length()-2;i+=2)
		{
			if(s[0]==s[i+2] && s[1]==s[i+3])
				continue;
			else
			{
				flag=1;
				cout<<"NO"<<endl;
				break;
			}
		}
		if(flag==0)
			cout<<"YES"<<endl;
	}
}
