#!/usr/bin/env checkio --domain=py run end-zeros

# Try to find out how many zeros a given number has at the end.
# 
# Input:A positive Int
# 
# Output:An Int.
# 
# 
# END_DESC

#

#

#
#



def end_zeros2(num: int) -> int:
    # your code here
    # str_num = str(num)
    # n = 0
    # if num == 0:
    #     return 1
    # while num % 10 == 0:
    #     n = n + 1
    #     num = num / 10
    
    n = 0
    for x in reversed(str(num)):
        if x == '0': n += 1
        else: return n
    
    
    return n
    
def end_zeros(num: int) -> int:
    # your code here
    key = str(num)
    x=key[::-1]
    ans=0
    for n in range(len(x)):
        if x[n]=='0':
            ans+=1
        else:
            return ans

if __name__ == "__main__":
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")