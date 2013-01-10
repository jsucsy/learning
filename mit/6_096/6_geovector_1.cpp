#include <iostream>
using namespace std;

void offsetVector(double &x0, double &x1, double &y0, double &y1,
		  double offsetX, double offsetY) {
  x0 += offsetX;
  x1 += offsetX;
  y0 += offsetY;
  y1 += offsetY;
}

void printVector(double x0, double x1, double y0, double y1){
  cout << "(" << x0 << "," << y0 << ") ->("
       << x1 << "," << y1 << ")" << endl;
}

int main() {
  double xStart = 1.2;
  double xEnd = 2.0;
  double yStart = 0.4;
  double yEnd = 1.6;

  offsetVector(xStart, xEnd, yStart, yEnd, 1.0, 1.5);
  printVector(xStart, xEnd, yStart, yEnd);
  return 0;
}
