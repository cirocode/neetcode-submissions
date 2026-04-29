class Solution {
    public boolean hasDuplicate(int[] nums) {
        Integer n = nums.length;

        HashSet<Integer> seen = new HashSet<Integer>();

        for (int i = 0; i < n; i++){
            seen.add(nums[i]);    
        };

        if (seen.size() == (nums.length)){
            return false;
        } else {
            return true;
        }
    }
}