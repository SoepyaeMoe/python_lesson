person = {};

while True:
    name = input('Name:');
    age = input('Age:');
    person[name] = age;
    isStop = input('Do you want to stop it? [y/n]');
    if isStop == 'y':
        break;

    print(person.items());

#for looping in dictionary use .items() 
# for (key, value) in person.items():
#     print(f'{key} is {value} years old.');

ages = list(person.values());
for age in set(ages):
    count = ages.count(age);
    print(f'{age} year is - {count}');