#sum all fibonnaci even fibonacci numbers up to 4 million

sum = 0
previous = current = 1

while current < 4000000:
    
    current,previous = current + previous,current
    if current % 2 == 0:
        sum += current
print(sum)
