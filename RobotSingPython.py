while True:
    s = str(input("Введите строку для робота: "))
    s = s.lower()
    s = s.replace(' ','')    
    word = 'аоуэяюиыеё'
    l = list(s)
    score = 0
    
    if s=='end':
        break

    if l[0] not in word and l[1] not in word:
        l.pop(0)
        l.insert(0,'а')
        score += 1
    if l[0] in word and l[1] in word:
        l.pop(0)
        l.insert(0,'б')
        score += 1
    
    
    for j in range(1, len(l)):
        if l[j] not in word and l[j - 1] not in word:
            l.pop(j)
            l.insert(j,'а')
            score += 1
        if l[j] in word and l[j - 1] in word:
            l.pop(j)
            l.insert(j,'б')
            score += 1
    
    print("Вывод: " + str(score))