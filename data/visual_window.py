from tkinter import *
from datetime import datetime
from data.db import db_connect
from data.log import record_log
from data.sql import *
from data.visual_def import *


def window_start(vl_title):
    window = Tk()
    window.title(vl_title)
    window.geometry('995x500')
    window['background']='#DCDCDC'

    def window_journal():
        txt_output = Text(width=110, height=30)
        txt_output.grid(row=0, column=1, padx=5, pady=2)
        txt_output.insert(1.0, text_len(db_connect(get_sql('histori_roll'), 'sql')))
        txt_output.config(state = DISABLED)
        scroll = Scrollbar(command=txt_output.yview)
        txt_output.config(yscrollcommand=scroll.set)
        txt_output.place(x=100, y=5)

        window.after(1000, window_journal)

    lable_name_input = Label(width=10, height=1, text='Имя')
    lable_name_input.grid(row=0, column=0, padx=5, pady=1)

    txt_name_input = Text(width=10, height=1)
    txt_name_input.grid(row=1, column=0, padx=5, pady=1)
    txt_name_input.insert(1.0, save_parameter_read('lable_name_input'))

    def clic_button_injuries():
        save_parameter_update('lable_name_input', txt_name_input.get("1.0", "end"))
        return db_connect(get_sql('histori_roll_in_injuries', txt_name_input.get("1.0", "end")), 'pl/sql')

    button_injuries = Button(window, text='Травма', command=clic_button_injuries)
    button_injuries.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    window.after(1000, window_journal)
    window.mainloop()
