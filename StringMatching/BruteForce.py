"""Finds if substring is present in string, and if
so the index of the first occurrence.

Input: Array of n characters representing text
        Array of m characters reresenting pattern
Output: Index of first character in the text that starts
        a matching substring, or returns -1
Time Efficiency: O((n-m-1)*m) or O(nm) """

def bruteForceStringMatcher(text,pattern):
    for i in range(len(text)-len(pattern)+1):
        j = 0 
        while j<len(pattern) and pattern[j] == text[i+j]:
            j=j+1
        if j==len(pattern):
            return i
    return -1
    
a = ['a','n','a','p','p','l','e','a','d','a','y','k','e','e','p','s']
b = ['d','a', 'y']
c = ['c','r','a','z','y']

print(bruteForceStringMatcher(a,b))
print(bruteForceStringMatcher(a,c))
    
