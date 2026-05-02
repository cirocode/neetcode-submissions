class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # With Division
        
        # total_product = 1
        # response = [0] * len(nums)
        # contains_zero = 0
        # zero_boolean = False

        # for digit in nums:
        #     if digit == 0:
        #         contains_zero += 1
        #         zero_boolean = True
        #     else:
        #         total_product *= digit
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         response[i] = total_product
        #         if contains_zero > 1:
        #             response[i] = 0
        #     else:
        #         response[i] = total_product // nums[i]

        #         if zero_boolean:
        #             response[i] = 0

        # return response

        # Without Division

        response = [0] * len(nums)

        prefix = [1] * len(nums)

        prefix_product = 1
        for i in range(len(nums)):
            prefix[i] = prefix_product

            prefix_product *= nums[i]

        postfix = [1] * len(nums)
        postfix_product = 1

        for i in range(len(nums)-1, -1, -1):
            postfix[i] = postfix_product

            postfix_product *= nums[i]

        for i in range(len(postfix)):
            response[i] = postfix[i] * prefix[i]

        return response



