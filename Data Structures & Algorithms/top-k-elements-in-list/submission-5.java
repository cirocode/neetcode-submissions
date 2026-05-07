class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if (nums.length == k) {
            return nums;
        }
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freq = new List[nums.length];

        for (int i = 0; i < nums.length; i++) {
            count.put(nums[i], count.getOrDefault(nums[i], 0) +1);

            freq[i] = new ArrayList<>();
        }

        for (Integer keySet : count.keySet()) {
            freq[count.get(keySet) - 1].add(keySet);
        }

        int index = 0;
        int[] solution = new int[k];

        for (int i = freq.length - 1; i > -1; i--) {
            for (int val : freq[i]) {
                solution[index] = val;
                index++;

                if (index == k) {
                    return solution;
                }
            }
        }
        return solution;

    }
        




}

