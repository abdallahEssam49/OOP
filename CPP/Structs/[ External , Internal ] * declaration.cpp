#include <bits/stdc++.h>
using namespace  std;
#define test int t; cin>>t; while(t--)

void fast(){ios_base::sync_with_stdio(0);cin.tie(0); cout.tie(0);}

struct Employee{ // External declaration

    string Name;
    string Address;
    string Email;
    double Salary;

    void print(){
        cout << "Name : " << Name << "\n\n";
        cout << "Address : " << Address << "\n\n";
        cout << "Email : " << Email << "\n\n";
        cout << "Salary : " << Salary << " $" << "\n\n";
    }

};

void solve ()
{
    Employee Abdo;
    Abdo.Address = "Banha , Egypt";
    Abdo.Email = "abdallah2029@gmail.com";
    Abdo.Name = "Abdallah Essam";
    Abdo.Salary = 200000;

    Abdo.print();

struct Emp{ // Internal declaration

    string name ;
    double salary ;
};

    cout << "\n\n";
    Emp Emp_array[3];
    for(int i=0;i<3;++i)cin >> Emp_array[i].name >> Emp_array[i].salary ;
    for(int i=0;i<3;++i){

        cout << "Name : " << Emp_array[i].name << "\n"
        <<"Salary : " << Emp_array[i].salary <<"\n\n";
    }

}

int main()
{
  fast();
  //test
  solve();
}
