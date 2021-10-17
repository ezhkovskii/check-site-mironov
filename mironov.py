from time import sleep
from tkinter import messagebox as mb

import requests


DATA_LOGIN = {
    "token": "5402a748fcaeb2a6a9add31803322657",
    "btn:Enter": "Enter"
    }
URL = "http://hsm.ugatu.su/artem/dbproj/"

def try_login(DATA_LOGIN):
    session = requests.Session()
    req = session.post(URL, data=DATA_LOGIN)
    return req.text

def trim_data(data):
    return data[data.find('задание получено'):]


def main():
    print('Проверка этапа Мироновым.\n\nВведите логин и пароль от сайта Миронова:')

    login_successful = False
    while not login_successful:
        login = input('Логин: ')
        password = input('Пароль: ')

        DATA_LOGIN['inp:Login'] = login
        DATA_LOGIN['inp:Password'] = password

        req = try_login(DATA_LOGIN)
        if req.find('Неверный логин') != -1:
            print('Неверный логин или пароль. Попробуйте еще раз.\n')
        else:
            login_successful = True


    print('Проверка запущена. Каждые 30 минут сайт Миронова будет проверяться.' \
        ' При изменении появится уведомление.\n')

    while True:
        data = try_login(DATA_LOGIN)
        data = trim_data(data)

        sleep(60*30)

        another_data = try_login(DATA_LOGIN)
        another_data = trim_data(data)

        if data != another_data:
            mb.showinfo(title='Уведомление', message='Сайт Миронова обновился')
            exit()  

if __name__ == "__main__":
    main()

