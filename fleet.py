from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = self.create_fleet()

    def create_fleet(self):
        temp_list = []
        i = 0
        while i < 3:
            temp_list.append(Robot(f'Robot {i}'))
            i = i + 1
        return temp_list
