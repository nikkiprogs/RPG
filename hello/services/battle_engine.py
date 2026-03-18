import time
import random
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.html import mark_safe
from .update_ur import upp
from .create_class import *
import os
import sqlite3

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'player_list.db')
connect = sqlite3.connect('player_list.db', check_same_thread=False)
cursor = connect.cursor()

def fight(heroy, ur, urr, csrf_token):
    def gena(heroy, ur, urr, csrf_token):
        global Name, Pass, Cod
        monst_spis = upp(ur)[2]
        mon_boss_spis = upp(ur)[1]
        if urr % 5 == 0:  monst = random.choice(mon_boss_spis)
        else: monst = random.choice(monst_spis)
        yield f'''
            <h2>------------------------------<br>
            ⚔️Битва начинается! Твой соперник: {monst}⚔️</h2>
            '''
        
        finish = f'''
        <form method="post" action="/menu/">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            <button type="submit" value="0">Выйти</button>
        </form>
        '''
        
        for i in range(8):
            if monst.health == 0 or heroy.health == 0:
                break
            yield '<h2>------------------------------</h2>'
            attack_messages = heroy.attacked(monst, urr)
            for msg in attack_messages:
                yield f'<p>{msg}</p>'
            yield f'<h2>Уровень здоровья монстра✳️ : {monst.health}</h2>'
            time.sleep(1)
            if monst.health == 0:
                yield f'<h2>Монстр убит!🩸 Уровень {urr} пройден!✅</h2>'
                ur += 1
                from hello.views import Name, Pass, Cod
                cursor.execute('UPDATE Users SET level = ? WHERE name = ? AND pass = ? AND cod = ?', [ur, Name, Pass, Cod])
                connect.commit()
                monst.vosst()
                heroy.vosst()
                yield finish
                break
            yield '------------------------------'
            monster_attack_messages = monst.attacked(heroy, urr)
            for msg in monster_attack_messages:
                yield f'<p>{msg}</p>'
            yield f'<h2>Уровень здоровья героя✳️ : {heroy.health}</h2>'
            if heroy.health == 0:
                yield f'<h2>Герой убит.🩸 Уровень {urr} не пройден.❌</h2>'
                monst.vosst()
                heroy.vosst()
                yield finish
                break

    return StreamingHttpResponse(gena(heroy, ur, urr, csrf_token))