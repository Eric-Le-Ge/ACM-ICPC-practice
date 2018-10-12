#include<iostream>
#include<string>
using namespace std;
string s;
int n, first, i, curr, counter;


int main(){
  cin >> n;
  cin >> s;
  first = 1; i=0;
  while(s[i] == 'L'){
    i++;first++;
  }
  curr = first;
  for (;first>0;first--) cout << first << endl;
  while(s[i]){
    while(s[i]=='R'){
      counter = 0;
      if (s[i+1] == 'R'){
        i++;
        curr++;
        cout << curr << endl;
      }
      else if (s[i+1] == 'L'){
        i++; counter++; curr++; 
        while(s[i]=='L') {counter ++; i++;}
        while (counter--) cout << curr +counter << endl;
        curr=i+1;

      }
      else{
        i++;
        curr++;
        cout << curr << endl;
        break;
      }
    }



  }




}
