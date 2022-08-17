from random import randint, choices
names = ('Linda', 'Chris', 'Howard', None, 'Chandler', "Alex", None, "Eason")
characters = ("Cloud", "Bayonetta", "Joker", 'Mario', 'Pikachu', 'Kirby', 'Meta Knight', "Link", 'Yoshi', 'Megaman')
dataset = [{"name": name, "characters_used": choices(characters, weights = [3,1,1,1,2,2,3,2,1,3], k=randint(3,5)), 'wins': randint(0,5)} for name in names]
dataset
