class Pynary:
    def __init__(self, decimal):
        self.decimal = decimal;
        self.binary = self.decimal_to_binary(decimal);

    def get_decimal(self): 
        return self.decimal;

    def set_decimal(self, decimal):
        self.decimal = decimal;

    def get_binary(self):
        return self.binary;

    def set_binary(self, binary):
        self.binary = binary;

    def decimal_to_binary(self, decimal):
        binary = ""
        while True:
            if decimal >= 1:
                binary += str(decimal % 2);
                decimal = decimal // 2;
            else:
                break;
        return binary[::-1];

    def binary_to_decimal(self, binary):
        decimal = 0;
        for index, token in enumerate(reversed(binary)):
            if token == "1" and decimal == 0: decimal = 1;
            elif token == "1" and decimal != 0: decimal += 2**index;
            else: continue;
        self.decimal = decimal;

        
if __name__ == "__main__":
    pynary0 = Pynary(0);
    print(f"0d: {pynary0.get_decimal()} \t\t 0b: {pynary0.get_binary()}");
    pynary5 = Pynary(5);
    print(f"5d: {pynary5.get_decimal()} \t\t 5b: {pynary5.get_binary()}");
    pynary10 = Pynary(10);
    print(f"10d: {pynary10.get_decimal()} \t 10b: {pynary10.get_binary()}");
    pynary15 = Pynary(15);
    print(f"15d: {pynary15.get_decimal()} \t 15b: {pynary15.get_binary()}");
    pynary20 = Pynary(20);
    print(f"20d: {pynary20.get_decimal()} \t 20b: {pynary20.get_binary()}");
    pynary25 = Pynary(25);
    print(f"25d: {pynary25.get_decimal()} \t 25b: {pynary25.get_binary()}");
    pynary30 = Pynary(30);
    print(f"30d: {pynary30.get_decimal()} \t 30b: {pynary30.get_binary()}");
    pynary35 = Pynary(35);
    print(f"35d: {pynary35.get_decimal()} \t 35b: {pynary35.get_binary()}");
    pynary40 = Pynary(40);
    print(f"40d: {pynary40.get_decimal()} \t 40b: {pynary40.get_binary()}");