def greet(fun):
    def wrapper(name):
        print('before');
        fun(name);
        print('after');
    return wrapper;


@greet
def sayName(name):
    print(name);

sayName('soe pyae moe');