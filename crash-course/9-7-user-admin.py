class User:

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.password = str(password)
        self.login_attempts = 0

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def describe_user(self):
        print('User ' + self.full_name() +' has password: '+ self.password)

    def greet_user(self):
        print('Hello, user ' + self.first_name)

    def reset_login_attempts(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def attempt_login(self):
        self.reset_login_attempts()
        while True:
            if self.login_attempts > 4:
                print('Access denied!')
                return
            self.increment_login_attempts()
            attempted_pass = input()
            if attempted_pass == self.password:
                print('Success!')
                return
            else:
                print('Incorrect password!')


class Privileges:

    def __init__(self):
        self.list_of_privileges = ['Delete posts',
                                   'Create posts',
                                   'Edit posts',
                                   'Ban users',
                                   'Create topics',
                                   'Delete topics']

    def show_privileges(self):
        print('Privileges: ')
        for privilege in self.list_of_privileges:
            print('-' + privilege)


class Admin(User):

    def __init__(self, first_name, last_name, password):
        super().__init__(first_name, last_name, password)
        self.privileges = Privileges()


user_0 = User('john', 'doe', 12345)

user_0.describe_user()
user_0.greet_user()

while True:
    print('Attempt login? (Y/N)')
    answer = input()
    if answer == 'Y':
        user_0.attempt_login()
        break
    elif answer == 'N':
        break
    else:
        print('Unknown command. Try again')

super_user = Admin('James', 'Smith', 'YouW1llN#v#rHac|<Th1s')

super_user.privileges.show_privileges()
