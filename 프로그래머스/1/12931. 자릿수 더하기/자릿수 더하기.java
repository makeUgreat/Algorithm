import java.util.stream.*;

public class Solution {
    public int solution(int n) {
        int answer = String.valueOf(n)
            .chars().map(c -> c - '0')
            .sum();
        
        

        return answer;
    }
}