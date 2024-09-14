#include <bits/stdc++.h>
using namespace  std;
#define test int t; cin>>t; while(t--)

void fast(){ios_base::sync_with_stdio(0);cin.tie(0); cout.tie(0);}

int sum(int a,int b){return a+b;}
int mul(int a,int b){return a*b;}

// Pointer To Function That Takes To Integers
int(*FunctionPtr)(int,int);

int compute(int a,int b,int(*FunctionPtr)(int,int))
{
    return (*FunctionPtr)(a,b);
}

void solve ()
{
    FunctionPtr = &sum; // address of function , you can remove it (&) no problem
    int val = (*FunctionPtr)(2,5);
    cout << val << "\n";
    val = compute(2,5,mul);
    cout << val << "\n";

    // array of pointers to function
    int (*arr[2])(int,int);
    arr[0] = sum;
    arr[1] = mul;

    val = (*arr[0])(3,5);
    cout << val << "\n";

    val = (*arr[1])(3,5);
    cout << val << "\n";
    
    // you can use this nice idea to ask a user to enter 0 for sum 1 for mul 
    // 2 for sub and so on , put functions in the array and call them with the 
    // input of user
}

int main()
{
  fast();
  //test
  solve();
}
