import random

class Roulette:
    def __init__(self):
        self.numbers = list(range(37))
        self.colors = {0: 'Green', **{n: 'Red' if n % 2 else 'Black' for n in range(1, 37)}}
    
    def spin(self):
        result = random.choice(self.numbers)
        return result, self.colors[result]

class Player:
    def __init__(self, balance):
        self.balance = balance
    
    def bet(self, amount, bet_type, value):
        if amount > self.balance:
            return "Insufficient funds!"
        
        self.balance -= amount
        
        number, color = Roulette().spin()
        
        if bet_type == 'number' and value == number:
            self.balance += amount * 36
            return f'You won! The result is {number} {color}. Balance: {self.balance}'
        elif bet_type == 'color' and value.lower() == color.lower():
            self.balance += amount * 2
            return f'You won! The result is {number} {color}. Balance: {self.balance}'
        else:
            return f'You lost! The result is {number} {color}. Balance: {self.balance}'

cash = int(input('Enter your balance: '))
player = Player(cash)
print(player.bet(int(input('Enter your bet: ')), 'color', input('Choose the color black or red: ')))
print(player.bet(int(input('Enter your bet: ')), 'number', int(input('Choose the number from 0 to 36: '))))