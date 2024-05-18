#include <iostream>
using namespace std;

struct employee {
  string name;
  int age;
  double salary;
  string gender;
};

const int MAX = 10000;

employee employees_arr[MAX];
int added = 0;	// Number of employees

void read_employee(employee & e) {
  cout<<"Enter employee 4 entries: name , age , salary , gender"<<endl;
  cin >> e.name >> e.age;
  cin >> e.salary >> e.gender;
}

void print_employee(employee & e) {
  cout << e.name << " has salary " << e.salary << "\n";
}
void print_employees() {
  for (int i = 0; i < added; ++i)
    print_employee(employees_arr[i]);
}


int main() {
  read_employee(employees_arr[added++]);
  read_employee(employees_arr[added++]);
  print_employees();
  return 0;
}
