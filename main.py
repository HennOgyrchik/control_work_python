# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать

#  идентификатор, 
# заголовок, 
# тело заметки и 
# дату/время создания или последнего изменения заметки.
# 
#  Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее

# Приложение должно запускаться без ошибок, должно уметь 
# сохранять данные в файл, 
# уметь читать данные из файла,
#  делать выборку по дате, 
# выводить на экран выбранную запись, 
# выводить на экран весь список записок, 
# добавлять записку, 
# редактировать ее 
# и удалять.
import os
import datetime
import json

def drawing():
    os.system('CLS')
    print('1 - show a list of notes')
    print('2 - add a new note')
    print('3 - delete a note')
    print('4 - edit a note')
    print('5 - view a note')
    print('6 - show by date')
    print('7 - exit')

def main():
    while True:
        os.system('CLS')
        drawing()
        user_choice=0
        try:
            user_choice=int(input('Input a number: '))
        except:
            continue

        if user_choice==1:
            show_all_notes()
        elif user_choice==2:
            save_in_file(get_new_id(), create_note())
        elif user_choice==3:
             delete_note()
        elif user_choice==4:
            edit_note()
        elif user_choice==5:
            show_note()
        elif user_choice==6:
            show_by_date()
        elif user_choice==7:
            return

def save_in_file(id,note):
    with open('notes/'+id+'.json', "w") as write_file:
        json.dump(note, write_file)
    input('Changes are saved! Press any key ')


def create_note(): 
    note = dict()
    note['title']=input('Note title: ')
    note['body']=input('Text: ')
    note['time']=datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
  
    return note

def get_new_id():
    os.system('CLS')
    id = input('Id: ')

    if (id+'.json') in os.listdir('notes\\'):
        input('A note with this id already exists! Press any key ')
        return get_new_id()
    return id


def show_all_notes():
    os.system('CLS')
    i=1
    for note in os.listdir('notes\\'):
        print(str(i)+') '+note.strip('.json'))
        i=i+1
    input('press any key ')

def delete_note():
    os.system('CLS')
    note=input('Enter the id of the note to delete: ')
    if (note+'.json') not in os.listdir('notes\\'):
        print('Notes with id do not exist!')
        delete_note()
        return
    os.remove('notes\\'+note+'.json')
    input('Note deleted! Press any key ')

def edit_note():
    os.system('CLS')
    id=input('Enter the note id to change: ')
    if (id+'.json') not in os.listdir('notes\\'):
        input('Note with id does not exist! Press any key ')
        edit_note()
        return
    
    save_in_file(id,create_note())
    

def show_note():
    os.system('CLS')
    id=input('Enter the note id: ')
    if (id+'.json') not in os.listdir('notes\\'):
        input('Note with id does not exist! Press any key ')
        show_note()
        return

    note=dict()
    with open('notes\\'+id+'.json', 'r', encoding='utf-8') as f: 
        note = json.load(f) 

    input('Title: '+note['title']+'\nText: '+note['body']+'\nDate: '+note['time']+'\nPress any key ')

def show_by_date():
    os.system('CLS')
    try:
        start_date_str=input('Enter the START date in the format dd.mm.yyyy hh:mm or leave it empty: ')
        if not start_date_str:
            start_date=datetime.datetime.strptime('01.01.0001 00:00','%d.%m.%Y %H:%M')
        else:
            start_date=datetime.datetime.strptime(start_date_str,'%d.%m.%Y %H:%M')

        end_date_str=input('Enter the END date in the format dd.mm.yyyy hh:mm or leave it empty: ')
        if not end_date_str:
            end_date=datetime.datetime.now()
        else:
            end_date=datetime.datetime.strptime(end_date_str,'%d.%m.%Y %H:%M')
    except:
        input('invalid date format!')
        show_by_date()
        return
    
    list_notes=list(list(dict()))
    for f in os.listdir('notes\\'):
        with open('notes\\'+f, 'r', encoding='utf-8') as file:
            list_notes.append((f,json.load(file)))

    i=1
    for note in list_notes:
        
        note_time=datetime.datetime.strptime(note[1]['time'],'%d.%m.%Y %H:%M')
        if  (start_date < note_time) and (note_time < end_date):
            print(str(i)+') '+note[0].strip('.json'))
            i=i+1

    input('Press any key ')

main()