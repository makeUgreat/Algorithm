import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(long n) {
        String str = Long.toString(n);
        
        int[] reversed = new StringBuilder(str).reverse().chars()
            .mapToObj(c -> Character.digit(c,10))
            .mapToInt(Integer::intValue)
            .toArray();
        
        return reversed;
    }
}