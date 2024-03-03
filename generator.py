from random import randint; 
lists = ['apple', 'orange', 'lemon', 'lime'];

def woldAddFuncrion(world):
    randWorld = world + lists[randint(0, len(lists) - 1)];
    return randWorld;
    

    

with open('./text.txt') as file:
    paragraph = file.read();
    worlds = paragraph.split();
    mapWorld = list(map(woldAddFuncrion, worlds));

paraCount = int(input('Paragraph count: '));
for count in range(paraCount):
    with open('./generator.txt', 'a') as write_file:
        write_file.write(' '.join(mapWorld) + '\n\n'); 
