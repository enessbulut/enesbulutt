#include<iostream>
#include<math.h>
using namespace std;
class dikdortgen;
class nokta {
	public:
		int x;
		int y;
		nokta(int _x,int _y):x(_x),y(_y){}
		void xata(int _x){x= _x;}
		void yata(int _y){y= _y;}
		friend class dikdortgen;
}; 
class dikdortgen {
	public:
		nokta a;
		nokta b;
		dikdortgen (nokta _a,nokta _b):a(_a),b(_b){}
		float alan();
		int cevre();
};
float dikdortgen :: alan(){
	return abs((a.x-b.x)*(a.y-b.y));
}
int dikdortgen::cevre(){
	return abs(2*((a.x-b.x)+(a.y-b.y)));
}
int main(){
int x,y;
cout<<"a noktasý (x,y):";
cin>>x>>y;
nokta a(x,y);
cout<<"b noktasý (x,y):";
cin>>x>>y;
nokta b(x,y);
dikdortgen d(a,b);
cout<<"Cevre:"<<d.cevre()<<endl;
cout<<"alan:"<<d.alan()<<endl;
return 0;	
}
