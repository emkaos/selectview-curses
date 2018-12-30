import curses 
import subprocess

def main(stdscr):
    # Clear screen
    #stdscr.clear()

    def show_preview(parameter):
        p = subprocess.Popen(f"{command} '{parameter}'", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()
        right_window.clear()
        right_window.addstr(output)

    def print_list(selected_index, start_index):
        left_window.clear()

        line_index = 0
        input_index = start_index
        while (line_index < curses.LINES and input_index < len(input)):
            if input_index == selected_index:
                attr = curses.A_STANDOUT
            else:
                attr = 0
            to_print = input[input_index]
            to_print = to_print.ljust(left_width)
            left_window.addnstr(line_index, 0, to_print, left_width-1, attr)
            line_index += 1
            input_index += 1

    command = 'cat'
    input = ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['c1.py','c2.py','c3.py','c4.py']
    input += ['b1.py','b2.py','b3.py','b4.py']
    input += ['b1.py','b2.py','b3.py','b4.py']
    input += ['b1.py','b2.py','b3.py','b4.py']
    selected_index = 0
    start_index = 0

    left_width = 20

    curses.curs_set(0)
    left_window = curses.newwin(0,left_width,0,0)
    left_window.keypad(1)
    right_window = curses.newwin(0,0,0,left_width)
    right_window.scrollok(1)

    while True:
        print_list(selected_index, start_index)
        show_preview(input[selected_index])

        right_window.refresh()
        left_window.refresh()

        key = left_window.getkey()
        if key == 'q':
            break
        elif key in ('j', 'KEY_DOWN') and selected_index < len(input) -1:
            selected_index += 1
            if selected_index >= curses.LINES:
                start_index += 1;
        elif key in ('k', 'KEY_UP'):
            selected_index -= 1
            if start_index >= curses.LINES:
                start_index -= 1
        elif key == 'G':
            selected_index = len(input) -1
            start_index = len(input) - curses.LINES
        elif key == 'g':
            second_key = left_window.getkey()
            if second_key == 'g':
                start_index = 0
                selected_index = 0
        elif key == '\x04':
            selected_index += curses.LINES
            start_index += curses.LINES
        elif key == '\x15':
            selected_index -= curses.LINES
            start_index -= curses.LINES
            

        if start_index < 0:
            start_index = 0
        if selected_index < 0:
            selected_index = 0
        if start_index > len(input) - curses.LINES:
            start_index = len(input) - curses.LINES
        if selected_index > len(input) - 1:
            selected_index = len(input) -1
        
        #import pdb; pdb.set_trace()


curses.wrapper(main)

#todo
# rechts scrollen
# pfeiltasten, ctrl-ud
# input aus argumenten
