#include<iostream>
using namespace std;

int ww, wb, bw, bb, L;

int start, end0,d,bc, bn;

int WW[3000],WB[3000],BW[3000],BB[3000];
int yesww[25],yeswb[25],yesbw[25],yesbb[25];

int curr, next0;
int dp_curr[5];
int dp_next[5];
int INF = 50000;

int black(int key){
  int tmp = key%12;
  if (tmp==0||tmp==2||tmp==5||tmp==7||tmp==10) return 1;
  else return 0;
}

int lin(int s, int e, int index){
  return s*60 + e*12 +index;

}

int main(){
  fill(yesww, yesww+25,0);
  fill(yeswb, yeswb+25,0);
  fill(yesbw, yesbw+25,0);
  fill(yesbb, yesbb+25,0);
  cin >> ww >> wb >> bw >> bb >> L;
  for (int i = 0;i<ww;i++){
    cin >> start >> end0;
    for (int j=0;j<12;j++){
      cin >> d;
      WW[lin(start, end0, j)] = d;
      yesww[start*5+end0] = 1;
    }
  }
  for (int i = 0;i<wb;i++){
    cin >> start >> end0;
    for (int j=0;j<12;j++){
      cin >> d;
      WB[lin(start, end0, j)] = d;
      yeswb[start*5+end0] = 1;
    }
  }
  for (int i = 0;i<bw;i++){
    cin >> start >> end0;
    for (int j=0;j<12;j++){
      cin >> d;
      BW[lin(start, end0, j)] = d;
      yesbw[start*5+end0] = 1;
    }
  }
  for (int i = 0;i<bb;i++){
    cin >> start >> end0;
    for (int j=0;j<12;j++){
      cin >> d;
      BB[lin(start, end0, j)] = d;
      yesbb[start*5+end0] = 1;
    }
  }


  fill(dp_curr, dp_curr+5, 0);
  fill(dp_next, dp_next+5, 0);
  cin >> curr;
  for (int i=1;i<L;i++){
    cin >> next0;
    d = next0-curr;
    if (d==0) continue;
    swap(dp_curr,dp_next);
    fill(dp_next,dp_next+5,INF);
    bc = black(curr);bn = black(next0);
    if (d>0){

      if(!bc && !bn){
        for (int j=1;j<6;j++){
          for (int k=1;k<6;k++){
            if (yesww[j*5+k]) dp_next[k-1] = min(dp_next[k-1],dp_curr[j-1]+WW[lin(j,k,d-1)]);
          }
        }
      }
      else if(bc && !bn){
        for (int j=1;j<6;j++){
          for (int k=1;k<6;k++){
            if (yesbw[j*5+k]) dp_next[k-1] = min(dp_next[k-1],dp_curr[j-1]+BW[lin(j,k,d-1)]);
          }
        }
      }
      else if(!bc && bn){
        for (int j=1;j<6;j++){
          for (int k=1;k<6;k++){
            if (yeswb[j*5+k]) dp_next[k-1] = min(dp_next[k-1],dp_curr[j-1]+WB[lin(j,k,d-1)]);
          }
        }
      }
      else if(bc && bn){
        for (int j=1;j<6;j++){
          for (int k=1;k<6;k++){
            if (yesbb[j*5+k]) dp_next[k-1] = min(dp_next[k-1],dp_curr[j-1]+BB[lin(j,k,d-1)]);
          }
        }
      }
    }
    else{
      if(!bc && !bn){
        for (int j=1;j<6;j++){
          for (int k=1;k<6;k++){
            if (yesww[k*5+j]) dp_next[k-1] = min(dp_next[k-1],dp_curr[j-1]+WW[lin(k,j,-d-1)]);
          }
        }
      }
      else if(bc && !bn){
        for (int j=1;j<6;j++){
          for (int k=1;k<6;k++){
            if (yeswb[k*5+j]) dp_next[k-1] = min(dp_next[k-1],dp_curr[j-1]+WB[lin(k,j,-d-1)]);
          }
        }
      }
      else if(!bc && bn){
        for (int j=1;j<6;j++){
          for (int k=1;k<6;k++){
            if (yesbw[k*5+j]) dp_next[k-1] = min(dp_next[k-1],dp_curr[j-1]+BW[lin(k,j,-d-1)]);
          }
        }
      }
      else if(bc && bn){
        for (int j=1;j<6;j++){
          for (int k=1;k<6;k++){
            if (yesbb[k*5+j]) dp_next[k-1] = min(dp_next[k-1],dp_curr[j-1]+BB[lin(k,j,-d-1)]);
          }
        }
      }

    }

    curr = next0;
    //
    // for (int g=0;g<5;g++){
    //   cout << dp_next[g] << " ";
    // }
    // cout << endl;


  }

  d = dp_next[0];
  for (int i=1;i<5;i++){
    d = min(d,dp_next[i]);
  }
  cout << d << endl;



}
