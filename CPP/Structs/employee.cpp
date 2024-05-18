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

void read_employee() {
  cout<<"Enter employee 4 entries: name , age , salary , gender"<<endl;
  cin >> employees_arr[added].name >> employees_arr[added].age;
  cin >> employees_arr[added].salary >> employees_arr[added].gender;
  added++;
}

void print_employees() {
  for (int i = 0; i < added; ++i) {
    employee e = employees_arr[i];
    cout << e.name << " has salary " << e.salary << "\n";
  }
}

int main() {
  employee first = { "mostafa", 22, 12000.5, "Male" };
  employees_arr[added++] = first;

  employees_arr[added].name = "hani";
  employees_arr[added].age = 55;
  employees_arr[added].salary = 75000;
  employees_arr[added].gender = "Male";
  added++;

  read_employee();
  print_employees();
  return 0;
}
