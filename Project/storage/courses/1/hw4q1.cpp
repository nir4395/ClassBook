#include <iostream>
#include <math.h>

using namespace std;

/* 
This program converts numbers from base 'a' to base 'b'
The 1st line of input is two integers 'a' and 'b' - between 2 and 10
The 2nd line of input is 'n' a natural number
The 3rd line of input is a number in base 'a' made of spaced 'n' digits
*/

int main() {
	int a, b, n;
	cin >> a >> b;
	cin >> n;


	int decimalNum = 0;
	int digit;
	// Covnert from base 'a' to decimal 
	for (int i = n;i > 0;i--) {
		cin >> digit;
		decimalNum += digit * pow(a, i-1); // Multiply the digit by 'a' to power of (i-1)
	}

	int remainder;

	// Convert from decimal to base 'b'
	while (decimalNum > 0) {
		remainder = decimalNum % b;
		decimalNum = decimalNum / b;
		cout << remainder;

	}

}