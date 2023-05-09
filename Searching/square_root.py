#FIND THE SQUARE ROOT OF A NUMBER USING BINARY SEARCH
#Time complexity = O (log x) where x is the number we want to square root
#Space complexity = O (1)
def mySqrt(x):
        if x == 0 or x == 1: #best case where x is equal to 0 or 1
            return x
        low = 0
        high = x
        while low <= high: #compare low and high when condition is false, end loop
            mid = (low + high) // 2
            if mid * mid == x: #perfect square
                return mid
            elif mid * mid > x: #if mid squared is greater then we need to reduce our high by 1 because our sqrt will be lower
                high = mid - 1
            else:
                low = mid+1 #if mid squared is lesser then we need to add by 1 and accept our answer as the mid until the condition is false
                ans = mid
        return ans
mySqrt(100)