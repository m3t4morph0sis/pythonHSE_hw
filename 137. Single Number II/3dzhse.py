class Solution:
    def singleNumber(self, nums):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num in count:
            if count[num] == 1:
                return num
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 2, 3, 2]
    result = solution.singleNumber(nums)
    print("исходный список:", nums)
    print("одиночное число:", result)
