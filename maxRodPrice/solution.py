""" Input = List with prices for various lengths of rod, length of rod
    Output = Maximum price for rod of length 
    
    Concept: Uses Dynamic Programming 
    Time efficiency is O(n^2)
    Space efficiency is O(1), i.e. uses constant space """


def maxPrice(price, n):
    
    val = [None]*(n+1)
    val[0] = 0
        
    for i in range (1,n+1):
        maxVal = 0
        for j in range (i):
            maxVal = max(maxVal, price[j] + val[i-j-1])
        val[i] = maxVal

    return val[n]

price = [1, 3, 6, 14, 14, 18, 19, 20] 
length = len(price) 
print("Maximum value for rod of length " + str(length) + " is " + str(maxPrice(price, length))) 

# Time efficiency is O(n^2)
# Space efficiency is O(1), i.e. uses constant space
