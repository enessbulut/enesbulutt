#include<iostream>
#include<cmath>
using namespace std;
void kartezyendenkutupsala(int x, int y,float & r,float & a )
{
	r=sqrt(x*x+y*y);
	a=atan(y/x);
}
void kutuptankartezyene(float a,float r, int & x, int & y)
{
	x=r*cos(a);
	y=r*sin(a);
}
int main()
{
	int x,y;
	float a,r,b;
	cout<<"1:kartezyenden kutupsala";
	cout<<"2:kutupsaldan kartezyene";
	cin>>b;
	if(b==1){
		cout<<"x değerini giriniz:";
		cin>>x;
		cout<<"y değerini giriniz:";
		cin>>y;
		kartezyendenkutupsala(x,y,a,r);
		cout<<"r="<<r<<"  "<<"a="<<a;
	}
	else if(b==2){
		cout<<"a ve r değerlerini giriniz:";
		cin>>a>>r;
		kutuptankartezyene(a,r,x,y);
		cout<<"x="<<x<<"  "<<"y="<<y;
	}
	return 0;
}
