import java.util.stream.*;

class Solution {
    public long solution(long n) {
        String sorted = String.valueOf(n)
            .chars().mapToObj(c -> (char)c)
            .sorted((a,b) -> b - a )
            .map(String::valueOf)
            .collect(Collectors.joining());
    
        return Long.parseLong(sorted);
    }
}