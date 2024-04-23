import threading
import time

class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.current_floor = 1
        self.direction = None
        self.is_emergency = False
        self.door_open_timer = None

    def go_up(self):
        if self.current_floor < self.num_floors:
            self.current_floor += 1
            print(f"Elevator going up. Current floor: {self.current_floor}")

    def go_down(self):
        if self.current_floor > 1:
            self.current_floor -= 1
            print(f"Elevator going down. Current floor: {self.current_floor}")

    def emergency_stop(self):
        self.is_emergency = True
        nearest_floor = self.num_floors if self.direction == "up" else 1
        print(f"Emergency stop! Elevator stopped at floor {nearest_floor}. Doors opening.")
        self.start_door_open_timer()

    def reset_emergency(self):
        self.is_emergency = False

    def start_door_open_timer(self):
        if self.door_open_timer is not None:
            self.door_open_timer.cancel()
        self.door_open_timer = threading.Timer(5.0, self.close_doors)
        self.door_open_timer.start()

    def close_doors(self):
        for i in range(5, 0, -1):
            print(f"Doors closing in {i} seconds...")
            time.sleep(1)
        print("Doors closing.")
        self.door_open_timer = None

    def request_floor(self, floor):
        if self.is_emergency:
            return
        if floor > self.current_floor:
            self.direction = "up"
            while self.current_floor < floor:
                self.go_up()
        elif floor < self.current_floor:
            self.direction = "down"
            while self.current_floor > floor:
                self.go_down()
        print(f"Elevator reached floor {self.current_floor}. Doors opening.")
        self.start_door_open_timer()

# Example usage:
elevator = Elevator(10)

while True:
    try:
        choice = input("Enter the floor you want to go to (1-10), or 'E' for emergency stop: ")
        if choice.lower() == 'e':
            elevator.emergency_stop()
            break
        elif choice.strip() == '':
            print("Please enter a floor number or 'E' for emergency stop.")
        else:
            floor = int(choice)
            if floor < 1 or floor > 10:
                raise ValueError("Invalid floor number. Please enter a number between 1 and 10.")
            elevator.request_floor(floor)
    except ValueError as e:
        print(e)
        continue

