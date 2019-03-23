#sum all integers from 1-1000 that are divisible by 3 or 5

sum([x for x in range(1000) if ((x % 5 == 0) or (x % 3 == 0))])
