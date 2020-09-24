from typing import List


class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        """
        idx = 0
        for n in range(len(nums)):
            print(n)
            if nums[n] != 0:
                nums[idx] = nums[n]
                idx += 1
        for n in range(idx, len(nums)):
            nums[n] = 0

    def moveZerosBest(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        """
        # idx = 0
        # for n in range(len(nums)):
        #     if nums[n] != 0:
        #         nums[idx], nums[n] = nums[n], nums[idx]
        #         idx += 1
        #     print(n, nums)

        idx = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                if nums[idx] == 0:
                    nums[idx], nums[n] = nums[n], nums[idx]
                idx += 1
            print(n, nums)
    
if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    sol = Solution()
    sol.moveZerosBest(nums)
    print(nums)