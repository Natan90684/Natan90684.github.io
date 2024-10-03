class UserManager:
    def __init__(self):
        self.users = {}
        self.banned_users = []

    def is_valid_registration(self, email, username, password, birthday):
        if int(birthday.split('-')[0]) <= (2024 - 12):  # Ensure the user is 12 years or older
            return email and username and password and "@" in email and username not in self.users
        return False

    def add_user(self, email, username, password):
        self.users[username] = {'email': email, 'password': password}

    def is_valid_login(self, username, password):
        return username in self.users and self.users[username]['password'] == password

    def ban_user(self, username):
        if username in self.users:
            self.banned_users.append(username)
            del self.users[username]

    def get_banned_users(self):
        return self.banned_users
