#include <stdio.h>
/* jsu
created 16 Dec 2012
last edit 16 Dec 2012
***correct solution***
*/

int main(){
  int x = 3;
  int y = 5;
  int limit = 1000;
  int i;
  int total = 0;
  for (i = 1; i < limit; i++){
	if (i % x == 0) {
	  	total += i;
		printf("%d\n", i);}
	else if (i % y == 0){
	  	total += i;
		printf("%d\n", i);
	  }
  }
  printf ("%d\n", total);
}
