import random
import time
from colorama import Fore

turns_list = ['Камень', 'Ножницы', 'Бумага']
count_cpu = 0
game = 0
player_count = 0
print(Fore.YELLOW + 'Это игра Камень ножницы бумага, счет пока 0-0')
time.sleep(0.7)
while game < 4:
    time.sleep(0.9)
    guess = input('Твой ход (Камень, ножницы или бумага?): ')
    cpu_value = random.randint(0, 2)
    cpu_turn = []
    cpu_turn.append(turns_list[cpu_value])
    if guess.capitalize() == turns_list[0] and ''.join(cpu_turn) == turns_list[2]:
        time.sleep(0.9)
        print(''.join(cpu_turn))
        time.sleep(0.3)
        print(Fore.RED +'Я победил! Просто изи....')
        count_cpu +=1
        print(f'Счет: {player_count} - {count_cpu}')
        game+=1
        print(Fore.GREEN + f'Игра номер: {game}')
    elif guess.capitalize() == turns_list[1] and ''.join(cpu_turn) == turns_list[0]:
        time.sleep(0.9)
        print(''.join(cpu_turn))
        time.sleep(0.3)
        print(Fore.RED + 'Я победил! ЛЛЛооооооХХХ')
        count_cpu += 1
        print(f'Счет: {player_count} - {count_cpu}')
        game += 1
        print(Fore.GREEN + f'Игра номер: {game}')
    elif guess.capitalize() == turns_list[2] and ''.join(cpu_turn) == turns_list[1]:
        time.sleep(0.9)
        print(''.join(cpu_turn))
        time.sleep(0.3)
        print(Fore.RED + 'Я победил! АХАХАХХАХА')
        count_cpu += 1
        print(f'Счет: {player_count} - {count_cpu}')
        game += 1
        print(Fore.GREEN + f'Игра номер: {game}')
    elif guess.capitalize() == turns_list[0] and ''.join(cpu_turn) == turns_list[1]:
        time.sleep(0.9)
        print(''.join(cpu_turn))
        time.sleep(0.3)
        print(Fore.GREEN + 'Хм.. Ладно, ты победил...')
        player_count += 1
        print(f'Счет: {player_count} - {count_cpu}')
        game += 1
        print(Fore.GREEN + f'Игра номер: {game}')
    elif guess.capitalize() == turns_list[1] and ''.join(cpu_turn) == turns_list[2]:
        time.sleep(0.9)
        print(''.join(cpu_turn))
        time.sleep(0.3)
        print(Fore.GREEN + 'Твоя победа...Но в следующий раз....')
        player_count += 1
        print(f'Счет: {player_count} - {count_cpu}')
        game += 1
        print(Fore.GREEN + f'Игра номер: {game}')
    elif guess.capitalize() == turns_list[2] and ''.join(cpu_turn) == turns_list[0]:
        time.sleep(0.9)
        print(''.join(cpu_turn))
        time.sleep(0.3)
        print(Fore.GREEN + 'Сегодня не мой день :(((((')
        player_count += 1
        print(f'Счет: {player_count} - {count_cpu}')
        game += 1
        print(Fore.GREEN + f'Игра номер: {game}')
    elif guess.capitalize() == ''.join(cpu_turn):
        print(Fore.BLUE + f'Ничья... Я тоже загадал {guess} \nСчет по прежнему: {player_count} - {count_cpu}')
time.sleep(0.9)
if count_cpu > player_count:
    print(Fore.GREEN + f'Спасибо за игру! Ты проиграл со счетом {player_count} - {count_cpu} ')
elif player_count > count_cpu:
    print(Fore.GREEN + f'Спасибо за игру! Ты победил со счетом {player_count} - {count_cpu} ')
else:
    print(Fore.GREEN + f'Это была тяжелая битва, спасибо за игру, у нас ничья...')
input('Press ENTER to exit')



