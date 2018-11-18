//Details:

#include<iostream>
#include<list>
using namespace std;

bool find(list<int> &li,int item)
{
	for(auto itr=li.begin();itr!=li.end();itr++)
	{
		if(*itr==item)
		return true;
	}
	return false;
}
void myinsert(list<int> &li,int item)
{
	auto itr=li.begin();
	for(;itr!=li.end();itr++)
		if(*itr==item)
			break;
	int temp=*itr;
	li.erase(itr);
	li.push_front(temp);
}

int main(void)
{
	list<int> li;
	int maxsize=0,n;
	cin>>maxsize>>n;
	int arr[n];
	for(int i=0;i<n;i++)
		cin>>arr[i];
	
	int mis=0;
	for(int i=1;i<n;i++)
	{
		if (find(li,arr[i])==false)
		{
			mis++;
			li.push_front(arr[i]);
			if(li.size()>maxsize)
				li.pop_back();
		}
		else
			myinsert(li,arr[i]);
	}
	cout<<mis+1;
	return 0;
}

