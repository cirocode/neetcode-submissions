class Solution {
    public boolean hasDuplicate(int[] nums) {
        Integer n = nums.length;

        HashSet<Integer> seen = new HashSet<Integer>();

        for (int i = 0; i < n; i++){
            if (seen.contains(nums[i])){
                return true;
            } else {
                seen.add(nums[i]);  
            }
        };

        return false;

    }
}