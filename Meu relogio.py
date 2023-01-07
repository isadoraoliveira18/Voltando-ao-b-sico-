# -*- coding: utf-8 -*-
import tkinter as MeuRelogio

import datetime

class Relogio:
    def __init__(self, master):
        self.myTela = master
        self.relogio = MeuRelogio.Label(
            self.myTela, font=('Comic Sans MS', 25), fg='RED')
        self.relogio.pack(pady=30, padx=30)
        self.alteracao()

    def alteracao(self):
        now = datetime.datetime.now()

        self.relogio['text'] = now.strftime('%H:%M:%S')

        self.myTela.after(1000, self.alteracao)


janelaRaiz = MeuRelogio.Tk()
Relogio(janelaRaiz)
janelaRaiz.mainloop()