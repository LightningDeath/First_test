# import datefinder
#
# a = datefinder.find_dates('"Дата начисления 21.04.2022". Отсюда мне надо вытащить только "21/04/2022". 22.12.11')
# b = list(a)
# print(b)
#
# # OUT
# # [datetime.datetime(2022, 4, 21, 0, 0), datetime.datetime(2022, 4, 21, 0, 0)]
#
# print(b[0].date().isoformat())
#
# # OUT
# # '2022-04-21'

from simple_term_menu import TerminalMenu


def main():
    options = ["entry 1", "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


if __name__ == "__main__":
    main()
