from robot import Robot


class Fleet:

    def __init__(self):
        self.robot_fleet = []
        self.create_fleet()

    def add_robot_into_fleet(self, robot):
        self.robot_fleet.append(robot)

    def dispaly_robots_fleet(self):
        for robot in self.robot_fleet:
            print(f'Robot: {robot.name} Health: {robot.health}')


    def create_fleet(self):
        self.add_robot_into_fleet(Robot("rb1"))
        self.add_robot_into_fleet(Robot("rb2"))
        self.add_robot_into_fleet(Robot("rb3"))