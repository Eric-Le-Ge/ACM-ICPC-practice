#include <cstdio>
#include <algorithm>
using namespace std;

char s[31];
int cur;

int Fill(){
cur = 0;
for (int j = 0,k=0;k<7;j++){
if (s[j]>='0'&&s[j]<='9'){
k++;
cur*=10;
cur+=s[j]-'0';
}
else if(s[j]>='A'&&s[j]<'Z'){
cur*=10;k++;
cur+=((s[j]-'A'-(s[j]>'Q'))/3+2);
}
}
return cur;
}

int main(){
int n;scanf("%d",&n);
int data[n];getchar();
for (int i=0;i<n;i++){
gets(s);
data[i]= Fill();
}
sort(data,data+n);
bool dup = false;n--;
for (int k=0,m=1;k<n;k+=m=1){
while(data[k] == data[k+1]){
m++;k++;
}
if(m>1){
dup=true;
printf("%03d-%04d %d\n",data[k]/10000,data[k]%10000,m);
}
}
if(!dup){
printf("No duplicates.\n");
}
return 0;
}
