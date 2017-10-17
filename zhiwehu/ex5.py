class InAndOut:

    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())


input_str = InAndOut()

input_str.get_string()
input_str.print_string()
