### find the greatest palindromic number that is a product of 2 3-digit numbers

num1 = list(range(100,999))
num2 = 100
array = []
while num2 <1000:
    for num in num1:
        product = num * num2
        productstring = str(product)
        reverse = productstring[::-1]
        if productstring == reverse:
            array.append(product)
    num2+=1
print(max(array))
