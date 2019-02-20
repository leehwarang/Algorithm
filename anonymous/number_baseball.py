#같은 자리에 있는지 -> 스트라이크
#다른 자리에 있지만 있기는 한지 -> 볼
#아예 없는지 -> 포볼 또는 낫싱
import random

def choice():
    game_player = ''
    for _ in range(3):
        game_player += str(random.randint(1,9))
    print("game_player : " + game_player)
    return game_player

def show_result(strike, ball, nothing):
    print("{}스트라이크, {}볼, {}낫싱".format(strike, ball, nothing))

def compare(computer, user):
    strike, ball, nothing = 0, 0, 0

    for i in range(len(user)):
        print(i, user[i])
        if user[i] in computer and i == computer.find(user[i]):
            computer = computer.replace(computer[i], '0', 1)
            strike += 1
        elif user[i] in computer:
            ball += 1
        else:
            nothing += 1
    
    show_result(strike, ball, nothing)
    
    
computer_number = choice()
user_number = input("숫자를 입력해주세요. : ")
compare(computer_number, user_number)










