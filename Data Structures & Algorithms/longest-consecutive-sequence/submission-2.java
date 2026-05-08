class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numbers = new HashSet<>();

        for (int number : nums) {
            numbers.add(number);
        }

        int longest = 0;
        for (int num : numbers) {
            if (!numbers.contains(num - 1)) {
                int currLongest = 1;
                int currNumber = num;

                while (numbers.contains(currNumber + 1)) {
                    currLongest++;
                    currNumber = currNumber + 1;
                }

                longest = Math.max(longest, currLongest);
            }
        }

        return longest;
    }
}
