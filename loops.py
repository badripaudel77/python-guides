# for, while, do while
# 0 to 10, step 2
for i in range(0,10,2):
    print(str(i) + "th =" + str(i))
i = 1
sum = 0
while i<= 10:
    sum += i
    i = i+1
print("Sum of 1 to 10 is : " + str(sum)) 

for i in range(11):
    if(i%2==0):
        print(i)
        break
print("broke out")

for j in range(8): 
    if(j % 2 == 0):
        continue
    print(j)
