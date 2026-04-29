class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer,Integer> seen = new HashMap<Integer,Integer>();
        int[] response = new int[2];



        for (int i = 0; i < nums.length; i++) {
            if (seen.containsKey(target - nums[i])) {
                
                response[0] = seen.get(target-nums[i]);
                response[1] = (i);
                return response;
            } else {
                seen.put(nums[i], i);
            }
        }
        return response;

    }
    
}
