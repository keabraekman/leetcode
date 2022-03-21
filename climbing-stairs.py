# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


result = []

def climbStairs(result, n):
    # print(n)
    if n < 0:
        return
    elif n == 0:
        result.append(1)
    else:
        climbStairs(result, n-1)
        climbStairs(result, n-2)


def climbStairs(n):
    one, two = 1, 1
    for i in range(n-1):
        three = one + two
        one = two
        two = three
    return three
        


# print(climbStairs(4))




def climbStairs(n):
    one, two = 1, 1
    for i in range(n-1):
        three = one+two
        one = two
        two = three
    return three

print(climbStairs(4))