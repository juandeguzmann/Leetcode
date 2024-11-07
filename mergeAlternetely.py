def mergeAlternately(word1, word2):
    results = []
    i = 0

    while i < len(word1) or i < len(word2):
        if i < len(word1):
            results.append(word1[i])
        if i < len(word2):
            results.append(word2[i])
        i += 1
    
    print(''.join(results))


word1 = "ab"
word2 = "pqrs"
mergeAlternately(word1, word2)