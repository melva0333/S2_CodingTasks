'''Write a function/method to loop through a range of numbers, from X to Y
    a) Highlight any that are divisible by 3 as "divisible by 3"
    b) Highlight any that are divisible by 5 as "divisible by 5"
    c) Highlight any that are divisible by both as "divisible by 3 and 5"
'''
def divisible_by_3_or_and_5(x,y):
    for n in range(x, y+1):
        # Need to have the divisible by 3 and 5 conditional first otherwise logic
        # dictates that the first conditional will be used as result
        if n % 3 == 0 and n % 5 == 0:
            print(f"{n} is divisible by 3 and 5")
        elif n % 3 == 0:
            print(f"{n} is divisible by 3")
        elif n % 5 == 0:
            print(f"{n} is divisible by 5")

#Sample test
divisible_by_3_or_and_5(1,15)
divisible_by_3_or_and_5(16,35)
divisible_by_3_or_and_5(36,50)