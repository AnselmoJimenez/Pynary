from inspect import _void
import string


class Pynary:
    def __init__(self):
        pass;
    
    def decimal_to_binary(self, decimal):
        if decimal >= 1:
            self.decimal_to_binary(decimal // 2);
        print(decimal % 2, end="");
        
            



if __name__ == "__main__":
    pynary = Pynary();
    print("0: ", end="\t");
    pynary.decimal_to_binary(0);
    print();
    print("5: ", end="\t");
    pynary.decimal_to_binary(5);
    print();
    print("10: ", end="\t");
    pynary.decimal_to_binary(10);
    print();
    print("15: ", end="\t");
    pynary.decimal_to_binary(15);
    print();
    print("20: ", end="\t");
    pynary.decimal_to_binary(20);
    print();
    print("25: ", end="\t");
    pynary.decimal_to_binary(25);
    print();
    print("30: ", end="\t");
    pynary.decimal_to_binary(30);
    print();
    print("35: ", end="\t");
    pynary.decimal_to_binary(35);
    print();
    print("40: ", end="\t");
    pynary.decimal_to_binary(40);
    print();
    print("45: ", end="\t");
    pynary.decimal_to_binary(45);
    print();
    print("50: ", end="\t");
    pynary.decimal_to_binary(50);
    print();