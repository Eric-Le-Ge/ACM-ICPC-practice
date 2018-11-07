#include<iostream>
#include<math.h>
using namespace std;
int l;

int main(){
	double x1, x2, y1, y2, r;
	cin >> l;
	while(l--){
		cin >> x1 >> y1 >> x2 >> y2 >> r;
		double q = sqrt(pow((x2-x1),2) + pow((y2-y1),2));
		double y3 = (y1+y2)/2;
		double x3 = (x1+x2)/2;
		double basex = sqrt(pow(r,2)-pow((q/2),2))*(y1-y2)/q; //calculate once
		double basey = sqrt(pow(r,2)-pow((q/2),2))*(x2-x1)/q; //calculate once

		double centerx1 = x3 + basex; //center x of circle 1
		double centery1 = y3 + basey; //center y of circle 1
		double centerx2 = x3 - basex; //center x of circle 2
		double centery2 = y3 - basey; //center y of circle 2
		cout << centerx1 << centery1 << centerx2 << centery2 << endl;
	}
}
