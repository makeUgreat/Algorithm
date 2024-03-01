import java.util.stream.*;
import java.util.*;

class Solution {
    public List<Long> solution(int x, int n) {
        return Stream.iterate((long)x, i -> i+x )
            .limit(n)
            .collect(Collectors.toList());
    }
}