class Restaurant:
    menus = {
        'pizza': 12000,
        'cola': 900,
        'apple': 500,
        'juice': 800
    }

    def __init__(self):
        self.orderList = [];
        self.totalPrice = 0;

    def addOrder(self, order):
        self.orderList.append(order);
        self.totalPrice += self.menus[order];

    def printBill(self):
        for order in self.orderList:
            print(f'{order} -  {self.menus[order]} Kyats');
        print(f'total - {self.totalPrice} Kyats');

def startProgram():
    restaurant = Restaurant();

    while True:
        order = input('Order: ');
        restaurant.addOrder(order);
        another = input('Order again? [y/n]');
        if another != 'y' and another != 'n':
            another = input("type only y or n y for yes and n for no");
        if another == 'y':
            continue;
        if another == 'n':
            restaurant.printBill();
            break;

startProgram();