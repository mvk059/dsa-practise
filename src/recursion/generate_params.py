class Solution:

    @staticmethod
    def generate_parenthesis(n):

        def generate(open_count: int, close_count: int, n: int, current: str, ans: list):
            if open_count == close_count == n:
                ans.append(current)
                return

            if open_count < n:
                generate(open_count + 1, close_count, n, current + '(', ans)
            if close_count < open_count:
                generate(open_count, close_count + 1, n, current + ')', ans)

        ans = []
        generate(0, 0, n, "", ans)
        return ans


sol = Solution()
result = sol.generate_parenthesis(2)
print(result)
