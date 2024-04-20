import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] num_list) {
        Arrays.sort(num_list);

        ArrayList<Integer> answer = new ArrayList<>();
        for (int i=5; i < num_list.length ;i++) {
                answer.add(num_list[i]);
        }
        
        return answer;
    }
}