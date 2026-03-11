from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.urls import reverse
from .services import *
from .services.update_ur import upp
from .services.battle_engine import fight
from django.utils.html import mark_safe
from django.contrib import messages
import os
import sqlite3
import hashlib
import time
import threading

def form_one(request):
    return render(request, "form_1.html")

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'player_list.db')
connect = sqlite3.connect('player_list.db', check_same_thread=False)
cursor = connect.cursor()

def reg(request):
    global Name, Pass, Cod
    Name = request.POST.get("name", "Undefined")
    Pass = request.POST.get("pass", "Undefined")
    Pass = Pass.encode('utf-8')
    Pass = hashlib.sha256(Pass)
    Pass = Pass.hexdigest()
    Cod= request.POST.get("cod", "Undefined")
    if Name == "":
        return redirect('home')
    if Pass == "":
        return redirect('home')
    if Cod == "":
        return redirect('home')
    else:
        polz = cursor.execute('SELECT * FROM Users WHERE name = ? AND pass = ? AND cod = ?', [Name, Pass, Cod])
        row = cursor.fetchone()

        if row is None:
            def gener():
                yield '<h2>Приветствую тебя, новичок!🌀 Ты попал в RPG-игру🔥, ' \
                'в которой можно сражаться с монстрами⚔️, которые меняются и ' \
                'становятся сильнее🦾 при прохождении уровней! Но не переживай, 1 из 6 героев🙎, ' \
                'которого ты выберешь, также будет становиться сильнее💪 и улучшать ' \
                'свою способность⚡️. Приступим к 1 этапу!✅️</h2>'
                yield '</div>'
                yield '<script>'
                yield 'document.addEventListener("DOMContentLoaded", function() {'
                yield '    setTimeout(function() {'
                yield '        window.location.href = "/registr/";'
                yield '    }, 12000);'
                yield '});'
                yield '</script>'
            return StreamingHttpResponse(gener())

        else:
            def gener():
                global ur, bag
                polz = cursor.execute(f'SELECT * FROM Users WHERE name = ? AND pass = ? AND cod = ?', [Name, Pass, Cod])
                row = cursor.fetchone()
                yield '<h2>Охо-хо, это же ты! Давненько к нам не заглядывал, где пропадал?🤔<br> \n' \
                'Пойдем скорее, нужно сразиться с множеством монстров!⚔️</h2>'
                ur = int(row[2])
                hero_name = row[3]
                if hero_name == 'Палладин':
                    bag = 0
                elif hero_name == 'Маг':
                    bag = 1
                elif hero_name == 'Ведьма':
                    bag = 2
                elif hero_name == 'Воин':
                    bag = 3
                elif hero_name == 'Подражатель':
                    bag = 4
                elif hero_name == 'Вампир':
                    bag = 5
                upp(ur)
                yield '</div>'
                yield '<script>'
                yield 'document.addEventListener("DOMContentLoaded", function() {'
                yield '    setTimeout(function() {'
                yield '        window.location.href = "/menu/";'
                yield '    }, 6000);'
                yield '});'
                yield '</script>'
            return StreamingHttpResponse(gener())

def registr(request):
    global ur, hero, bag
    ur = 0
    upp(ur)
    
    action_url = reverse('reger')
    
    def gener():
        hero_spis = upp(ur)
        yield '<div class="hero-list">'
        for i, hero in enumerate(hero_spis[0]):
            yield f'<div>{hero}</div>'
            
        yield '</div>'
        
        csrf_token = request.META.get('CSRF_COOKIE')
        
        yield f'''
        <div class="form-container">
            <form method="post" action="{action_url}">
                <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                <h2>Выбери персонажа🙎 (обрати внимание, что после выбора персонажа🙎, 
                его нельзя будет изменить!❌ Для выбора вводи только цифру):</h2>
                
                <div class="input-wrapper">
                    <input type="text" id="Pers" name="Pers" 
                           placeholder="Выбор" 
                           style="padding: 10px; width: 200px;">
                </div>
                
                <button type="submit" style="margin-top: 10px;">
                    Подтвердить
                </button>
            </form>
        </div>
        '''
        
    return StreamingHttpResponse(gener())

