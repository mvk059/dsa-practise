from src.test_helper import test_function


# @param arrive : list of integers
# @param depart : list of integers
# @param K : integer
# @return a boolean
# TC: O(NLogN), N: length of arrive/depart
# SC: O(N), N: length of arrive/depart
def hotel(arrive, depart, K):
    rooms = [(a, 1) for a in arrive] + [(d, 2) for d in depart]
    rooms.sort()
    current_rooms = 0

    for room in rooms:
        if room[1] == 1:
            current_rooms += 1
        else:
            current_rooms -= 1
        if current_rooms > K:
            return 0

    return 1


def main():
    # Last value is the expected output
    test_cases = [
        ([1, 2, 3], [10, 3, 5], 1, 0),  # More guests than capacity
        ([1, 2, 3], [4, 5, 6], 2, 0),  # Fits within capacity
        ([1, 2, 3, 4], [5, 6, 7, 8], 3, 0),  # Over capacity
        ([1], [2], 1, 1),  # Single guest
        ([1, 2], [3, 4], 2, 1),  # Two guests, fits capacity
    ]
    test_function(hotel, test_cases)


if __name__ == '__main__':
    main()
