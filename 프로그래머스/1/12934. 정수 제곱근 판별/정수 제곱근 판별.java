import java.util.*;
class Solution {
    public double solution(long n) {
        double answer = Math.sqrt(n);
        if (answer == (long)answer) {
            return Math.pow(answer+1,2);
        }
        else {
            return -1;
        }
    }
}