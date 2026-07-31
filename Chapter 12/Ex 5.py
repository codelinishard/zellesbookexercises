# midway through, I realised there was nothing in the questions
# that said it had to be a graphical programme, so I changed track
# to save on the hassle of aligning everything graphically

from dice import Dice
from graphics import *
from random import randint


class crapsDice(Dice):
    def __init__(self,diceCount:int):
        self.diceCount = diceCount
        self.dice = [1] * diceCount
        
    def roll_all(self):
        self.roll(range(self.diceCount))

    def values(self):
        return self.dice
    
    def sum_all(self):
        sum = 0
        for value in self.dice:
            sum += value
        return sum
    
    def Run_Stage_1(self):
        """This is for the come out roll"""
        sum = self.sum_all()
        for value in self.dice:
            sum += value
        if sum == 7 or sum == 11:
            return False, 0
        elif sum == 2 or sum == 3 or sum == 12:
            return False, 0
        else:
            return True, sum
    def Run_stage_2(self, point):
        """This handles all stage 2 rolling"""
        sum = self.sum_all()
        if sum == 7:
            return False, 0
        elif sum == point:
            return False, sum
        else:
            return True, 0
    
class craps:

    def __init__(self, interface):
        self.money = 100
        self.cpumoney = 100
        self.interface = interface
        self.dice = crapsDice(2)
        self.is_shooter = self.determine_shooter() # Boolean

    def determine_shooter(self):
        self.interface.start_choosing_shooter()
        CPU_sum = 0
        your_sum = 0
        while CPU_sum == your_sum:
            self.interface.determining_shooter("CPU")
            self.dice.roll_all()
            dice_rolls = self.dice.values()
            CPU_sum = self.dice.sum_all()
            self.interface.show_roll_outcome(dice_rolls, CPU_sum)
            self.interface.determining_shooter("You")
            self.dice.roll_all()
            dice_rolls = self.dice.values()
            your_sum = self.dice.sum_all()
            self.interface.show_roll_outcome(dice_rolls, your_sum)
            if CPU_sum == your_sum:
                self.interface.determine_shooter_tie()

        if CPU_sum > your_sum:
            self.interface.shooter_picked("CPU")
            return False
        else:
            self.interface.shooter_picked("You")
            return True

    def run(self):
        
        while self.money > 0 and self.cpumoney> 0 and self.interface.wantToPlay():
            self.playRound()            
        if self.money == 0:
            self.interface.cpu_win()
        elif self.cpumoney == 0:
            self.interface.you_win()
        self.interface.close()

    def playRound(self):
        if self.is_shooter:
            bet = self.interface.get_bet()
        else:
            if self.cpumoney > self.money:
                bet = randint(1,self.money)
            else:
                bet = randint(1,self.cpumoney)
            self.interface.CPU_bets(bet)
        while bet > self.money or bet > self.cpumoney:
            self.interface.no_funds()
            bet = self.interface.get_bet()
        self.money = self.money - bet
        self.cpumoney = self.cpumoney - bet
        self.interface.setMoney(self.cpumoney,self.money)
        
        # come-out roll
        self.dice.roll_all()
        dice_rolls = self.dice.values()
        come_sum = self.dice.sum_all()
        self.interface.show_roll_outcome(dice_rolls, come_sum)
        continue_game, point = self.dice.Run_Stage_1()
        if continue_game == False:
            if self.is_shooter:
                if point in [2,3,12]:
                    self.interface.lose_stage1("You", point)
                    self.update_money("CPU", bet)
                else:
                    self.interface.win_stage1("You", point)
                    self.update_money("You", bet)
            else: #CPU
                if point in [2,3,12]:
                    self.interface.lose_stage1("CPU", point)
                    self.update_money("You", bet)
                else:
                    self.interface.win_stage1("CPU", point)
                    self.update_money("CPU", bet)
                
        elif continue_game:
            self.interface.continuing_game()
            # repeat rolls until point or 7
            self.dice.roll_all()
            dice_rolls = self.dice.values()
            roll_sum = self.dice.sum_all()
            self.interface.show_roll_outcome(dice_rolls, roll_sum)
            continue_game, score = self.dice.Run_stage_2(point)
            while continue_game:
                self.dice.roll_all()
                dice_rolls = self.dice.values()
                roll_sum = self.dice.sum_all()
                self.interface.show_roll_outcome(dice_rolls, roll_sum)
                continue_game, score = self.dice.Run_stage_2(point)
            else:
                if score == point:
                    if self.is_shooter:
                        self.interface.win_stage2("You", point)
                        self.update_money("You", bet)
                    else:
                        self.interface.win_stage2("CPU",point)
                        self.update_money("CPU", bet)
                else:
                    if self.is_shooter:
                        self.interface.lose_stage2("You", point)
                        self.is_shooter = False
                        self.update_money("CPU", bet)
                    else:
                        self.interface.lose_stage2("CPU", point)
                        self.is_shooter = True
                        self.update_money("You", bet)
    def update_money(self,winner,bet):
        if winner == "CPU":
            self.cpumoney += bet *2
        elif winner == "You":
            self.money += bet *2
        self.interface.setMoney(self.cpumoney,self.money)

