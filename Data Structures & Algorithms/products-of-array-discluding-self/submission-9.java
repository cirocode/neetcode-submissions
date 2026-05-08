class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] productLeft = new int[nums.length];
        int[] productRight = new int[nums.length];

        Arrays.fill(productLeft, 1);
        Arrays.fill(productRight, 1);

        int product = 1;

        for (int i = 0; i < nums.length; i++) {
            System.out.println(productLeft[i]);
            productLeft[i] *= product;

            product *= nums[i];
        }

        product = 1;

        for (int i = nums.length - 1; i > -1; i--) {
            productRight[i] *= product;

            product *= nums[i];
        }

        for (int i = 0; i < nums.length; i++) {
            productRight[i] = productRight[i] * productLeft[i];
        }

        return productRight;
    }
}  
