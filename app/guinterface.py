""" This module contains all GUI needs. """
import tkinter as tk
from tkinter import messagebox as tkmb
import settings as s
import app.algo as a


class Field:
    """ Represents Checkers field. """

    # graphics
    _background = 'grey70'

    def __init__(self, app, frame):
        self.app = app
        self.frame = frame
        DotButton.frame = frame
        DotButton.field = self

        self.checkers_used_list = []
        # configure frame
        self.frame.configure(background=self._background)

    def draw(self, **kwargs):
        self.checkers = kwargs.get('checkers', self.app._checkers)
        self.rows = kwargs.get('rows', self.app._rows)
        self.columns = kwargs.get('columns', self.app._columns)
        # draw widgets
        for y in range(self.rows):
            for x in range(self.columns):
                DotButton(x, y)

    def clear(self):
        for item in DotButton.all:
            item.widget.grid_forget()
            del item.widget
            del item
        DotButton.all = []
        self.checkers_used_list = []

    def reset(self):
        for item in DotButton.all:
            item.deactivate()
        self.checkers_used_list = []

    def get_input(self):
        return self.checkers_used_list


class Menu:
    """ Represents Menu Frame. """

    def __init__(self, app, frame):
        self.app = app
        self.frame = frame
        self.draw()

    def draw(self):
        # init
        quit_button = tk.Button(text='QUIT', fg='red', command=quit)
        draw_button = tk.Button(text='Draw', command=self.draw_field)
        clear_button = tk.Button(text='Clear', command=self.clear_field)
        reset_button = tk.Button(text='Reset', command=self.reset_field)
        calculate_button = tk.Button(text='Calculate', command=self.calculate)
        # pack
        quit_button.pack(side=tk.TOP)
        draw_button.pack(side=tk.TOP)
        clear_button.pack(side=tk.TOP)
        reset_button.pack(side=tk.TOP)
        calculate_button.pack(side=tk.BOTTOM)
        # bind
        self.frame.quit = quit_button
        self.frame.draw = draw_button
        self.frame.clear = clear_button
        self.frame.reset = reset_button
        self.frame.calculate = calculate_button

    def draw_field(self):
        self.app.field.draw()

    def clear_field(self):
        self.app.field.clear()

    def reset_field(self):
        self.app.field.reset()

    def calculate(self):
        if not self.app.goal:
            self.app.goal = self.app._goal
        points = a.calculate(self.app.field.get_input(), self.app.goal)
        self.app.show_points(points)


class DotButton:
    all = []
    frame = None
    field = None
    # graphics
    _active_background = 'black'
    _active_font = 'white'

    _not_active_background = 'white'
    _not_active_font = 'black'

    _pad = 3
    _height = s.HEIGHT
    _width = s.WIDTH

    def __init__(self, x, y):
        text = '{},{}'.format(x,y)
        widget = tk.Button(
            self.frame,
            text=text,
            background=self._not_active_background,
            foreground=self._not_active_font,
            height=self._height,
            width=self._width,
            command=self._press(text),
        )
        widget.grid(row=y, column=x,
                    padx=self._pad, pady=self._pad)
        self.widget = widget
        self.text = text
        self.all.append(self)

    def _press(self, text):
        x, y = text.split(',')
        x, y = int(x), int(y)
        def command():
            try:
                index = self.field.checkers_used_list.index((x, y))
            except ValueError:
                self.field.checkers_used_list.append((x, y))
                self.activate()
            else:
                self.field.checkers_used_list.pop(index)
                self.deactivate()
        return command

    def activate(self):
        self.widget['background'] = self._active_background
        self.widget['foreground'] = self._active_font

    def deactivate(self):
        self.widget['background'] = self._not_active_background
        self.widget['foreground'] = self._not_active_font


# main Application
class GUI:
    """ Represents GUI tkinter application. """

    # store defaults
    _columns = s.COLUMNS
    _rows = s.ROWS
    _checkers = s.CHECKERS
    _goal = s.GOAL

    def __init__(self, master):
        self.master = master

        self.field_frame = tk.Frame(self.master)
        self.menu_frame = tk.Frame(self.master)
        # pack frames
        self.field_frame.pack(side=tk.LEFT)
        self.menu_frame.pack(side=tk.RIGHT)

        self.menu = Menu(self, self.menu_frame)
        self.field = Field(self, self.field_frame)

        # define attributes
        self.checkers = None
        self.rows = None
        self.columns = None
        self.goal = None
        self.checkers_left = None

    @staticmethod
    def show_points(points):
        tkmb.showinfo(title='Calculation', message='You have {} points!'.format(points))


# main
def launch_gui():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
