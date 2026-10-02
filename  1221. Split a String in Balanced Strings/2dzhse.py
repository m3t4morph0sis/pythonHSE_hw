class Solution:
    def balancedStringSplit(self, s):
        balance = 0
        answer = 0
        for char in s:
            if char == "L":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                answer += 1
        return answer
if __name__ == "__main__":
    solution = Solution()
    test_string = "RLRRLLRLRL"
    result = solution.balancedStringSplit(test_string)
    print("строка:", test_string)
    print("количество сбалансированных строк:", result)