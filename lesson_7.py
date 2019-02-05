#!/usr/bin/python3

import random
import time
import sys


"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
class Keg: # достаем бочонок из мешка
   def get_bag(self):
        bag = [i for i in range(1, self.numb + 1)]
        random.shuffle(bag)
        for x, y in enumerate(bag):
            print('{:*^30}'.format('*'))
            print('Бочонок номер: {} (осталось {})'.format(y, self.numb - (x + 1)))
            yield y
   
   def __init__(self, numb):
      self.numb = numb
      self.gen = self.get_bag()

class Card:

   def __set_card(self):
        num_in_row = set()
        while len(num_in_row) < self.rows * 5:
            num_in_row.add(random.randint(1, 91))
        cards = list(num_in_row)
        random.shuffle(cards)
        while len(cards) % self.rows != 0:
            cards.append('None')
        self.rows = int(len(cards) / self.rows)
        cards = [cards[i: i + self.rows] for i in range(0,len(cards),self.rows)]

        for i in range(len(cards)):
            cards[i].sort()
        self.card_user = cards[:3]
        self.card_pc = cards[3:]
   def __init__(self, amount_card):
      row = 3
      self.rows = row * amount_card
      self.__set_card()
   def get_card(self, card_gamers):
        print('{:-^25}'.format(self.name))
        print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(card_gamers[0]))
        print('{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]} '.format(card_gamers[1]))
        print('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(card_gamers[2]))
        print('{:-^25}'.format( '-'))
   def find(self, card_gamers, num_keg):
        for i, n in enumerate(card_gamers):
            if num_keg in n:
                card_gamers[i][n.index(num_keg)] = '-'
                self.score += 1
                if self.score == 15:
                    print('{} Победила!'.format(self.name))
                    sys.exit(1)
                return True
        return False

class Gamers(Card):

    def __init__(self, name):
        self.name = name
        self.score = 0

def main():

    game = Card(2)
    keg = Keg(90)
    gamer_human = Gamers('Карточка игрока')
    gamer_pc = Gamers('Карточка компьютера')

    while True:
        num_keg = next(keg.gen)
        gamer_human.get_card(game.card_user)
        gamer_pc.get_card(game.card_pc)
        
        print("Введите 'y', если хотите зачеркнуть цифру")
        print("Введите 'n', если хотите продолжить")
        choose = input("Зачеркнуть цифру? (y/n): ")
        if choose == 'y':
            if gamer_human.find(game.card_user, num_keg):
                continue
            else:
                print('Game Over')
                sys.exit(1)
        if choose == 'n':
            if gamer_human.find(game.card_user, num_keg):
                print('Game Over')
                sys.exit(1)
            elif gamer_human.find(game.card_pc, num_keg):
                continue
        if choose != 'n' and choose != 'y':
            print('Введите y или n')
            time.sleep(1)
            continue

if __name__ == '__main__':
    main()
