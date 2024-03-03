# file = open('./text.txt');
# # for line in file:
# #     print(line);
# # file.seek(0);
# # lineList = file.readlines();
# # print(lineList);
# file.seek(40);
# readFile = file.read(50);
# print(readFile);
# file.close();

with open('./text.txt') as file:
    for line in file:
        print(line);