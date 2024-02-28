import java.util.Arrays;

class Solution {
    public double solution(int[] arr) {
        double answer = Arrays.stream(arr).average().orElse(Double.NaN);
        return answer;
    }
}