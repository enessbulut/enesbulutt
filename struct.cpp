#include<iostream>
using namespace std;
struct t {
	string adsoy;
	string ulke;
	char cins;
	int zaman;	
};
int main()
{
struct t sporcu[10];
string a,b,c;
int x;
int y;
int z;
cout<<"Marathonda yarisan atletlerin bilgilerini giriniz:"<<endl;
for(int i=0;i<10;i++){
	cout<<"�s�m soyad ulke cinsiyet(e/k) saat dak�ka san�ye s�ras�yla giriniz:"<<endl;
	cin>>sporcu[i].adsoy>>sporcu[i].cins>>sporcu[i].ulke>>sporcu[i].zaman;
}
z=sporcu[0].zaman;
y=sporcu[0].zaman;
x=sporcu[0].zaman;
for(int i=0;i<10;i++){
	if(sporcu[i].zaman<x && sporcu[i].cins == 'e'){
		x=sporcu[i].zaman;
		a=sporcu[i].adsoy;
	}
	if (sporcu[i].zaman<y && sporcu[i].cins=='k'){
		y=sporcu[i].zaman;
		b=sporcu[i].adsoy;
	}
	if(sporcu[i].zaman<z && sporcu[i].ulke== "Turkiye"){
		z=sporcu[i].zaman;
		c=sporcu[i].adsoy;
	}	
}
cout<<"erkeklerde alt�n madalya:"<<a<<"  " <<x<<endl;
cout<<"kad�nlarda alt�n alt�n madalya:"<<b<<" "<<y<<endl;
cout<<"en iyi T�rk atlet:"<< c<<z<<endl;
return 0;
}

