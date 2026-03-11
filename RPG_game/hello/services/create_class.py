import time
import random
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils.html import mark_safe

class Character:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health
        self.max_health = health

    def __str__(self):
        return f'Имя🙎: {self.name} | Урон🗡 : {self.attack} | Здоровье✳️ : {self.health}.'
    
    def attacked(self, other, ur):
        messages = []
        messages.append(f'<h2>{self.name} атакует 🗡  {other.name}!</h2>')
        other.take_damage(self.attack, ur)
        return messages

    def take_damage(self, damage, ur):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def vosst(self):
        self.health = self.max_health

class Warrior(Character):
    def __init__(self, name, attack, health, buff):
        self.name = name
        self.attack = attack
        self.health = health
        self.max_health = health
        self.buff = buff

    def __str__(self):
        return f'Имя🙎: {self.name} | Урон🗡 : {self.attack} | Здоровье✳️ : {self.health} | Навык🔥: {self.buff}.'
    
    def attacked(self, other, ur):
        messages = [f'<h2>{self.name} атакует 🗡  {other.name}!</h2>']
        other.take_damage(self.attack, ur)
        chance = random.randrange(101)
        if 1 <= ur <= 249 and chance <= 25:
            other.take_damage(self.attack, ur)
            messages.append('<h2>Воин нанес двойной урон!🗡🗡</h2>')
        if 250 <= ur <= 999 and chance <= 30:
            other.take_damage(self.attack, ur)
            messages.append('<h2>Воин нанес двойной урон!🗡🗡</h2>')
        if 1000 <= ur <= 4999 and chance <= 35:
            other.take_damage(self.attack, ur)
            messages.append('<h2>Воин нанес двойной урон!🗡🗡</h2>')
        if 5000 <= ur <= 9999 and chance <= 40:
            other.take_damage(self.attack, ur)
            messages.append('<h2>Воин нанес двойной урон!🗡🗡</h2>')
        if ur >= 10000 and chance <= 45:
            other.take_damage(self.attack, ur)
            messages.append('<h2>Воин нанес двойной урон!🗡🗡</h2>')
        return messages
    
    
class Palladin(Warrior):
    def attacked(self, other, ur):
        messages = [f'<h2>{self.name} атакует 🗡  {other.name}!</h2>']
        other.take_damage(self.attack, ur)
        chance = random.randrange(101)
        if 1 <= ur <= 249 and chance <= 30:
            self.health += 20
            messages.append('<h2>Палладин получил броню!🛡</h2>')
        if 250 <= ur <= 999 and chance <= 35:
            self.health += 25
            messages.append('<h2>Палладин получил броню!🛡</h2>')
        if 1000 <= ur <= 4999 and chance <= 40:
            self.health += 30
            messages.append('<h2>Палладин получил броню!🛡</h2>')
        if 5000 <= ur <= 9999 and chance <= 45:
            self.health += 35
            messages.append('<h2>Палладин получил броню!🛡</h2>')
        if ur >= 10000 and chance <= 50:
            self.health += 40
            messages.append('<h2>Палладин получил броню!🛡</h2>')
        return messages

class Magic(Warrior):
    def attacked(self, other, ur):
        messages = [f'<h2>{self.name} атакует 🗡  {other.name}!</h2>']
        other.take_damage(self.attack, ur)
        chance = random.randrange(101)
        if 1 <= ur <= 249 and chance <= 20:
            self.health += 35
            messages.append('<h2>Маг исцелился!💊</h2>')
        if 250 <= ur <= 999 and chance <= 25:
            self.health +=40
            messages.append('<h2>Маг исцелился!💊</h2>')
        if 1000 <= ur <= 4999 and chance <= 30:
            self.health += 50
            messages.append('<h2>Маг исцелился!💊</h2>')
        if 5000 <= ur <= 9999 and chance <= 35:
            self.health +=55
            messages.append('<h2>Маг исцелился!💊</h2>')
        if ur >= 10000 and chance <= 40:
            self.health +=60
            messages.append('<h2>Маг исцелился!💊</h2>')
        return messages

class Witch(Warrior):
    def attacked(self, other, ur):
        messages = [f'<h2>{self.name} атакует 🗡  {other.name}!</h2>']
        other.take_damage(self.attack, ur)
        chance = random.randrange(101)
        if 1 <= ur <= 249 and chance <= 20:
            other.poison()
            messages.append('<h2>Ведьма отравила соперника!🧪</h2>')
        if 250 <= ur <= 999 and chance <= 25:
            other.poison()
            messages.append('<h2>Ведьма отравила соперника!🧪</h2>')
        if 1000 <= ur <= 4999 and chance <= 30:
            other.poison()
            messages.append('<h2>Ведьма отравила соперника!🧪</h2>')
        if 5000 <= ur <= 9999 and chance <= 35:
            other.poison()
            messages.append('<h2>Ведьма отравила соперника!🧪</h2>')
        if ur >= 10000 and chance <= 40:
            other.poison()
            messages.append('<h2>Ведьма отравила соперника!🧪</h2>')
        return messages

class Podrazhatel(Warrior):
    def take_damage(self, damage, ur):
        chance = random.randrange(101)
        if 1 <= ur <= 249 and chance <= 20:
            messages = ['<h2>Подражатель увернулся!🪞</h2>']
            return messages
        if 250 <= ur <= 999 and chance <= 25:
            messages = ['<h2>Подражатель увернулся!🪞</h2>']
            return messages
        if 1000 <= ur <= 4999 and chance <= 30:
            messages = ['<h2>Подражатель увернулся!🪞</h2>']
            return messages
        if 5000 <= ur <= 9999 and chance <= 35:
            messages = ['<h2>Подражатель увернулся!🪞</h2>']
            return messages
        if ur >= 10000 and chance <= 40:
            messages = ['<h2>Подражатель увернулся!🪞</h2>']
            return messages
        else:
            self.health -= damage
            if self.health < 0:
                self.health = 0

class Vampire(Warrior):
   def attacked(self, other, ur):
        messages = [f'<h2>{self.name} атакует 🗡  {other.name}!</h2>']
        other.take_damage(self.attack, ur)
        chance = random.randrange(101)
        if 1 <= ur <= 249 and chance <= 20:
            self.health += self.attack
            messages.append('<h2>Вампиризм применен!🧛</h2>')
        if 250 <= ur <= 999 and chance <= 25:
            self.health += self.attack
            messages.append('<h2>Вампиризм применен!🧛</h2>')
        if 1000 <= ur <= 4999 and chance <= 30:
            self.health += self.attack
            messages.append('<h2>Вампиризм применен!🧛</h2>')
        if 5000 <= ur <= 9999 and chance <= 35:
            self.health += self.attack
            messages.append('<h2>Вампиризм применен!🧛</h2>')
        if ur >= 10000 and chance <= 40:
            self.health += self.attack
            messages.append('<h2>Вампиризм применен!🧛</h2>')
        return messages
    
class Monstr(Character):
    def poison(self):
        self.health -= self.health/100*40