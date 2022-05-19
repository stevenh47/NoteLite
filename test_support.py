#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    May 13, 2022 05:57:46 PM PDT  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import test

def main(buttonname, *args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = test.Toplevel1(_top1, buttonname)
    root.mainloop()

def updatelabel(*args):
    _w1.outputText.delete("1.0","end")
    _w1.outputText.insert(END, "new text value")

if __name__ == '__main__':
    test.start_up()




