#include<iostream>
using namespace std;
int dx[8] = {-1,-1,0,1,1,1,0,-1};
int dy[8] = {0,1,1,1,0,-1,-1,-1};
int art[1004004];
int n,m,q,x1,y1,x2,y2,cx,cy,t,b;
int d,w,w0,dpt;
//disjoint sets
int par[1002];
int Rank[1002];
void init(int N){
    for (int i=0;i<N;i++){
        par[i] = i;
        Rank[i] = 0;
    }
}

int find(int x){
    if (par[x]==x){
        return x;
    } else {
        return par[x] = find(par[x]);
    }
}

void unite(int x,int y){
    x = find(x);
    y = find(y);
    if (x==y) return;
    if (Rank[x]<Rank[y]){
        par[x]=y;
    }
    else{
        par[y] = x;
        if (Rank[x]==Rank[y]) Rank[x]++;
    }
}

bool same(int x, int y){
    return find(x) == find(y);
}

int lin(int x, int y){
    return y*(n+2)+x;
}

void stroke(){
    int tx, ty;
    d=0,w=0,w0=0,dpt=0;
    if (art[lin(cx,cy)] == 1) return;
    art[lin(cx,cy)] = 1;
    if (art[lin(cx,cy-1)]&&art[lin(cx,cy+1)]&&art[lin(cx-1,cy)]&&art[lin(cx+1,cy)]){
      b--;
      return;
    }
    //else if (art[lin(cx-1,cy)]&&art[lin(cx+1,cy)]&&(art[lin(cx,cy+1)]==0)&&(art[lin(cx,cy-1)]==0) && same(lin(cx-1,cy),lin(cx+1,cy))) b++;
    //else if (art[lin(cx,cy-1)]&&art[lin(cx,cy+1)]&&(art[lin(cx-1,cy)]==0)&&(art[lin(cx+1,cy)]==0) && same(lin(cx,cy-1),lin(cx,cy+1))) b++;
    for (int i=0;i<8;i++){
      t = lin(cx+dx[i],cy+dy[i]);
      if (art[t]){
        if (w == 0 && d==0) d=1;
        else if (w && d==0){
          w=1;
          d=1;
        }
        else if (w && w0 == 0 && same(t,dpt)) swap(w,w0);
        else if (w && w0 && same(t,dpt)){
          w = w0 = 0;
          b++;
        }
        dpt = t;
      }
      else if (i%2==0 && w==0) w=1;
    }
    t = lin(cx+dx[0],cy+dy[0]);
    if (art[t]&&w && w0 && same(t,dpt)) b++;


    for (int i=0;i<8;i++){

        t = lin(cx+dx[i],cy+dy[i]);
        if (art[t]) unite(t,lin(cx,cy));
    }



    // for (ty=0;ty<=m+1;ty++){
    //   for (tx=0;tx<=n+1;tx++){
    //
    //     cout << art[lin(tx, ty)] << " ";
    //   }
    //   cout <<endl;
    //
    //
    // }
    // cout << endl;
}


int main(){
    cin >> n >> m >> q;
    b = 1;
    fill(art, art+1004004,0);
    init((n+2)*(m+2));
    for (cx=0,cy=0;cy<m+1;cy++){
        unite(lin(cx, cy),lin(cx, cy+1));
        art[lin(cx, cy)] = 1;
    }
    for (cx=0,cy=m+1;cx<n+1;cx++){
        unite(lin(cx, cy),lin(cx+1, cy));
        art[lin(cx, cy)] = 1;
    }
    for (cx=n+1,cy=m+1;cy>0;cy--){
        unite(lin(cx, cy),lin(cx, cy-1));
        art[lin(cx, cy)] = 1;
    }
    for (cx=n+1,cy=0;cx>0;cx--){
        unite(lin(cx, cy),lin(cx-1, cy));
        art[lin(cx, cy)] = 1;
    }




    while(q--){
        cin >> x1 >> y1 >> x2 >> y2;

        if (x1 == x2){
            cx = x1;
            cy = y1;
            for (;cy<=y2;cy++){

                stroke();

            }
        }
        else{
            cy = y1;
            cx = x1;
            for (;cx<=x2;cx++){

                stroke();

            }
        }
        cout << b << endl;



    }
}
