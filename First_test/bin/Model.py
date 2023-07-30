import os

from bin.module.model.Open_file import open_file as o_f
from bin.module.model.Add_note import add_note as a_n
from bin.module.model.Find_rec_date import find_rec_date as f_r_d
from bin.module.model.Find_rec_index import find_rec_index as f_r_i
from bin.module.model.Find_rec_header import find_rec_header as f_r_h
from bin.module.model.Delete_rec import delete_rec as d_r
from bin.module.model.Read_note import read_note as r_n
from bin.module.model.Clear_note import clear_note as c_n
from bin.module.model.Rewrite import rewrite as rw
from bin.module.model.Edite_note import edit_note as e_n
from bin.module.model.Check_empty import check_empty as c_e

path = os.getcwd() + r"\data\note.json"


def open_file():
    return o_f(path)


def add_note(note_list, index, n_dict):
    return a_n(path, note_list, index, n_dict)


def find_rec_index(index, n_dict):
    return f_r_i(index, n_dict)


def find_rec_header(header, n_dict):
    return f_r_h(header, n_dict)


def find_rec_date(date, word, n_dict):
    return f_r_d(date, word, n_dict)


def delete_rec(flag, value, n_dict):
    return d_r(flag, value, n_dict)


def read_note():
    return r_n(path)


def clear_note():
    c_n(path)


def edit_note(flag, index, text, note_dict):
    """ Функция изменяет текст или заголовок по индексу\n
        flag определяет поведение 1 - текст, 2 - заголовок\n
        index - номер записи\n
        text - введенный пользователем текст\n
        note_dict - текущий словарь
    """
    return e_n(flag, index, text, note_dict)


def rewrite(n_dict):
    rw(path, n_dict)


def check_empty(n_dict):
    return c_e(n_dict)
