from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet().robots
        self.herd = Herd().dinosaurs

    def run_game(self):
        print("Would you like to run the game?")
        while True:
            run = input("Yes or No?: ")
            run = run.lower()
            if run == 'yes':
                self.display_welcome()
                self.battle()
                break
            if run == 'no':
                print("Come back another time!")
                break
            print("Please enter yes or no only: ")

    def display_welcome(self):
        print('Welcome to Dino Vs Robots! Your challengers are:')
        i = 0
        string_fleet = ''
        while i < len(self.fleet):
            string_fleet += f' {self.fleet[i].name} '
            i = i + 1
        print(string_fleet)
        print('VS')
        j = 0
        string_herd = ''
        while j < len(self.herd):
            string_herd += f' {self.herd[j].type} '
            j = j + 1
        print(string_herd)
        print('______________________________________')

    def battle(self):
        continue_game = True
        while continue_game:
            print('Who would you like to battle as? Enter 0 for Robot and 1 for Dino')
            choice = self.integer_only_input()
            if choice == 0:
                print('Please select from the following:')
                self.show_robo_options()
                selected_robot = self.integer_only_input()
                if self.fleet[selected_robot].health <= 0:
                    print(f'{self.fleet[selected_robot].name} has no more health, please select another')
                else:
                    self.robo_turn(selected_robot)
                continue_game = self.continue_game()
            elif choice == 1:
                print('Please select from the following:')
                self.show_dino_options()
                selected_dino = self.integer_only_input()
                if self.herd[selected_dino].health <= 0:
                    print(f'{self.herd[selected_dino].type} has no more health, please select another')
                else:
                    self.dino_turn(selected_dino)
                continue_game = self.continue_game()
        else:
            self.display_winners()

    def dino_turn(self, dinosaur):
        print('Who would you like to battle?')
        self.show_robo_options()
        selected_robot = self.integer_only_input()
        if self.fleet[selected_robot].health <= 0:
            print(f'{self.fleet[selected_robot].name} has no more health, please select another')
        else:
            self.herd[dinosaur].attack(self.fleet[selected_robot])
            print(f'{self.herd[dinosaur].type} attacked {self.fleet[selected_robot].name}')

    def robo_turn(self, robot):
        print('Who would you like to battle?')
        self.show_dino_options()
        selected_dino = self.integer_only_input()
        if self.herd[selected_dino].health <= 0:
            print(f'{self.herd[selected_dino].type} has no more health, please select another')
        else:
            self.fleet[robot].attack(self.herd[selected_dino])
            print(f'{self.fleet[robot].name} attacked {self.herd[selected_dino].type}')

    def show_dino_options(self):
        i = 0
        while i < len(self.herd):
            if self.herd[i].health <= 0:
                print(f'{i}. {self.herd[i].type} is defeated!')
            else:
                print(f'{i}. {self.herd[i].type} | Health: {self.herd[i].health}%')
            i = i + 1

    def show_robo_options(self):
        i = 0
        while i < len(self.fleet):
            if self.fleet[i].health <= 0:
                print(f'{i}. {self.fleet[i].name} is defeated!')
            else:
                print(f'{i}. {self.fleet[i].name} | Health: {self.fleet[i].health}%')
            i = i + 1

    def display_winners(self):
        print('_______________________________')
        if self.fleet_health_calculator() > self.herd_health_calculator():

            print('Robots Win!')
            self.show_robo_options()
            self.show_dino_options()
        elif self.herd_health_calculator() > self.fleet_health_calculator():
            print('Dinosaurs Win!')
            self.show_dino_options()
            self.show_robo_options()

    def continue_game(self):
        if self.fleet_health_calculator() <= 0 or self.herd_health_calculator() <= 0:
            return False
        else:
            return True

    def fleet_health_calculator(self):
        i = 0
        fleet_health_total = 0
        while i < len(self.fleet):
            fleet_health_total += self.fleet[i].health
            i += 1
        return fleet_health_total

    def herd_health_calculator(self):
        j = 0
        herd_health_total = 0
        while j < len(self.herd):
            herd_health_total += self.herd[j].health
            j += 1
        return herd_health_total

    def integer_only_input(self):
        while True:
            try:
                value = int(input('Enter #'))
                return value
            except:
                print("That's not a valid option")