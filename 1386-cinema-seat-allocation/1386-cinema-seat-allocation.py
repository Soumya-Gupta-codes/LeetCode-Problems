class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for r, seat in reservedSeats:
            if r not in rows:
                rows[r] = set()
            rows[r].add(seat)

        answer = (n - len(rows)) * 2

        for seats in rows.values():
            left = all(i not in seats for i in [2, 3, 4, 5])
            middle = all(i not in seats for i in [4, 5, 6, 7])
            right = all(i not in seats for i in [6, 7, 8, 9])

            if left and right:
                answer += 2
            elif left or middle or right:
                answer += 1

        return answer