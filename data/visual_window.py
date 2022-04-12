from tkinter import *
from datetime import datetime
from data.db import db_connect
from data.log import record_log
from data.sql import *
from data.visual_def import *


def window_start(vl_title):
    # НАСТРОЙКИ ОКНА
    window = Tk()
    window.title(vl_title)
    window.geometry('995x500')
    window['background'] = '#DCDCDC'

    # ВЫВОД ИНФОРМАЦИИ ИЗ ТАБЛИЦЫ histori_roll
    def window_journal():
        txt_histori_roll = Text(width=110, height=30)
        txt_histori_roll.grid(row=0, column=1, padx=5, pady=2)
        txt_histori_roll.insert(1.0, text_len(db_connect(get_sql('histori_roll'), 'sql')))
        txt_histori_roll.config(state=DISABLED)
        scroll = Scrollbar(command=txt_histori_roll.yview)
        txt_histori_roll.config(yscrollcommand=scroll.set)
        txt_histori_roll.place(x=100, y=5)

        window.after(1000, window_journal)

    # ЛЕЙБЛ ИМЕНИ
    lable_name_input = Label(width=10, height=1, text='Имя')
    lable_name_input.grid(row=0, column=0, padx=5, pady=1)

    # ВВОД ИМЕНИ
    txt_name_input = Text(width=10, height=1)
    txt_name_input.grid(row=1, column=0, padx=5, pady=1)
    # ЧТЕНИЕ ИМЕНИ ИЗ CONFIG
    txt_name_input.insert(1.0, save_parameter_read('lable_name_input'))

    # ФУНКЦИЯ КНОПКА ТРАВМЫ
    def clic_button_injuries():
        # ЗАПИСЬ В CONFIG ИМЕНИ
        save_parameter_update('lable_name_input', txt_name_input.get("1.0", "end"))
        return db_connect(get_sql('histori_injuries', txt_name_input.get("1.0", "end").strip()), 'pl/sql')

    # ФУНКЦИЯ КНОПКА ПРЫЖОК
    def clic_button_jumping():
        # ЗАПИСЬ В CONFIG ИМЕНИ
        save_parameter_update('lable_name_input', txt_name_input.get("1.0", "end"))
        return db_connect(
            get_sql(
                sql_name='histori_jumping',
                sql_mod_name=txt_name_input.get("1.0", "end").strip(),
                sql_mod_value=v_ck_bx_jumping.get()
            ), 'pl/sql')

    # КНОПКА ТРАВМЫ
    button_injuries = Button(window, text='Травма', command=clic_button_injuries)
    button_injuries.grid(row=3, column=0, sticky="ew", padx=5, pady=1)

    # КНОПКА ПРЫЖОК
    button_injuries = Button(window, text='Прыжок', command=clic_button_jumping)
    button_injuries.grid(row=4, column=0, sticky="ew", padx=5, pady=1)

    # ЧЕКБОКС ПРЫЖОК
    v_ck_bx_jumping = IntVar()
    check_box_jumping = Checkbutton(window, text='В слепую', variable=v_ck_bx_jumping)
    check_box_jumping.grid(row=5, column=0, sticky="ew", padx=5, pady=1)

    # АВТООБНОВЛЕНИЕ ЖУРНАЛА
    window.after(1000, window_journal)
    window.mainloop()
