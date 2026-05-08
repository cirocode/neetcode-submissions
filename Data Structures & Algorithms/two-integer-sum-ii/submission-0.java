class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        int sum = 0;
        for (int i=0; i < numbers.length; i++) {
            sum = numbers[left] + numbers[right];

            if (sum > target) {
                right--;
                sum = numbers[left] + numbers[right];
            }

            if (sum < target) {
                left++;
                sum = numbers[left] + numbers[right];
            }

            if (sum == target) {
                return new int[] {left + 1, right + 1};
            }
        }

        return new int[] {};
    }
}
