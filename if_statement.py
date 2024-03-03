name = input('Name:');
password = input('Password:');

inputName = "Soe Pyae Moe";
inputPassword = "password";
if name != inputName:
    print('username incorrect');
elif password != inputPassword:
    print('password incorrect');
elif name == inputName and inputPassword == password:
    print('login success');
else:
    print('User name or password incorrect!Try again!');