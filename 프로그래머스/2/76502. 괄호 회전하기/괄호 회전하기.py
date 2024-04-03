def is_valid_brackets(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in bracket_map.values():  # 여는 괄호일 경우
            stack.append(char)
        elif char in bracket_map.keys():  # 닫는 괄호일 경우
            if stack == [] or bracket_map[char] != stack.pop():  # 스택이 비었거나 쌍이 맞지 않는 경우
                return False
    return stack == []  # 스택이 비어있어야 모든 괄호가 정확히 맞는 것

def solution(s):
    valid_count = 0
    for i in range(len(s)):
        if is_valid_brackets(s[i:] + s[:i]):  # 문자열을 회전시킨 결과가 올바른 괄호 문자열인지 판별
            valid_count += 1
    return valid_count