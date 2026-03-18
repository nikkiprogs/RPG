from .create_class import *

def upp(ur):
    global hero_spis, mon_boss_spis, monst_spis, warrior, witch, vampire, mag, palladin, podrazhatel
    if 0 <= ur < 100:
        goblin = Monstr('Гоблин', 35, 70)
        ork = Monstr('Орк', 30, 85)
        troll = Monstr('Тролль', 20, 115)
        demon_boss = Monstr('Босс Демон', 35, 130)
        ork_boss = Monstr('Босс Орк', 25, 150)
        palladin = Palladin('Палладин', 35, 90, 'Броня 20 с шансом 30%🛡')
        mag = Magic('Маг', 30, 100, 'Лечение на 35 с шансом 20%💊')
        witch = Witch('Ведьма', 25, 100, 'Отравление на 40% здоровья с шансом 20%🧪')
        warrior = Warrior('Воин', 40, 80, 'Критический урон (Х2) с шансом 25%🗡🗡')
        podrazhatel = Podrazhatel('Подражатель', 25, 100, 'Уклонение от атаки с шансом 20%🪞')
        vampire = Vampire('Вампир', 30, 80, 'Шанс вампиризма 20%🧛')
        monst_spis = [goblin, ork, troll]
        mon_boss_spis = [ork_boss, demon_boss]
        hero_spis = [palladin, mag, witch, warrior, podrazhatel, vampire]

    if 100 <= ur < 250:
        goblin = Monstr('Гном', 40, 80)
        ork = Monstr('Полурослик', 30, 95)
        troll = Monstr('Дварф', 20, 130)
        demon_boss = Monstr('Босс Гном', 40, 145)
        ork_boss = Monstr('Босс Дварф', 25, 170)
        palladin = Palladin('Палладин', 35, 100, 'Броня 20 с шансом 30%🛡')
        mag = Magic('Маг', 35, 115, 'Лечение на 35 с шансом 20%💊')
        witch = Witch('Ведьма', 25, 115, 'Отравление на 40% здоровья с шансом 20%🧪')
        warrior = Warrior('Воин', 45, 90, 'Критический урон (Х2) с шансом 25%🗡🗡')
        podrazhatel = Podrazhatel('Подражатель', 25, 115, 'Уклонение от атаки с шансом 20%🪞')
        vampire = Vampire('Вампир', 30, 90, 'Шанс вампиризма 20%🧛')
        monst_spis = [goblin, ork, troll]
        mon_boss_spis = [ork_boss, demon_boss]
        hero_spis = [palladin, mag, witch, warrior, podrazhatel, vampire]

    if 250 <= ur < 500:
        goblin = Monstr('Орк-гоблин', 45, 90)
        ork = Monstr('Гоблиноид', 35, 105)
        troll = Monstr('Троллеподобная нечисть', 25, 145)
        demon_boss = Monstr('Босс Гоблиноид', 45, 160)
        ork_boss = Monstr('Босс Нечисть', 30, 190)
        palladin = Palladin('Палладин', 40, 110, 'Броня 25 с шансом 35%🛡')
        mag = Magic('Маг', 35, 130, 'Лечение на 40 с шансом 25%💊')
        witch = Witch('Ведьма', 30, 130, 'Отравление на 40% здоровья с шансом 25%🧪')
        warrior = Warrior('Воин', 45, 100, 'Критический урон (Х2) с шансом 30%🗡🗡')
        podrazhatel = Podrazhatel('Подражатель', 30, 130, 'Уклонение от атаки с шансом 25%🪞')
        vampire = Vampire('Вампир', 30, 100, 'Шанс вампиризма 25%🧛')
        monst_spis = [goblin, ork, troll]
        mon_boss_spis = [ork_boss, demon_boss]
        hero_spis = [palladin, mag, witch, warrior, podrazhatel, vampire]

    if 500 <= ur < 1000:
        goblin = Monstr('Великан', 50, 100)
        ork = Monstr('Огр', 35, 115)
        troll = Monstr('Зверочеловек', 25, 160)
        demon_boss = Monstr('Босс Великан-огр', 50, 180)
        ork_boss = Monstr('Босс Рептилоид', 30, 210)
        palladin = Palladin('Палладин', 40, 125, 'Броня 25 с шансом 35%🛡')
        mag = Magic('Маг', 35, 145, 'Лечение на 40 с шансом 25%💊')
        witch = Witch('Ведьма', 30, 145, 'Отравление на 40% здоровья с шансом 25%🧪')
        warrior = Warrior('Воин', 50, 110, 'Критический урон (Х2) с шансом 30%🗡🗡')
        podrazhatel = Podrazhatel('Подражатель', 35, 145, 'Уклонение от атаки с шансом 25%🪞')
        vampire = Vampire('Вампир', 30, 110, 'Шанс вампиризма 25%🧛')
        monst_spis = [goblin, ork, troll]
        mon_boss_spis = [ork_boss, demon_boss]
        hero_spis = [palladin, mag, witch, warrior, podrazhatel, vampire]

    if 1000 <= ur < 2500:
        goblin = Monstr('Дракон', 55, 110)
        ork = Monstr('Дракон-гоблин', 40, 130)
        troll = Monstr('Бес', 30, 175)
        demon_boss = Monstr('Босс Демоноид', 55, 200)
        ork_boss = Monstr('Босс Драконид', 35, 230)
        palladin = Palladin('Палладин', 45, 150, 'Броня 30 с шансом 40%🛡')
        mag = Magic('Маг', 35, 160, 'Лечение на 50 с шансом 30%💊')
        witch = Witch('Ведьма', 30, 160, 'Отравление на 40% здоровья с шансом 30%🧪')
        warrior = Warrior('Воин', 50, 120, 'Критический урон (Х2) с шансом 35%🗡🗡')
        podrazhatel = Podrazhatel('Подражатель', 35, 160, 'Уклонение от атаки с шансом 30%🪞')
        vampire = Vampire('Вампир', 35, 120, 'Шанс вампиризма 30%🧛')
        monst_spis = [goblin, ork, troll]
        mon_boss_spis = [ork_boss, demon_boss]
        hero_spis = [palladin, mag, witch, warrior, podrazhatel, vampire]

    if 2500 <= ur < 5000:
        goblin = Monstr('Джин', 60, 120)
        ork = Monstr('Нежить', 45, 140)
        troll = Monstr('Природный дух', 30, 190)
        demon_boss = Monstr('Босс Фея', 60, 220)
        ork_boss = Monstr('Босс Зомби', 40, 250)
        palladin = Palladin('Палладин', 45, 160, 'Броня 30 с шансом 40%🛡')
        mag = Magic('Маг', 40, 170, 'Лечение на 50 с шансом 30%💊')
        witch = Witch('Ведьма', 35, 170, 'Отравление на 40% здоровья с шансом 30%🧪')
        warrior = Warrior('Воин', 55, 130, 'Критический урон (Х2) с шансом 35%🗡🗡')
        podrazhatel = Podrazhatel('Подражатель', 35, 170, 'Уклонение от атаки с шансом 30%🪞')
        vampire = Vampire('Вампир', 35, 130, 'Шанс вампиризма 30%🧛')
        monst_spis = [goblin, ork, troll]
        mon_boss_spis = [ork_boss, demon_boss]
        hero_spis = [palladin, mag, witch, warrior, podrazhatel, vampire]

    if 5000 <= ur < 10000:
        goblin = Monstr('Лиса-нежить', 65, 130)
        ork = Monstr('Волк-гоблин', 50, 155)
        troll = Monstr('Ангел', 35, 205)
        demon_boss = Monstr('Босс Лорд', 65, 240)
        ork_boss = Monstr('Босс Королевский тролль', 45, 275)
        palladin = Palladin('Палладин', 50, 170, 'Броня 35 с шансом 45%🛡')
        mag = Magic('Маг', 40, 185, 'Лечение на 55 с шансом 35%💊')
        witch = Witch('Ведьма', 35, 185, 'Отравление на 40% здоровья с шансом 35%🧪')
        warrior = Warrior('Воин', 55, 145, 'Критический урон (Х2) с шансом 40%🗡🗡')
        podrazhatel = Podrazhatel('Подражатель', 40, 180, 'Уклонение от атаки с шансом 35%🪞')
        vampire = Vampire('Вампир', 40, 140, 'Шанс вампиризма 35%🧛')
        monst_spis = [goblin, ork, troll]
        mon_boss_spis = [ork_boss, demon_boss]
        hero_spis = [palladin, mag, witch, warrior, podrazhatel, vampire]
        
    if ur >= 10000:
        goblin = Monstr('Лесной эльф', 70, 140)
        ork = Monstr('Птицезмей', 60, 170)
        troll = Monstr('Темный эльф', 40, 230)
        demon_boss = Monstr('Босс Демоническая сущность', 70, 260)
        ork_boss = Monstr('Босс ???', 50, 300)
        palladin = Palladin('Палладин', 50, 180, 'Броня 40 с шансом 50%🛡')
        mag = Magic('Маг', 45, 200, 'Лечение на 60 с шансом 40%💊')
        witch = Witch('Ведьма', 40, 200, 'Отравление на 40% здоровья с шансом 40%🧪')
        warrior = Warrior('Воин', 60, 160, 'Критический урон (Х2) с шансом 45%🗡🗡')
        podrazhatel = Podrazhatel('Подражатель', 40, 200, 'Уклонение от атаки с шансом 40%🪞')
        vampire = Vampire('Вампир', 40, 160, 'Шанс вампиризма 40%🧛')
        monst_spis = [goblin, ork, troll]
        mon_boss_spis = [ork_boss, demon_boss]
        hero_spis = [palladin, mag, witch, warrior, podrazhatel, vampire]
        
    return [hero_spis, mon_boss_spis, monst_spis]

