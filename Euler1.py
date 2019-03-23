#sum all integers from 1-1000 that are divisible by 3 or 5

i = 0
sum = 0
while i < 1001:
    i+=1
    if i%3==0 or i%5==0:
        sum+=i
print(sum)
