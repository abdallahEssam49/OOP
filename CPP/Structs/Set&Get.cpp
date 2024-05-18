#include <iostream>
using namespace std;

struct employee {
  string name;
  int age;
  double salary;
  string gender;

void print_employee() {
  cout << name << " has salary " << salary << "\n";
}

void read_employee() {
  cout<<"Enter employee 4 entries: name , age , salary , gender"<<endl;
  cin >> name >> age;
  cin >> salary >> gender;
}

int get_age() {
  return age;
}
void set_age(int new_age) {
  age = new_age;
}
};

const int MAX = 10000;

employee employees_arr[MAX];
int added = 0;	// Number of employees

void print_employees() {
  for (int i = 0; i < added; ++i)
      employees_arr[i].print_employee();
}

int main() {
  employees_arr[added++].read_employee();
  employees_arr[added++].read_employee();
  print_employees();
  return 0;
}
