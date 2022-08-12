import os, sys, time as t, importlib.util
from datetime import datetime, timedelta
connection = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(connection)

currentfolder='funcionesd'
songspath = os.path.join(os.getcwd().replace(currentfolder, ''), 'media/', 'songs/')
songspathutils = os.path.join(songspath, 'utilities/')
sys.path.append(songspathutils)
backuppath = os.path.join(os.getcwd().replace(currentfolder, ''), 'media/', 'backups/')
sys.path.append(songspath)
sys.path.append(backuppath)
from appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar
import appfunctions, time as t
from connection import cur

def now():
    # dd/mm/YY H:M:S
    now= datetime.now()
    año= int(now.strftime("%Y"))
    mes= int(now.strftime("%m"))
    dia= int(now.strftime("%d"))
    hora= int(now.strftime("%H"))
    minuto= int(now.strftime("%M"))
    segundo = int(now.strftime("%S"))
    return año, mes, dia, hora, minuto, segundo

def singleday():
    query=f'select id, date, time, currentyear, song from paginaweb_events_list where selection=4;'
    cur.execute(query)
    special=cur.fetchall()
    
    idlist, timelist, datelist, thisyear, songidlist = ([] for i in range(5))

    for idlist_, timelist_, datelist_, thisyear_, songidlist_ in special:
        idlist.append(idlist_)
        datelist.append(timelist_)
        timelist.append(datelist_)
        thisyear.append(thisyear_)
        songidlist.append(songidlist_)
    return idlist, timelist, datelist, thisyear, songidlist

def singleweek():
    query=f'select id, week, time, currentyear, song from paginaweb_events_list where selection=5;'
    cur.execute(query)
    items=cur.fetchall()

    idlist, timelist, weeklist, thisyear, songidlist = ([] for i in range (5))


    
    for idlist_, timelist_, weeklist_, thisyear_, songidlist_ in items:
        idlist.append(idlist_)
        weeklist.append(timelist_)
        timelist.append(weeklist_)
        thisyear.append(thisyear_)
        songidlist.append(songidlist_)

    list1, weekdays=[], []
    for week in weeklist:
        dates = datetime.strptime(week + '-1', "%Y-W%W-%w")
        list1.append(dates)
        
    for day in list1:
        dayweeklist=[]
        for i in range(7):

            tomorrow = str(day + timedelta(days = i))
            dayweeklist.append(tomorrow[:-9])
        weekdays.append(dayweeklist)
    
    
    return idlist, timelist, weekdays, thisyear, songidlist

def singleweekdays():
    query = f'select id, time, currentyear, song from paginaweb_events_list where selection=2;'
    cur.execute(query)
    special=cur.fetchall()
    
    idlist, timelist, currentyear, songidlist = ([] for i in range(4))

    for idlist_, timelist_, currentyear_, songidlist_ in special:
        idlist.append(idlist_)
        timelist.append(timelist_)
        currentyear.append(currentyear_)
        songidlist.append(songidlist_)
        
    return idlist, timelist, currentyear, songidlist

def singleweekendays():
    query = f'select id, time, currentyear, song from paginaweb_events_list where selection=3;'
    cur.execute(query)
    special=cur.fetchall()
    
    idlist, timelist, currentyear, songidlist = ([] for i in range(4))

    for idlist_, timelist_, currentyear_, songidlist_ in special:
        idlist.append(idlist_)
        timelist.append(timelist_)
        currentyear.append(currentyear_)
        songidlist.append(songidlist_)
        
    return idlist, timelist, currentyear, songidlist

def alldays():
    query = f'select id, time, currentyear, song from paginaweb_events_list where selection=1;'
    cur.execute(query)
    special=cur.fetchall()
    
    idlist, timelist, currentyear, songidlist = ([] for i in range(4))

    for idlist_, timelist_, currentyear_, songidlist_ in special:
        idlist.append(idlist_)
        timelist.append(timelist_)
        currentyear.append(currentyear_)
        songidlist.append(songidlist_)
        
    return idlist, timelist, currentyear, songidlist

def playsong(option, song):
    try:
        if option == 1:
            filepath = os.path.join(songspath, song)
            filename = song.replace('.py', '')
            with open(filepath, 'r') as f:
                contenido = f.read()
                
            # print(contenido)
            # print(filename)
            player = compile(contenido, filename, 'exec')
            exec(player)
            año, mes, dia, hora, minuto, segundo=now()
            print(f"ID: {song} | [FINISHED] I've finished waiting working at {año}-{mes}-{dia} | {hora}:{minuto}:{segundo}")
                        
        elif option == 0:
            filepath = os.path.join(songspath, 'defaultsong.py')
            
            with open(filepath, 'r') as f:
                contenido = f.read()
            player = compile(contenido, filename, 'exec')
            exec(player)
            año, mes, dia, hora, minuto, segundo=now()
            print(f"ID: {song} | [FINISHED] I've finished waiting working at {año}-{mes}-{dia} | {hora}:{minuto}:{segundo}")
            
    except Exception as ex:
        print(f'[EXCEPCIÓN] {ex}')



def getsong(ids: int):
    query = f'select filename from paginaweb_events_files where id={ids};'
    cur.execute(query)
    res = cur.fetchall()
    print(res, len(res))
    
    if len(res) == 0:
        print("Es cero")
        año, mes, dia, hora, minuto, segundo=now()
        print(f"ID: {ids} | [STARTING] I've started working at {año}-{mes}-{dia} | {hora}:{minuto}:{segundo}")
        
        playsong(0, '')
        
    elif len(res) == 1:
        songfile = "".join(res[0])
        año, mes, dia, hora, minuto, segundo=now()
        print(f"ID: {ids} | [STARTING] {songfile} I've started working at {año}-{mes}-{dia} | {hora}:{minuto}:{segundo}")
        playsong(1, songfile)


    
    ## Here goes the code
    
