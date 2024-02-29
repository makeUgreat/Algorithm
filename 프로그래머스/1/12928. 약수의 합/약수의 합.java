import java.util.stream.*;

class Solution {
    public int solution(int n) {
        return IntStream.rangeClosed(1,n)
            .filter(x -> n%x ==0).sum();
    }
}