def reger(request):
    global ur
    hero_spis = upp(ur)[0]
    
    if request.method != 'POST':
        return redirect('registr')
    
    if request.POST.get('csrfmiddlewaretoken') is None:
        return redirect('registr')
    
    global bag
    bag = request.POST.get("Pers", "Undefined")
    
    try:
        bag = int(bag) - 1
    except ValueError:
        return redirect('registr')
        
    if bag not in range(0, 6):
        return redirect('registr')
        
    hero = hero_spis[bag]
    
    def gener():
        yield f'🙎Выбран герой: {hero.name}✅<br>'
        
        cursor.execute(
            'INSERT INTO Users(name, level, pers, pass, cod) '
            'VALUES(?, ?, ?, ?, ?)', 
            [Name, 0, hero.name, Pass, Cod]
        )
        connect.commit()
        
        yield '<script>'
        yield 'setTimeout(function() {'
        yield '    window.location.href = "/menu/";'
        yield '}, 3000);'
        yield '</script>'
        
    return StreamingHttpResponse(gener())

def menu(request):
    global ur, urr, hero, bag, Name, Pass, Cod
    polz = cursor.execute(f'SELECT * FROM Users WHERE name = ? AND pass = ? AND cod = ?', [Name, Pass, Cod])
    row = cursor.fetchone()
    ur = int(row[2])
    hero_spis = upp(ur)[0]
    upp(ur)
    hero = hero_spis[bag]
    urr = ur + 1
    cursor.execute('''
    SELECT COUNT(*) + 1 AS Mesto
    FROM Users WHERE level > 
    (SELECT level FROM Users WHERE name = ? AND pass = ? AND 
    cod = ?)''', [Name, Pass, Cod])
    mesto = cursor.fetchone()[0]
    polz = cursor.execute(f'SELECT * FROM Users WHERE name = ? AND pass = ? AND cod = ?', [Name, Pass, Cod])
    row = cursor.fetchone()
    def gena():
        csrf_token = request.META.get('CSRF_COOKIE')
        yield f'''
        <h2>------------------------------<br>
        ⚡️{row[1]} | 🙎Персонаж: {hero}<br>
        🔥Уровень: {ur} | ⚠️  Место в рейтинге: {mesto}<br>
        Выберите, что вы хотите сделать:</h2><br>
        <form method="post" action="/vyb/">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            <button type="submit" name="action" value="1">1. Сыграть {urr} уровень⚔️</button><br>
            <button type="submit" name="action" value="2">2. Посмотреть рейтинг игроков⚠️</button><br>
            <button type="submit" name="action" value="3">3. Удалить аккаунт❌</button>
        </form>
        '''
        
    return StreamingHttpResponse(gena())

def vyb(request):
    global ur, urr
    vyb_menu = request.POST.get('action')
    if vyb_menu == '1':
        csr_token = request.META.get('CSRF_COOKIE')
        return HttpResponse(fight(hero, ur, urr, csr_token))
        
    elif vyb_menu == '2':
        def genadiq():
            yield '<h2>⚠️  Рейтинг лучших игроков⚠️</h2>'
            cursor.execute('SELECT name, pers, level FROM Users ORDER BY level DESC LIMIT 20')
            mesto = 1
            time.sleep(1)
            for i in cursor.fetchall():
                i = str(i).replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace("'", "") + ' уровень'
                yield f'<h2>{mesto}. {i}</h2>'
                mesto += 1
                time.sleep(0.4)
            csrf_token = request.META.get('CSRF_COOKIE')
            yield f'''
            <form method="post" action="/menu/">
                <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                <button type="submit" value="0">Выйти</button>
            </form>
            '''
                
        return StreamingHttpResponse(genadiq())

    elif vyb_menu == '3':
        def gena():
            csrf_token = request.META.get('CSRF_COOKIE')
            yield f'''
            <h2>Вы уверены, что хотите удалить аккаунт? ❌<br>
            <form method="post" action="/udalenie/">
                <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                <button type="submit" name="action" value="да">Да</button><br>
                <button type="submit" name="action" value="нет">Нет</button>
            </form>
            '''
        return StreamingHttpResponse(gena())


def udalenie(request):
    button = request.POST.get('action')
    def gena():
        if button == 'да':
            time.sleep(1)
            cursor.execute('DELETE FROM Users WHERE name = ? AND pass = ? AND cod = ?', [Name, Pass, Cod])
            connect.commit()
            yield '<h2>Аккаунт удален.❌</h2>'
            time.sleep(2.5)
            yield '<script>'
            yield 'setTimeout(function() {'
            yield '    window.location.href = "/home/";'
            yield '}, 1000);'
            yield '</script>'

            
        else:
            yield '<h2>Аккаунт сохранен.✅️</h2>'
            time.sleep(2)
            yield '<script>'
            yield 'setTimeout(function() {'
            yield '    window.location.href = "/menu/";'
            yield '}, 1000);'
            yield '</script>'

    return StreamingHttpResponse(gena())