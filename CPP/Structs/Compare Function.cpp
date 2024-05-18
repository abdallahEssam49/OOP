#include <iostream>
#include <algorithm>
using namespace std;

struct employee {
  string name;
  int age;
  double salary;
  string gender;

void read_employee() {
  cout<<"Enter employee 4 entries: name , age , salary , gender"<<endl;
  cin >> name >> age;
  cin >> salary >> gender;
}

  void print_employee() {
    cout << name << " has salary " << salary << "\n";
  }

  int get_age() {
    return age;
  }
  void set_age(int new_age) {
    age = new_age;
  }
};

const int MAX = 10000;

employee emplyees_arr[MAX];
int added = 0;	// Number of employees

void print_employees() {
  cout << "******************\n";
  for (int i = 0; i < added; ++i)
    emplyees_arr[i].print_employee();
}

bool compare_name(employee &a, employee &b) {
  return a.name < b.name;	// smaller name first
}

bool compare_salary(employee &a, employee &b) {
  return a.salary > b.salary;	// bigger salary salary
}

bool compare_name_salary(employee &a, employee &b) {
  // smaller name first, if tie smaller salary
  if (a.name != b.name)
    return a.name < b.name;
  return a.salary < b.salary;
}

int main() {
  int arr[5] = { 5, 1, 3, 2, 4 };
  sort(arr, arr + 5);	
  for (int i = 0; i < 5; ++i)
    cout << arr[i] << " ";
  cout << "\n";

  emplyees_arr[added++].read_employee();
  emplyees_arr[added++].read_employee();
  emplyees_arr[added++].read_employee();

  sort(emplyees_arr, emplyees_arr + added, compare_name);
  print_employees();

  sort(emplyees_arr, emplyees_arr + added, compare_salary);
  print_employees();

  sort(emplyees_arr, emplyees_arr + added, compare_name_salary);
  print_employees();

  return 0;
}
