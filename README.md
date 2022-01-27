# Pynary
_Binary to Decimal and Decimal to Binary Converter in Python_ 

## Purpose and Description
This project was created to help with my Introduction to Computation Course at the Pennsylvania State University. We were tasked to create a Deterministic Finite Automata that accepted binary numbers that were divisible by 5. I simply used this to convert multiples of 5 to their binary representation and print them to the console.  

---

## Implementation
To create this project I created the `Pynary` class with attributes **_decimal_** and **_binary_** that contains the setter and getter methods for the classes attributes, `decimal_to_binary(self, decimal)` and `binary_to_decimal(self, binary)`

```Python
decimal_to_binary(self, decimal):
    binary = ""
    while True:
        if decimal >= 1:
            binary += str(decimal % 2);
            decimal = decimal // 2;
        else:
            break;
    return binary[::-1];
```
* The Decimal to Binary method takes an unsigned integer, decimal, value and converts it to a binary string. We take this decimal value and find its remainder to 2 and then use integer division by 2 to assign decimal to the next significant bit. We do this until the decimal value becomes 0 and return the reverse the string we got.   
Thanks to [geeksforgeeks](https://www.geeksforgeeks.org/program-decimal-binary-conversion/) for helping me get started with this method.  

```Python
def binary_to_decimal(self, binary):
    decimal = 0;
    for index, token in enumerate(reversed(binary)):
        if token == "1" and decimal == 0: decimal = 1;
        elif token == "1" and decimal != 0: decimal += 2**index;
        else: continue;
    self.decimal = decimal;
```
* The Binary to Decimal method takes in a string of binary numbers and converts it to its corresponding decimal value. We take this string value and read each value as well as its index in the string. The index will help us find the value we need to raise 2 to. If it is a 1 and it is the first iteration, we make decimal = 0. If it is not the first iteration then we add 2 to the power of the index to the current decimal value. if it is 0 then we just keep iterating until we find another 1 or the end of the string. Then we return the decimal value. 