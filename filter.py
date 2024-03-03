nums = [1,2,3,4,5,6,7,8,9];

# def filterFunction(num):
#     return num%2 ==0;

nums = list(filter(lambda num:num%2==0, nums));
print(nums);

#-------------------------------------------------------------------

# nums = [num for num in nums if num%2==0];
# print(nums);