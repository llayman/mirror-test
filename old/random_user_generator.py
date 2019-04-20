import random
import string

n = 10000000

with open('users_'+str(n)+'.csv', 'w') as out:
    for i in range(n):
        username = ''.join(random.choices(string.ascii_lowercase, k=9) + random.choices(string.digits, k=9))
        password = ''.join(random.choices(string.ascii_letters+string.digits+string.punctuation, k=8))
        out.write('{},{}\n'.format(username, password))



