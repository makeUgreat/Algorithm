function solution(num_list, n) {
    for (let e of num_list) {
        if (e === n) {
            return 1;
        }
    }
    return 0;
}