class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats=list(sorted(seats))
        students=list(sorted(students))
        i,j=0,0
        sum_result=0
        while j <len(seats):
            sum_result+=abs(students[j]-seats[i])
            j+=1
            i+=1
        return sum_result
 