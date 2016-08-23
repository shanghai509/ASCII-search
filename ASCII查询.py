#coding=utf-8
from Tkinter import *
class show:
    number=dict()
    char=dict()

    def __init__(self):
        self.root=Tk();
        self.root.title("ASCII查询");
        self.root.geometry("400x300");
        self.root.resizable(width=False,height=True);

        Label(text="ASCII查询",font=25).pack();
        self.logn();

        #left
        self.frm_left= Frame(self.root);
        self.frm_left_top=Frame(self.frm_left);
        Label(self.frm_left_top,text="字符",font=(20)).pack(side=LEFT);
        self.var_char=StringVar();
        Entry(self.frm_left_top,textvariable=self.var_char,width = 9).pack(side=RIGHT);
        self.frm_left_top.pack();

        self.varlb_char=StringVar();
        self.listb_char = Listbox(self.frm_left,width=13, height=13,listvariable=self.varlb_char,selectmode=BROWSE)
        for key in self.char.keys():
            self.listb_char.insert(END,key)

        self.scrl_char = Scrollbar(self.frm_left)
        self.scrl_char.pack(side=RIGHT,fill=Y)
        self.listb_char.configure(yscrollcommand = self.scrl_char.set)
        self.listb_char.pack(side=LEFT, fill=BOTH)
        self.scrl_char['command'] = self.listb_char.yview
        self.listb_char.bind('<ButtonRelease>', self.get_char, )
        self.frm_left.pack(side=LEFT)


        #mid
        self.frm_mid=Frame(self.root)
        self.text=Text(self.frm_mid, width=20, height=7,font=15)
        self.text.pack();
        self.btn_clear=Button(self.frm_mid,text="清除",width=6, height=1,command=self.clear).pack(side=LEFT)
        self.btn_search=Button(self.frm_mid,text="查询",width=6, height=1,command=self.search)

        #self.btn_search.bind("<Enter>",self.search)

        self.btn_search.pack(side=RIGHT)
        self.frm_mid.pack(side=LEFT)

        #right
        self.frm_right=Frame(self.root)
        self.frm_rightT=Frame(self.frm_right)
        self.var_number=StringVar();
        Entry(self.frm_rightT,textvariable=self.var_number,width=10).pack(side=LEFT)
        Label(self.frm_rightT,text="数字",font=20).pack(side=RIGHT)
        self.frm_rightT.pack()

        self.varlb_num=StringVar()
        self.listb_num=Listbox(self.frm_right,listvariable=self.varlb_num,width=15, height=13,selectmode=BROWSE)
        self.listb_num.bind('<ButtonRelease>', self.get_num)
        for key in sorted(self.number.keys(),key=lambda t: t[0],reverse=False):
            self.listb_num.insert(END,key)

        self.scrl_num=Scrollbar(self.frm_right)
        self.scrl_num.pack(side=RIGHT,fill=Y)

        self.listb_num.configure(yscrollcommand=self.scrl_num.set)
        self.scrl_num['command']=self.listb_num.yview


        self.listb_num.pack()
        self.frm_right.pack(side=RIGHT)

    def get_char(self,event):
        self.var_char.set('')
        self.var_number.set('')
        tmp = self.listb_char.get(self.listb_char.curselection())
        self.var_char.set(tmp)

    def get_num(self,event):
        self.var_number.set('')
        self.var_char.set('')
        tmp=self.listb_num.get(self.listb_num.curselection())
        self.var_number.set(tmp)

    def search(self,event=NONE):
        self.text.delete("1.0","10.0")
        temp_char=self.var_char.get()
        temp_num=self.var_number.get()
        if temp_char!="":
            if temp_char not in self.char.keys():
                self.text.insert('1.0',"无此字符信息")
            else:
                self.text.insert('1.0',"字符信息："+temp_char+'\n'+'\n')
                self.text.insert("2.0","十进制为:"+str(self.char[temp_char][0])+'\n')
                self.text.insert("3.0", "十六进制为:" + str(self.char[temp_char][1])+'\n')
                self.text.insert("4.0", "字符信息为:" + str(self.char[temp_char][2])+'\n')
        else:
            if temp_num not in self.number.keys():
                self.text.insert('1.0',"无此数字对应的ＡＳＣＩＩ")
            else:
                self.text.insert('1.0', "数字为：" + temp_num + '\n' )
                self.text.insert("2.0", "十进制为:" + str(self.number[temp_num][0]) + '\n')
                self.text.insert("3.0", "十六进制为:" + str(self.number[temp_num][1]) + '\n')
                self.text.insert("4.0", "字符信息为:" + str(self.number[temp_num][2]) + '\n')
    def clear(self):
        self.var_char.set('');
        self.var_number.set('');

        self.text.delete('1.0','10.0');

    def logn(self):
        f=file("shuju.txt");
        for line in f:
            chunk=line.strip().split();
            self.number[chunk[0]]=[chunk[0],chunk[1],chunk[2]]
            self.char[chunk[2]]=[chunk[0],chunk[1],chunk[2]]


def main():
    r=show()
    mainloop()

if __name__=="__main__":
    main()