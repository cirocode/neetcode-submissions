class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total_product = 1
        response = [0] * len(nums)
        contains_zero = 0
        zero_boolean = False

        for digit in nums:
            if digit == 0:
                contains_zero += 1
                zero_boolean = True
            else:
                total_product *= digit

        print(contains_zero)

        for i in range(len(nums)):
            if nums[i] == 0:
                response[i] = total_product
                if contains_zero > 1:
                    response[i] = 0


                

            else:
                response[i] = total_product // nums[i]

                if zero_boolean:
                    response[i] = 0

        print(response)
                

        return response
