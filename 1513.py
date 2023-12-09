'''
Medium
This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. 
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
'''
# O(n*k) basic approach with multiple hits. For a medium, I would implement this and discuss getting O(n+k) using KMP...
def search1(pat, str):
    ret = []

    for i in range(len(str)-len(pat)+1):
        for j in range(len(pat)):
            if str[i+j] != pat[j]:
                break  
            if j == len(pat)-1:
                ret.append(i)

    return ret

# knuth-morris-pratt with multiple hits
def search(pat, str):
    i = 0
    j = 0
    pref = prefix(pat)
    ret = []

    while i < len(str):
        if str[i] != pat[j]:
            j = pref[j]
            if j < 0:
                i+=1
                j+=1
        else:
            i+=1
            j+=1
            if j==len(pat):
                ret.append(i-j)
                j = pref[j]
    return ret

def prefix(pat):
    pref = [-1] * len(pat)
    j = 0

    for i in range(1,len(pat)):
        if pat[i] == pat[j]:
            pref[i] = pref[j]
            j+=1
        else:
            pref[i] = j
            while j >= 0 and pat[i] != pat[j]:
                j = pref[j]
            j+=1
    pref.append(j)
    return pref
        

str = "bbabacadabacab"
pat = "abaca"

# print(prefix(pat))
print(search(pat, str))