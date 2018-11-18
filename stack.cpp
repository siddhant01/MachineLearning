#include<iostream>
#include<string>
using namespace std;

int count(string s)
{
	int c=0;
	for(int i=0;i<s.length();i++)
	{
		if(s[i]=='(')
			c++;
	}
	return c;
}

#include<stack>

int main()
{
	string b;
	cin>>b;
	int s=0;
	for(int i=0;i<b.length();i++)
	{
		if(b[i]=='(')
			s++;
		else
			s--;
	}
	if (s==0)
		cout<<count(b);
	else
		cout<<-1;
}
	
