def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    arr2 = ["ye", "woo", "ma", "aya"]
    for bab in babbling:
        for a in arr:
            if bab.startswith(a):
                bab = bab[len(a):]
            elif bab.endswith(a):
                bab = bab[:-len(a)]
        if bab == "":
            answer += 1
        else:
            for a in arr2:
                if bab.startswith(a):
                    bab = bab[len(a):]
                elif bab.endswith(a):
                    bab = bab[:-len(a)]
            if bab == "":
                answer += 1        
        
        
    return answer