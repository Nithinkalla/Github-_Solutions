class Solution {
    public int climbStairs(int n) {
        int count = 0;
        int first = 0;
        int second = 1;
        int steps = 0;
        while(count < n){
            steps = first + second;
            first = second;
            second = steps;
            count++;
        }
        return steps;
    }
}