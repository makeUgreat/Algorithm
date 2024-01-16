def solution(STR):
    answer = []
    my_dict = dict()
    str_len = len(STR)
    for i in range(str_len):
        now_char = STR[i]
        # 현재 문자열이 딕셔너리에 있으면 인덱스번호를 가져오고
        # 없으면 0을 반환
        now_dict = my_dict.get(now_char, None)

        if now_dict is not None:
            my_dict[now_char] = i
            answer.append(i - now_dict)
        else:
            my_dict[now_char] = i
            answer.append(-1)



    return answer