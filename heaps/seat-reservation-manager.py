# 1845. Seat Reservation Manager

import heapq
class SeatManager:
    def __init__(self, n: int):
        self.seats = list(range(1, n+1))
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)