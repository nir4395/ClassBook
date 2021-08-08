#include <iostream>
#include <math.h>

using namespace std;

/*
This program converts from decimal to two's complement and vice versa based on your selection
The 1st line of input is a natural number (n) larger than 1
The 2nd line of input is the character 't' or 'f'
The 3rd line of input is dependent on your previous selection:
	if 'f' - enter a number between -2^(n-1) and 2^(n-1) - 1
	if 't' - enter a binary number of n bits
The output is also dependent on your selection
	if 'f' - the number will be represented as Two's complement
	if 't' - the number will be represented as a decimal number
*/
int main() {

	int n, num;
	char select;

	cin >> n;
	cin >> select;

	switch (select) {
	case 'f':
	{
		bool isNegative = false;
		int currentNum, remainder;
		int add = 1;

		cin >> num;

		if (num < 0) { // Determines whether the the number is negative or not 
			isNegative = true;
			num = -num;
		}

		// Convert from decimal to two's complement
		for (int i = 0; i < n; i++) {
			currentNum = (num / pow(2, i));
			remainder = currentNum % 2;

			// If the input is negative transform 0's to 1's, and 1's to 0's
			// After the transofrmation, add 1 to the whole number
			if (isNegative) {
				remainder = (remainder + 1) % 2;
				remainder += add;
				if (remainder > 1) {
					remainder = 0;
					add = 1;
				}
				else {
					add = 0;
				}
			}
			cout << remainder;
		}
		break;
	}

	case 't':
	{
		int decimalNum = 0;

		// Convert from two's complement to decimal
		for (int i = n; i > 0; i--) {
			cin >> num;
			if (i == n) { // The leftmost digit is multiplied by a negative number
				decimalNum -= num * pow(2, (i - 1)); // Multiply the bit by 2 to the power of (i-1)
			}
			else {
				decimalNum += num * pow(2, (i - 1)); // Multiply the bit by 2 to the power of (i-1)
			}
		}
		cout << decimalNum << endl;
		break;
	}
	}
}