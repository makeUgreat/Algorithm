def solution(s):
    String = list(s)
    stack = []
    
    for ch in String:
        if not stack:
            stack.append(ch)
        else:
            if ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

    if stack:
        return 0
    else:
        return 1