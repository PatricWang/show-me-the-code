import curses
import string

stdscr = curses.initscr()

def display_info(str,x=0,y=0,colorpair=1):
    global stdscr
    stdscr.addstr(y,x,str,curses.color_pair(colorpair))
    stdscr.refresh()

def get_ch_and_continue():
    global stdscr
    stdscr.nodelay(0)
    ch = stdscr.getch()
    stdscr.nodelay(1)
    return True

def set_win():
    global stdscr
    curses.start_color()
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(1)

def unset_win():
    global stdscr
    curses.nocbreak()
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    try:
        set_win()
        display_info('hola,curses',1,1,2)
        # for x in range(15):
        #     for y in range(10):
        #         display_info(string.ascii_letters[(5*x+y)%52],x,y,2)
        display_info('press any key to continue..',0,9)
        get_ch_and_continue()
    except Exception,e:
        raise e
    finally:
        unset_win()