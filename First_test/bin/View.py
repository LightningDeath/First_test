from bin.module.view.User_choice import user_choice as u_c
from bin.module.view.New_note import new_note as n_n
from bin.module.view.Find_or_delete_record import find_or_delete_record as f_o_d_r
from bin.module.view.Enter_index import enter_index as e_i
from bin.module.view.Enter_header import enter_header as e_h
from bin.module.view.Enter_date import enter_date as e_d
from bin.module.view.Get_parameter import get_parameter as g_p
from bin.module.view.Repeat_message import repeat_message as r_m
from bin.module.view.Wath_edit import wath_edit as w_e
from bin.module.view.Edit import edit as ed
from bin.module.view.View_result import view_result as w_r
from bin.module.view.Warning import warning as war
from bin.module.view.Info import info as inf
from bin.module.view.Repeat import repeat as rep


def user_choice():
    return u_c()


def new_note():
    return n_n()


def find_or_delete_record(value):
    return f_o_d_r(value)


def enter_index():
    return e_i()


def enter_header():
    return e_h()


def enter_date(word):
    return e_d(word)


def get_parameter(text, text2, n_dict):
    return g_p(text, text2, n_dict)


def repeat_message(k):
    return r_m(k)


def wath_edit():
    return w_e()


def edit(ch, index, n_dict):
    return ed(ch, index, n_dict)


def view_result(note_rec):
    w_r(note_rec)


def info(a):
    inf(a)


def warning():
    return war()


def repeat():
    return rep()
