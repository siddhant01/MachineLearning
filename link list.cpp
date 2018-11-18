//Details:

#include<bits/stdc++.h>
using namespace std;

struct node
{
	int info=0;
	node *link=NULL;
}*start=NULL;

void insert(int item)
{
	node *n=new node;
	if(n==NULL)
		return;
	n->info=item;
	n->link=start;
	start=n;
}

node* reverse(node *ptr)
{
	node *current=ptr;
	node *next=NULL;
	node *prev=NULL;
	while(current!=NULL)
	{
		next=current->link;
		current->link=prev;
		prev=current;
		current=next;
	}
	return prev;
}

void midreverse()
{
	node *ptr=start;
	node *midptr=start;
	node *pmidptr=NULL;
	while(ptr->link!=NULL &&  ptr->link->link!=NULL)
	{
		ptr=ptr->link->link;
		pmidptr=midptr;
		midptr=midptr->link;
	}
//	cout<<"hello";
	if(ptr->link!=NULL)
	{
		midptr=midptr->link;
		pmidptr=pmidptr->link;
	}
	cout<<ptr->info;
	cout<<midptr->info;
	pmidptr->link=reverse(midptr);
}

void traverse()
{
	node *ptr=start;
	while(ptr!=NULL)
	{
		cout<<ptr->info<<"  ";
		ptr=ptr->link;
	}
	cout<<endl;
}

int main(void)
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		int t;
		cin>>t;
		insert(t);
	}
	traverse();
	cout<<"\n";
	midreverse();
	cout<<endl;
	traverse();
 	return 0;
}

