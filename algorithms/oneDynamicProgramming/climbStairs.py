
def climbStairs(n):
    one, two = 1, 1

    for i in range(n - 1):
        print(one, two)
        temp = one
        one = one + two
        two = temp
        
    return one

climbStairs(5)