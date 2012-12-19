#include <stdio.h>

int odd_even(int x){
  if ((x & 1) == 0){
	printf ("x is even\n");
	}
	else {
	  printf ("x is odd\n");
	}
	return 0;
}

int main() {
  int x;
  int selection;

  do{
  printf("\n0 - Exit ");
  printf("\n1 - OddEven: ");
  printf("\nSelect option: ");
  scanf("%d", &selection);
  printf("\nEnter parameter: ");
  scanf("%d", &x);

  switch (selection)
  {  
	case 0:
	  break;
    case 1:
	odd_even(1);
	break;
  default:
	break;
	}
  }
  while (selection != 0);

  return 0;	
}
