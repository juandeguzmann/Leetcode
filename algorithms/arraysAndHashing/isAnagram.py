def isAnagram(s, t):
    sLetterDict = {}
    charIndex = 0

    while charIndex < len(s):
        char = s[charIndex]
        if char in sLetterDict:
            sLetterDict[char] += 1
        else:
            sLetterDict[char] = 1
        charIndex += 1

    tLetterDict = {}
    charIndex = 0

    while charIndex < len(t):
        char = t[charIndex]
        if char in tLetterDict:
            tLetterDict[char] += 1
        else:
            tLetterDict[char] = 1
        charIndex += 1
    
    if sLetterDict == tLetterDict:
        return True
    else:
        return False
    
s="jar"
t="jam"


print(isAnagram(s, t))