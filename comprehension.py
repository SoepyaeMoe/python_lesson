# prices = [1000, 3000, 5000, 9000];
# double_price = [];

# for price in prices:
#     double_price.append(price*2);

# double_price = [price*2 for price in prices];
# print(double_price);
nums = [1,2,3,4,5,6,7,8,9,10];
# double_num = [];

# for num in nums:
#     if num%2 == 0:
#         double_num.append(num*2);
# print(double_num);

double_num = [num*2 for num in nums if num%2 == 0];
print(double_num);