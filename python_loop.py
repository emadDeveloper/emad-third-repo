list1 = []

num = int(input("how many values you want to keep in your list: "))

for i in range(num):
    x = int(input("give your list value: "))
    list1.append(x)

print(list1)

sum = 1
for i in list1:
    sum = sum*i
print(sum)

if(sum%2==0):
    print("the value is even")

else:
    print("the value is odd")    

