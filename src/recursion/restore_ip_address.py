from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        result = []

        def recurse(i, dots, current):
            if dots == 4 and i == len(s):
                result.append(current[:-1])
                return

            if dots > 4:
                return

            for j in range(1, 4):
                if i + j > len(s):
                    break
                char = s[i:i+j]
                if (char.startswith("0") and len(char) > 1) or (j == 3 and int(char) >= 256):
                    continue
                recurse(i + j, dots + 1, current + char + ".")

        recurse(0, 0, "")
        return result


def main():
    sol = Solution()
    # result = sol.restoreIpAddresses("25525511135")
    result = sol.restoreIpAddresses("101023")
    print(result)


if __name__ == "__main__":
    main()
