class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
      seats.sort()
      students.sort()
      i, diff = 0, 0
      while i < len(seats):
        diff += abs(students[i]-seats[i])
        i+=1
      return diff

        