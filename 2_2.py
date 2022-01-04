def generous_new(total_lambs):

    paid_so_far = 0
    n = 0
    next_pay = 0
    while total_lambs >= paid_so_far:
        n += 1
        next_pay = 2**(n-1)
        paid_so_far = paid_so_far+next_pay

    return n-1
#     biggest_pay = 2**(n-2)
#     #print("Biggest pay: {}".format(biggest_pay))

#     difference = total_lambs - paid_so_far + next_pay
#     #print("Difference: {}".format(difference))
#     second_biggest_pay = biggest_pay/2
#     #print("Second pay: {}".format(second_biggest_pay))


#     stingy_price_of_extra_worker = biggest_pay + second_biggest_pay

#     if stingy_price_of_extra_worker > difference:
#         return n - 1
#     else:
    #     return n

def generous(total_lambs):
    #num_henchmen = math.frexp(total_lambs + 1)[1] - 1 # inverted sum of geometric series with r=2
    num_henchmen = (total_lambs + 1).bit_length() -1
    return num_henchmen
    # # All bellow logic is to check for the possibility of adding another henchmen
    # paid_so_far = (1-2**num_henchmen)/(-1) # total_lambs of geometric series with r = 2
    # difference = total_lambs - paid_so_far
    # biggest_pay = 2**(num_henchmen-1) # value of nth geometric series number
    # second_biggest_pay = biggest_pay/2
    # stingy_price_of_extra_worker = biggest_pay + second_biggest_pay

    # if stingy_price_of_extra_worker > difference:
    #     return num_henchmen
    # else:
    #     return num_henchmen+1


def stingy(total_lambs):
    total_paid = 0
    n = 0
    while total_lambs >= total_paid:
        n += 1
        total_paid = fiborecur(n+2) - 1 # sum Fibonacci(n) = Fibonacci(n+2)-1
    return n-1

def fiborecur(n):
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[i-2]+fibs[i-1])
    return fibs[-1]


def solution(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)

#1,1,2
#1,2,3
new_g = [generous_new(i) for i in range(1000)]
old_g = [generous(i) for i in range(1000)]

for i in range(len(new_g)):
    if new_g[i] != old_g[i]:
        print(i)

# print(generous_new(2))
#print(generous(2))
# import matplotlib.pyplot as plt

# plt.bar(range(10*9, diff))
# plt.show()