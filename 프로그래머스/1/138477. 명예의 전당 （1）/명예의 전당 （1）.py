def solution(k, score):
    # score를 for로 순회한다
    # 매번 얻은 점수를 누적 배열에 저장하고 내림차순으로 정렬
    accum = []
    answer = []

    for s in score:
        accum.append(s)
        accum.sort(reverse=True)
        
        if len(accum) < k:
            answer.append(accum[-1])
        else:
            answer.append(accum[k-1])
    return answer