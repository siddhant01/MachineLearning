//Details:

#include<iostream>
using namespace std;

int s=0;
int r=4,c=4;

int fun(int **m,int cr,int cc)
{
	cout<<"current position "<<cr<<" "<<cc<<" "<<m[cr][cc]<<endl;
	if(m[cr][cc]==9)
		s=1;
	if(m[cr][cc]==1)
		m[cr][cc]=0;

	if(0<=cr-1 && m[cr-1][cc]!=0)
		fun(m,cr-1,cc);
	if(cr+1<r && m[cr+1][cc]!=0)
		fun(m,cr+1,cc);
	if(0<=cc-1 && m[cr][cc-1]!=0)
		fun(m,cr,cc-1);
	if(cc+1<c && m[cr][cc+1]!=0)
		fun(m,cr,cc+1);
}

int main(void)
{
	cin>>r>>c;
		int **m=new int*[r];
	for(int i=0;i<r;i++)
		m[i]=new int[c];
	for(int i=0;i<r;i++)
		for(int j=0;j<c;j++)
			cin>>m[i][j];
	
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
			cout<<m[i][j]<<" ";
		cout<<endl;
	}
	fun(m,0,0);
	
	if(s==0)
		cout<<-1;
	else
		cout<<1;
	
 	return 0;
}