class TextInterface:

    def __init__(self):
        print("Welcome to craps.")
        print("The game has two stages. After betting, 2 die are rolled.")
        print("If 7 or 11 is rolled, the person who rolled, the shooter, wins the bet.")
        print("If 2,3, or 12 is rolled, the shooter loses the bet, and the next round starts.")
        print("If none of the above was rolled, the round enters stage 2.")
        print("The shooter will have to roll what they just rolled again to win.")
        print("However, if they roll a 7 before that, they lose, and the other person becomes the shooter.")
        print("The game will continue until you or the CPU goes bankrupt, or you want to quit.")
    
    #used throughout
    def show_roll_outcome(self, values, sum):
        print(f"\nThe dice roll values are {values[0]}, {values[1]}. Total score: {sum}.")
    def setMoney(self, cpumoney,money):
        print(f"\nYou currently have ${money}, while CPU has ${cpumoney}.")
    def wantToPlay(self):
        ans = input("Do you wish to try your luck? ")
        return ans[:1] in "yY"

    #before starting
    def start_choosing_shooter(self):
        print("\nThe starting shooter must first be determined. The person who rolls higher starts first.")
        input("Press 'enter' to continue")
    def determining_shooter(self,person):
        print(f"\nRolling dice for {person}.")
    def determine_shooter_tie(self):
        print("\nDue to a tie, let's reroll.")
    def shooter_picked(self,person):
        print(f"\n{person} rolled higher on their dice rolls. ")
        print(f"The shooter will first be {person} then.")
        input("Press 'enter' to continue.")
    
    #betting methods
    def get_bet(self):
        valid_input = 0
        while valid_input <= 0:
            try: valid_input = int(input("How much do you want to bet? ")) 
            except ValueError: print("Only int values are allowed. Try again")
        return valid_input
    def CPU_bets(self,bet):
        print("The CPU will bet $" + str(bet))   
    def no_funds(self):
        print("You can't bet this much. Try a lower bet.")
    
    #stage1 methods
    def win_stage1(self, person:str, point):
        print(f"{person} rolled a {point}. A natural! ")
    def lose_stage1(self, person:str, point):
        print(f"{person} rolled a {point}. An unfortunate loss. ")
    def continuing_game(self):
        print("Since a round ending number was not rolled, we will proceed to stage 2.")

    #stage2 methods
    def win_stage2(self, person:str, point):
        print(f"Rolling {point} again, {person} wins this round.")
    def lose_stage2(self, person:str, point):
        print(f"Rolling a 7 before {point}, {person} unfortunately lost this round.")
        print("The shooter will be changing next round.")

    #methods when exiting
    def you_win(self):
        print("The CPU ran out of money. You win!")
        input("Press 'Enter' to exit. ")
    def cpu_win(self):
        print("You ran out of money. You lose.")
        input("Press 'Enter' to exit. ")
    def close(self):
        print("\nThanks for playing!")
        input("Press 'Enter' to exit. ")

inter = TextInterface()
app = craps(inter)
app.run()

