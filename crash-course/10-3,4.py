class GuestBook:

    def __init__(self, directory):
        self.directory = directory + 'guest_book.txt'
        self.file = open(self.directory, 'w')
        self.file.close()

    def add(self, name):
        self.file = open(self.directory, 'a')
        self.file.write(name + '\n')
        self.file.close()

    def erase(self):
        self.file = open(self.directory, 'w')
        self.file.close()

    def show(self):
        self.file = open(self.directory, 'r')
        print(''.join(self.file.readlines()))
        self.file.close()


my_guests = GuestBook('')

while True:
    guest = input()
    if guest:
        my_guests.add(guest)
    else:
        break

my_guests.show()
