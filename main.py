from battlefield import Battlefield

if __name__ == '__main__':
    test_battlefield = Battlefield()

    while test_battlefield.run_game() == True:
          test_battlefield.display_welcome()
          test_battlefield.battle()
    else:
        print("okay nvm")