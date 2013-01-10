#include <iostream>
#include <cstring>
using namespace std;

int main() {
  char frag1[] = "I'm a s";
  char frag2[] = "tring!";
  char frag3[20];
  char finalString[20]= "";

  strcpy(frag3, frag1);
  strcat(finalString, frag3);
  strcat(finalString, frag2);

  cout << finalString << endl;
  return 0;
}
