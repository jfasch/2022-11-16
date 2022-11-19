def print_user(user):
    print(f'ID:{user.id}, Firstname:{user.firstname}, Lastname:{user.lastname}, Date of birth: {user.birth}')

def print_users(users):
    for u in users:
        print_user(u)

