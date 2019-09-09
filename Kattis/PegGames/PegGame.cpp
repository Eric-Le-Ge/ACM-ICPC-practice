#include<iostream>
#include<vector>
using namespace std;

int trans[36][3] = {{0,1,3},{0,2,5},{1,3,6},{1,4,8},{2,4,7},
{2,5,9},{3,1,0},{3,4,5},{3,6,10},{3,7,12},{4,7,11},
{4,8,13},{5,2,0},{5,4,3},{5,8,12},{5,9,14},{6,3,1},
{6,7,8},{7,4,2},{7,8,9},{8,7,6},{8,4,1},{9,8,7},{9,5,2},
{10,6,3},{10,11,12},{11,7,4},{11,12,13},{12,7,3},{12,8,5},
{12,11,10},{12,13,14},{13,8,4},{13,12,11},{14,9,5},{14,13,12}};

int net(int board[15]){
	vector<int> scores;
	for (int i=0;i<36;i++){
		int dest = trans[i][0];
		int mid = trans[i][1];
		int src = trans[i][2];
		if (board[dest] == 0 and board[mid] and board[src]){
			int m = board[mid]; int s = board[src];
			int score = board[mid] * board[src];
			board[mid] = 0; board[src] = 0; board[dest] = s;
			int op = net(board);
			scores.push_back(score - op);
			board[mid] = m; board[src] = s; board[dest] = 0;
		}
	}
	if (scores.size() == 0) return 0;
	int ma = scores[0];
	for (int i=0;i<scores.size();i++){
		ma = max(scores[i], ma);
	}
	return ma;
}

int main(){
	int board[15];
	for (int i=0;i<15;i++){
		cin >> board[i];
	}
	cout << net(board) << endl;
}