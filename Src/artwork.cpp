#include<iostream>
using namespace std;
int art[1000][1000];
int n,m,q,x1,y1,x2,y2,x,y,b;
void stroke(){
    if (art[x][y] == 1) return;
    art[x][y] = 1;
    if (x==0){
        if (y==0){
            if (art[1][0] && art[0][1]) b--;
        }
        else if (y==m-1){
            if (art[x][y-1] &&art[x+1][y]) b--;
        }
        else {
            if (art[x][y-1]&&art[x+1][y]&&art[x][y+1]) b--;
            else if ((art[x][y-1]==0) && art[x+1][y] && (art[x][y+1]==0))b++;
        }
    }
    else if (x==n-1){
        if (y==0){
            if (art[x-1][0] && art[x][1]) b--;
        }
        else if (y==m-1){
            if (art[x][y-1] &&art[x-1][y]) b--;
        }
        else {
            if (art[x][y-1]&&art[x-1][y]&&art[x][y+1]) b--;
            else if ((art[x][y-1]==0) && art[x-1][y] && (art[x][y+1]==0))b++;
        }
    }
    else{
        if (y==0){
            if (art[x-1][y]&&art[x][y+1]&&art[x+1][y]) b--;
            else if ((art[x-1][y]==0)&&art[x][y+1]&&(art[x+1][y]==0)) b++;
        }
        else if (y==m-1){
            if (art[x-1][y]&&art[x][y-1]&&art[x+1][y]) b--;
            else if ((art[x-1][y]==0)&&art[x][y-1]&&(art[x+1][y]==0)) b++;
        }
        else{
            if (art[x-1][y]&&art[x+1][y]&&(art[x][y-1]==0)&&(art[x][y+1]==0)) b++;
            else if (art[x][y-1]&&art[x][y+1]&&(art[x-1][y]==0)&&(art[x+1][y]==0)) b++;
            else if (art[x][y-1]&&art[x][y+1]&&art[x-1][y]&&art[x+1][y]) b--;
        }
        
        
    }
    
    
}
int main(){
    cin >> n >> m >> q;
    b = 1;
    for (int i=0;i<1000;i++){
        for (int j=0;j<1000;j++){
            art[i][j] = 0;
        }
    }
    while(q--){
        cin >> x1 >> y1 >> x2 >> y2;
        if (x1 == x2){
            x = x1-1;
            for (y=y1-1;y<y2;y++){
                stroke();
            }
        }
        else{
            y = y1-1;
            for (x=x1-1;x<x2;x++){
                stroke();
            }
        }
        cout << b << endl;
        
    }
    
}

