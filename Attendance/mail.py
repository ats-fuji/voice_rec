# -*- coding: utf8 -*-
import tkinter
import globals as gl
import calendar
from tkinter.scrolledtext import ScrolledText


root = tkinter.Tk()
root.title(u'勤怠連絡フォーマット')
root.geometry('500x250')


# 削除関数
def delete():
    To_address.delete(0, tkinter.END)
    Cc_address.delete(0, tkinter.END)
    mail_title.delete(0, tkinter.END)
    main_text.delete('1.0', tkinter.END)

# ボタンが押されるとここが呼び出される


def paid(event):
    # 中身を削除してから入力
    delete()
    month.insert(tkinter.END, gl.gv.month)
    day.insert(tkinter.END, gl.gv.day)
    To_address.insert(tkinter.END, 'PTCS*Jisha-Guide問合せ窓口ptcs-jisha-guide@persol.co.jp')
    Cc_address.insert(tkinter.END, '担当営業・MITERASの勤怠承認者')
    mail_title.insert(tkinter.END, '【勤怠連絡_有給】藤森淳_東海1G_342345')
    main_text.insert('1.0', '以下の日程で有給休暇を取得します。\n')
    main_text.insert('2.0', '\t〇/〇（〇）\n')
    main_text.insert('3.0', '理由：私用のため\n')


def holiday_work(event):
    delete()
    To_address.insert(tkinter.END, 'PTCS*Jisha-Guide問合せ窓口ptcs-jisha-guide@persol.co.jp')
    Cc_address.insert(tkinter.END, '担当営業・MITERASの勤怠承認者')
    mail_title.insert(tkinter.END, '【勤怠連絡_休日出勤】藤森淳_東海1G_342345')
    main_text.insert('1.0', '以下の日程で休日出勤します。\n')
    main_text.insert('2.0', '\t〇/〇（〇）\n')
    main_text.insert('3.0', '理由：就業先出社日のため\n')


# ボタン
paid_bt = tkinter.Button(text=u'有休', width=10)
holiday_work_bt = tkinter.Button(text=u'休日出勤', width=10)
calendar_bt = tkinter.Button(text=u'日付選択', width=10)

# 左クリック（<Button-1>）されると関数を呼び出すようにバインド
paid_bt.bind('<Button-1>', paid)
holiday_work_bt.bind('<Button-1>', holiday_work)
#calendar_bt.bind('<Button-1>', calendar.calender_app)

# 最初から配置しておく
date_lbl = tkinter.Label(text='日程：')
month = tkinter.Entry(font=('', 10), width=5)
slash_lbl = tkinter.Label(text='/')
day = tkinter.Entry(font=('', 10), width=5)
To_address = tkinter.Entry(font=('', 10), width=50)
Cc_address = tkinter.Entry(font=('', 10), width=50)
To_lbl = tkinter.Label(text='To：')
Cc_lbl = tkinter.Label(text='Cc：')
title_lbl = tkinter.Label(text='【件名】')
mail_title = tkinter.Entry(font=('', 10), width=50)
main_lbl = tkinter.Label(text='【本文】')
main_text = ScrolledText(root, font=('', 10), height=5, width=50)

# 配置
paid_bt.place(x=20, y=5)
holiday_work_bt.place(x=100, y=5)
date_lbl.place(x=20, y=40)
month.place(x=80, y=40)
slash_lbl.place(x=120, y=40)
day.place(x=130, y=40)
To_address.place(x=80, y=60)
Cc_address.place(x=80, y=80)
To_lbl.place(x=20, y=60)
Cc_lbl.place(x=20, y=80)
title_lbl.place(x=20, y=100)
mail_title.place(x=80, y=100)
main_lbl.place(x=20, y=120)
main_text.place(x=80, y=120)


root.mainloop()
