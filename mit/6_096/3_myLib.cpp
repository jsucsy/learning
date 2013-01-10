#include <iostream>
#include "3_myLib.h"
using namespace std;

int cube(int x)
{
  return x*square(x);
}

int square(int x)
{
  return x*x;
}

void increment(int &a){
  a = a+1;
  cout << "a in increment " << a << endl;
}

void swap(int &a, int &b){
  int t = a;
  a =b;
  b = t;
}

int divide(int numerator, int denominator, int &remainder)
{
  remainder = numerator % denominator;
  return numerator / denominator;
}

int main(){
  int x = 3;
  cout <<"x squared is " <<square(x)<<endl;
  cout <<"x cubed is " << cube(x)<<endl;

  int q = 3;
  increment(q);
  cout << "q in main " << q << endl;

  int r = 5;
  swap(q, r);
  cout << "q " << q << endl;
  cout << "r " << r << endl;

  int num = 14;
  int den =4;
  int rem;

  int result = divide(num, den, rem);
  cout << result << "*" << den << "+" << rem << "=" << num << endl;

  return 0;
}
