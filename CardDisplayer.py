#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    Jun 04, 2022 02:53:22 PM PDT  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import CardDisplayer_support

class CardDisplayer:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x518+917+372")
        top.minsize(120, 1)
        top.maxsize(2564, 1421)
        top.resizable(1,  1)
        top.title("CardDisplayer")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.textTitle = tk.Text(self.top)
        self.textTitle.place(relx=0.033, rely=0.058, relheight=0.075
                , relwidth=0.49)
        self.textTitle.configure(background="white")
        self.textTitle.configure(font="TkTextFont")
        self.textTitle.configure(foreground="black")
        self.textTitle.configure(highlightbackground="#d9d9d9")
        self.textTitle.configure(highlightcolor="black")
        self.textTitle.configure(insertbackground="black")
        self.textTitle.configure(selectbackground="#c4c4c4")
        self.textTitle.configure(selectforeground="black")
        self.textTitle.configure(wrap="word")
        self.tooltip_font = "TkDefaultFont"
        self.textTitle_tooltip = \
        ToolTip(self.textTitle, self.tooltip_font, '''????????????''')

        self.FrameTag = tk.Frame(self.top)
        self.FrameTag.place(relx=0.033, rely=0.156, relheight=0.122
                , relwidth=0.908)
        self.FrameTag.configure(relief='groove')
        self.FrameTag.configure(borderwidth="2")
        self.FrameTag.configure(relief="groove")
        self.FrameTag.configure(background="#d9d9d9")
        self.FrameTag.configure(highlightbackground="#d9d9d9")
        self.FrameTag.configure(highlightcolor="black")

        self.textTag = tk.Text(self.FrameTag)
        self.textTag.place(relx=0.018, rely=0.317, relheight=0.429
                , relwidth=0.723)
        self.textTag.configure(background="white")
        self.textTag.configure(font="TkTextFont")
        self.textTag.configure(foreground="black")
        self.textTag.configure(highlightbackground="#d9d9d9")
        self.textTag.configure(highlightcolor="black")
        self.textTag.configure(insertbackground="black")
        self.textTag.configure(selectbackground="#c4c4c4")
        self.textTag.configure(selectforeground="black")
        self.textTag.configure(wrap="word")

        self.buttonShowTags = tk.Button(self.FrameTag)
        self.buttonShowTags.place(relx=0.789, rely=0.317, height=24, width=97)
        self.buttonShowTags.configure(activebackground="beige")
        self.buttonShowTags.configure(activeforeground="#000000")
        self.buttonShowTags.configure(background="#d9d9d9")
        self.buttonShowTags.configure(command=CardDisplayer_support.buttonShowTagsClicked)
        self.buttonShowTags.configure(compound='left')
        self.buttonShowTags.configure(disabledforeground="#a3a3a3")
        self.buttonShowTags.configure(foreground="#000000")
        self.buttonShowTags.configure(highlightbackground="#d9d9d9")
        self.buttonShowTags.configure(highlightcolor="black")
        self.buttonShowTags.configure(pady="0")
        self.buttonShowTags.configure(text='''Show tags''')

        self.labelCardId = tk.Label(self.top)
        self.labelCardId.place(relx=0.717, rely=0.044, height=24, width=124)
        self.labelCardId.configure(activebackground="#f9f9f9")
        self.labelCardId.configure(anchor='w')
        self.labelCardId.configure(background="#d9d9d9")
        self.labelCardId.configure(compound='left')
        self.labelCardId.configure(disabledforeground="#a3a3a3")
        self.labelCardId.configure(foreground="#000000")
        self.labelCardId.configure(highlightbackground="#d9d9d9")
        self.labelCardId.configure(highlightcolor="black")
        self.labelCardId.configure(text='''??????ID???''')

        self.buttonSave = tk.Button(self.top)
        self.buttonSave.place(relx=0.833, rely=0.927, height=24, width=47)
        self.buttonSave.configure(activebackground="beige")
        self.buttonSave.configure(activeforeground="#000000")
        self.buttonSave.configure(background="#d9d9d9")
        self.buttonSave.configure(command=CardDisplayer_support.buttonSaveClick)
        self.buttonSave.configure(compound='left')
        self.buttonSave.configure(disabledforeground="#a3a3a3")
        self.buttonSave.configure(foreground="#000000")
        self.buttonSave.configure(highlightbackground="#d9d9d9")
        self.buttonSave.configure(highlightcolor="black")
        self.buttonSave.configure(pady="0")
        self.buttonSave.configure(text='''Save''')

        self.textContent = ScrolledText(self.top)
        self.textContent.place(relx=0.033, rely=0.309, relheight=0.589
                , relwidth=0.908)
        self.textContent.configure(background="white")
        self.textContent.configure(font="TkTextFont")
        self.textContent.configure(foreground="black")
        self.textContent.configure(highlightbackground="#d9d9d9")
        self.textContent.configure(highlightcolor="black")
        self.textContent.configure(insertbackground="black")
        self.textContent.configure(insertborderwidth="3")
        self.textContent.configure(selectbackground="#c4c4c4")
        self.textContent.configure(selectforeground="black")
        self.textContent.configure(wrap="none")

# Support code for Balloon Help (also called tooltips).
# derived from http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
from time import time, localtime, strftime
class ToolTip(tk.Toplevel):
    """ Provides a ToolTip widget for Tkinter. """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):
        self.wdgt = wdgt
        self.parent = self.wdgt.master
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        self.withdraw()
        self.overrideredirect(True)
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')
    def spawn(self, event=None):
        self.visible = 1
        self.after(int(self.delay * 1000), self.show)
    def show(self):
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()
    def move(self, event):
        self.lastMotion = time()
        if self.follow is False:
            self.withdraw()
            self.visible = 1
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)
    def hide(self, event=None):
        self.visible = 0
        self.withdraw()
    def update(self, msg):
        self.msgVar.set(msg)
#                   End of Class ToolTip

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    CardDisplayer_support.main()

if __name__ == '__main__':
    CardDisplayer_support.main()




