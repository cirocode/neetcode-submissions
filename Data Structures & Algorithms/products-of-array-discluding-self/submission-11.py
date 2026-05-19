class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightSideProduct = [1] * len(nums)
        leftSideProduct = [1] * len(nums)
        output = [1] * len(nums)
        currentProduct = 1
        
        for index in range(len(nums)):
            rightSideProduct[index] *= currentProduct

            currentProduct *= nums[index]
        currentProduct = 1
        
        for index in range(len(nums)-1, -1, -1):
            leftSideProduct[index] *= currentProduct
            output[index] = leftSideProduct[index] * rightSideProduct[index]
            currentProduct *= nums[index]
        return output