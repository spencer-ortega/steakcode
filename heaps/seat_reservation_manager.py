"""Seat Reservation Manager Module

This module provides a SeatManager class for managing seat reservations.
"""

import heapq

class SeatManager:
    """This class manages seat reservations."""

    def __init__(self, n: int):
        """Initialize the SeatManager with 'n' seats."""
        self.seats = list(range(1, n + 1))
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        """Reserve and return the smallest available seat."""
        return heapq.heappop(self.seats)

    def unreserve(self, seat_number: int) -> None:
        """Unreserve a previously reserved seat and make it available."""
        heapq.heappush(self.seats, seat_number)
