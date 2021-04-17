from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet().robots
        self.herd = Herd().dinosaurs

    def run_game(self):
        run = input("Would you like to run the game? ")
        run = run.lower()
        if run == 'yes':
            self.display_welcome()
            self.battle()
        elif run == 'no':
            print("come back another time!")
        else:
            run = input("please enter yes or no only: ")

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
            choice = int(input('Enter #:'))
            if choice == 0:
                print('Please select from the following:')
                self.show_robo_options()
                selected_robot = int(input('Enter #'))
                self.robo_turn(selected_robot)
                continue_game = self.continue_game()
            elif choice == 1:
                print('Please select from the following:')
                self.show_dino_options()
                selected_dino = int(input('Enter #'))
                self.dino_turn(selected_dino)
                continue_game = self.continue_game()
            else:
                choice = int(input("Please enter 0 or 1"))
        else:
            self.display_winners()

    def dino_turn(self, dinosaur):
        print('Who would you like to battle?')
        self.show_robo_options()
        selected_robot = int(input('Enter #'))
        if self.fleet[selected_robot].health == 0:
            print(f'{self.fleet[selected_robot].name} has no more health and has been removed from the game')
        else:
            self.herd[dinosaur].attack(self.fleet[selected_robot])
            print(f'{self.herd[dinosaur].type} attacked {self.fleet[selected_robot].name}')

    def robo_turn(self, robot):
        print('Who would you like to battle?')
        self.show_dino_options()
        selected_dino = int(input('Enter #'))
        if self.herd[selected_dino].health == 0:
            print(f'{self.herd[selected_dino].type} has no more health, please select another')
        else:
            self.fleet[robot].attack(self.herd[selected_dino])
            print(f'{self.fleet[robot].name} attacked {self.herd[selected_dino].type}')

    def show_dino_options(self):
        i = 0
        while i < len(self.herd):
            if self.herd[i].health == 0:
                print(f'{i}. {self.herd[i].type} is defeated!')
            else:
                print(f'{i}. {self.herd[i].type} | Health: {self.herd[i].health}%')
            i = i + 1

    def show_robo_options(self):
        i = 0
        while i < len(self.fleet):
            if self.fleet[i].health == 0:
                print(f'{i}. {self.fleet[i].name} is defeated!')
            else:
                print(f'{i}. {self.fleet[i].name} | Health: {self.fleet[i].health}%')
            i = i + 1

    def display_winners(self):
        print('game ended')

    def continue_game(self):
        i = 0
        fleet_health_total = 0
        while i < len(self.fleet):
            fleet_health_total += self.fleet[i].health
            i += 1
        j = 0
        herd_health_total = 0
        while j < len(self.herd):
            herd_health_total += self.herd[j].health
            j += 1

        if fleet_health_total == 0 or herd_health_total == 0:
            return False
        else:
            return True
