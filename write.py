# with open('./text.txt', 'w') as file: # 'w' optional for 'write'
#     file.write('Soe Pyae Moe,');

# #another work
# with open ('./text.txt', 'a') as file: # 'a' optional for 'amend || add'
#     file.write('I want to be a professional developer');

sen = ['Soe Pyae Moe', 'I am 21 years old.'];
with open('./text.txt', 'a') as file:
    file.writelines(sen);