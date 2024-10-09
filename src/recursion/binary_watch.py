from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        # Loop through all possible combinations of hours and minutes and count the number of set bits
        for h in range(12):
            for m in range(60):
                # Check if the number of set bits in hours and minutes equals the target number
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    result.append(f"{h}:{m:02d}")
        return result


def main():
    sol = Solution()
    result = sol.readBinaryWatch(1)
    print(result)
    print("\n")
    result = sol.readBinaryWatch(2)
    print(result)


if __name__ == "__main__":
    main()

