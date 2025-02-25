### Native
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        taken_places = [i for i in range(len(seats)) if seats[i] == 1]
        taken_places_length = len(taken_places)

        if taken_places_length == 1:
            return len(seats) - 1

        max_distance = -1
        for i in range(taken_places_length - 1):
            seat_left = taken_places[i]
            seat_right = taken_places[i + 1]

            max_distance = max(max_distance, (seat_right - seat_left) // 2)
        
        return max_distance
    
### Fairly Optimal bruh
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first_one = 0
        max_distance = 0
        while first_one < len(seats):
            if seats[first_one]:
                break
            else:
                first_one += 1
                max_distance += 1

        current_distance = 0

        for i in range(first_one, len(seats)):
            if seats[i]:
                max_distance = max(max_distance, (current_distance + 1) // 2)
                current_distance = 0
            
            else:
                current_distance += 1
        max_distance = max(max_distance, current_distance)

        return max_distance

### Optimal and readable
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        last_occupied_seat_index = -1
        current_empty_seats = 0

        for i in range(len(seats)):
            if seats[i] == 1:
                if last_occupied_seat_index == -1:
                    max_distance = max(max_distance, i)
                else:
                    distance_between_seats = i - last_occupied_seat_index
                    max_distance = max(max_distance, distance_between_seats // 2)
                last_occupied_seat_index = i
                current_empty_seats = 0
            else:
                current_empty_seats += 1
                
        max_distance = max(max_distance, current_empty_seats)

        return max_distance

