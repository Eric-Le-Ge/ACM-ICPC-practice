#include <iostream>
using namespace std;
int modInverse(int a, int m);
int power(int x, unsigned int y, unsigned int m);
int gcd(int a, int b);
int crt(int num[], int rem[], int k);

#define MOD 1000000007;
// static ints
int T , n, p;

int solve()
{
	return 0
}


int main()
{
	cin >> T;
	for (int t = 0;t < T; t++)
	{
		// IO
		cin >> n >> p;
		// solve
		int ans = solve();
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
}

// Function to find modular inverse of a under modulo m 
// Assumption: m is prime
int modInverse(int a, int m) 
{ 
    return power(a, m-2, m);
}

// To compute x^y under modulo m 
int power(int x, unsigned int y, unsigned int m) 
{ 
    if (y == 0) 
        return 1; 
    int p = power(x, y/2, m) % m; 
    p = (p * p) % m; 
    return (y%2 == 0)? p : (x * p) % m; 
}

// Function to return gcd of a and b 
int gcd(int a, int b) 
{ 
    if (a == 0) 
        return b; 
    return gcd(b%a, a); 
} 

int crt(int num[], int rem[], int k)
{
    // Compute product of all numbers
    int prod = 1;
    for (int i = 0; i < k; i++)
    prod *= num[i];
    
    // Initialize result
    int result = 0;
    
    // Apply above formula
    for (int i = 0; i < k; i++)
    {
        int pp = prod / num[i];
        result += rem[i] * modInverse(pp, num[i]) * pp;
    }
    
    return result % prod;
}
