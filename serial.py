class SerialGenerator:
    """
    A class used to generate sequential serial numbers.
    """
    def __init__(self, start=0):
        """
        Initializes the SerialGenerator object with a starting number.
        """
        self.start = start
        self.next = start

    def generate(self):
        """
        Returns the next sequential serial number.
        """
        result = self.next
        self.next += 1
        return result

    def reset(self):
        """
        Resets the serial number back to the original starting number.
        """
        self.next = self.start



