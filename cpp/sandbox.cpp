#include <iostream>
using namespace std;

int main() {
  int x = 0;

	do {
	  cout <<"x=";
	  cin >> x;
  if ((x & 1) == 0) {
	cout<< "x is even\n";
  }
  else{
	cout<<"x is odd\n";
  }
	}while ( x != 0);

  return 0;
}
