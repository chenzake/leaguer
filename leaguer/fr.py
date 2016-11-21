# -*- coding:utf-8 -*-

import Tkinter
import ttk
from db import session, User
from sqlalchemy import or_


# "选择方法的command，向treeview中填充数据"
def get_user(name=None,phonenumber=None,money=None):

    # 清空原节点
    for _ in map(tree.delete, tree.get_children("")):
        pass
    user = session.query(User)
    if name is None and phonenumber is None and money is None:
        persons = user.filter(or_(User.name == var1.get(),
                                  User.phonenumber == var2.get(),
                                  User.money == var_money.get())).all()
    else:
        persons = user.filter(or_(User.name == name,
                                  User.phonenumber == phonenumber,
                                  User.money == money)).all()

    for i, person in enumerate(persons):
        id = person.id
        name = person.name
        phonenumber = person.phonenumber
        money = person.money
        tree.insert('', i, values=(id, name, phonenumber, money))


Delete_item = []


# “鼠标选中事件”
def select(event):
    global Delete_item
    Delete_item = []
    seitem = tree.selection()
    # print seitem

    se = tree.item(seitem)
    Delete_item.append(se)
    # print Delete_item


Update_dict = {}


def update(event):
    global Update_dict
    Update_dict = {}
    print event.y, event.x
    rowid = tree.identify_row(event.y)
    column = tree.identify_column(event.x)
    print rowid
    x, y, width, height = tree.bbox(rowid, column)

    print x, y, width, height
    seitem = tree.selection()
    se = tree.item(seitem)
    print se['values']
    var1_update.set(se['values'][1])
    var2_update.set(se['values'][2])
    var_money_update.set(se['values'][3])
    pady = height // 2

    entry7.place(x=0 + 90, y=y + pady, anchor='w')

    entry8.place(x=90 + 100, y=y + pady, anchor='w')

    entry9.place(x=90 + 100 + 190, y=y + pady, anchor='w')
    # print var2_update.get()
    Update_dict = {'id': se['values'][0]}


def update_user():
    entry7.place_forget()
    entry8.place_forget()
    entry9.place_forget()
    print var2_update.get()
    global Update_dict
    if Update_dict:
        user = session.query(User)
        user.filter(User.id == Update_dict['id']).update({User.name:var1_update.get(),
                                                        User.phonenumber:var2_update.get(),
                                                        User.money:var_money_update.get()})

        print user.filter(User.id == 1).one().phonenumber
        session.commit()

    get_user(var1_update.get(), var2_update.get(), var_money_update.get())

def delete_user():
    global Delete_item
    # print Delete_item
    for user in Delete_item:
        user_id = user['values'][0]

        session.query(User).filter(User.id == user_id).delete()
    session.commit()
    get_user()


root = Tkinter.Tk()
root.title("会员管理")
root.geometry("600x600")
frame1 = Tkinter.Frame(root, width=600, heigh=200)
frame2 = Tkinter.Frame(root, width=600, heigh=200)
frame3 = Tkinter.Frame(root, width=600, heigh=100)
frame4 = Tkinter.Frame(root, width=600, heigh=100)

# scrollbar = Tkinter.Scrollbar(frame2)


var1_update = Tkinter.Variable()
var2_update = Tkinter.Variable()
var_money_update = Tkinter.Variable()
var1 = Tkinter.Variable()
var2 = Tkinter.Variable()
var_money = Tkinter.Variable()
# label1 =Tkinter.Label(root, text="姓名").grid(row=0)
label1 = Tkinter.Label(frame1, text="姓名").grid(row=0, padx=10, pady=10, sticky='NSEW')
entry1 = Tkinter.Entry(frame1, textvariable=var1).grid(row=0, column=1)
label2 = Tkinter.Label(frame1, text="电话").grid(row=1, padx=10, pady=10)
entry2 = Tkinter.Entry(frame1, textvariable=var2).grid(row=1, column=1)
label_money = Tkinter.Label(frame1, text="余额").grid(row=2, padx=10, pady=10)
entry_money = Tkinter.Entry(frame1, textvariable=var_money).grid(row=2, column=1)
search_button = Tkinter.Button(frame1, text='查找', bg='grey', width=10, heigh=3, command=get_user)
search_button.grid(row=0, column=2, columnspan=2, rowspan=2, padx=100, pady=10)

tree = ttk.Treeview(frame2, column=("id", "name", "phone", "money"), show='headings',
                    )
tree.bind("<ButtonRelease-1>", select)
tree.bind('<Double-Button-1>', update)

vbar = ttk.Scrollbar(frame2, orient='vertical', command=tree.yview)
# 设置滚动条
tree.configure(yscrollcommand=vbar.set)
tree.column('id', width=90, anchor='center')
tree.column('name', width=100, anchor='center')
tree.column('phone', width=190, anchor='center')
tree.column('money', width=190, anchor='center')
tree.heading('id', text="编号")
tree.heading('name', text="姓名")
tree.heading('phone', text="电话")
tree.heading('money', text="余额")

tree.grid(row=0, column=0, sticky='NSEW')
vbar.grid(row=0, column=1, sticky='NS')

delete_button = Tkinter.Button(frame3, text="删除", bg='grey',
                               width=10, heigh=3, command=delete_user)
delete_button.grid(row=0, column=1, columnspan=2, rowspan=2, padx=50)

update_button = Tkinter.Button(frame3, text="修改", bg='grey',
                               width=10, heigh=3, command=update_user)
update_button.grid(row=0, column=0, )


def add_user():
    new_user = User(name=var3.get(), phonenumber=var4.get(), money=var5.get())
    session.add(new_user)
    session.commit()
    get_user(var3.get(),var4.get(),var5.get())

var5 = Tkinter.Variable()
var3 = Tkinter.Variable()
var4 = Tkinter.Variable()
label3 = Tkinter.Label(frame4, text="姓名").grid(row=0, sticky='NSEW')
label4 = Tkinter.Label(frame4, text="电话").grid(row=1, sticky='NSEW')
label5 = Tkinter.Label(frame4, text="余额").grid(row=2, sticky='NSEW')
entry3 = Tkinter.Entry(frame4, textvariable=var3).grid(row=0, column=1)
entry4 = Tkinter.Entry(frame4, textvariable=var4).grid(row=1, column=1)
entry5 = Tkinter.Entry(frame4, textvariable=var5).grid(row=2, column=1)
add_button = Tkinter.Button(frame4, text="增加", bg="grey", width=10, heigh=3, command=add_user)
add_button.grid(row=0, column=2, rowspan=3, padx=100, )


entry7 = Tkinter.Entry(tree, textvariable=var1_update, width=90)
entry8 = Tkinter.Entry(tree, textvariable=var2_update, width=100)
entry9 = Tkinter.Entry(tree, textvariable=var_money_update, width=190)


frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=2, pady=10)
frame1.grid_propagate(0)
frame2.grid_propagate(0)
frame4.grid(row=3, pady=20)
frame4.grid_propagate(0)

root.mainloop()
