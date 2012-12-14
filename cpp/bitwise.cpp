#include <iostream>
using namespace std;

int oddEven(){
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

int nthBitTest(){
  int x = 0;
  int n = 0;

  do {
	cout <<"x=";
	cin >>x;
	cout <<"n=";
	cin>>n;
	  if (x & (1<<n)) {
		cout<<"n-th bit is set\n";
	  }
	  else{
		cout <<"n-th bit is not set\n";
	  }
  }while (x != 0);
  return 0;
}

int nthBitSet(int x, int n){
  int y = x | (1<<n);
  return y;
}

int nthBitUnset(int x, int n){
  int y = x & ~(1<<n);
  return y;
}

int main() {
  int selection = 0;

  do{
	cout << "0: Exit\n";
	cout << "1: Bitwise odd-even test\n";
	cout << "2: Test n-th bit\n";
	cout << "Select function: ";
	cin >> selection;

	switch (selection){
		case 0:
		  break;
		case 1:
		  oddEven();
		  break;
		case 2:
		  nthBitTest();
		  break;
		default:
		  break;
	}

  } while (selection != 0);
  
  return 0;
}
