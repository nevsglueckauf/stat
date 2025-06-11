from textfoo import Texitfy
import statistics

def clc_med(mylist:list):
    """ Median „zu Fuß“ berechnen """
    mylist.sort()
    mid = len(mylist) // 2
    if len(mylist) % 2 == 0:
        return sum(mylist[mid-1:mid+1]) / 2
    else:
        return mylist[mid]

print(Texitfy.quote_typo('zu Fuß'))

bills = [29.99, 29.99, 32.47, 29.99, 47.63, 31.12]
print(clc_med(bills))



# Calculate middle values
print(statistics.median(bills))
exit()


bills.append(29.99)
print(clc_med(bills))

# print(sum([29.99, 31.12])/2)
# exit()
# avg = sum(bills)/len(bills)

# print(avg)

# bills.sort()

# print(bills)

mid = len(bills) // 2
sum1 = bills[mid-1] + bills[mid]
print(sum1)
print(bills[2:3])
sum2 = sum(bills[2:4])

print(sum2)





