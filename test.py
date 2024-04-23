import unittest
from Elevator import Elevator

class TestElevator(unittest.TestCase):

    def test_go_up(self):
        elevator = Elevator(10)
        elevator.current_floor = 3
        elevator.go_up()
        self.assertEqual(elevator.current_floor, 4)

if __name__ == '__main__':
    unittest.main()
