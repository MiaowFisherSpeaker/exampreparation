# -*- coding: utf-8 -*-
import tkinter as tk
import json
Name_code_dic = {}#code_name:code
#从json文件调用
try:
    with open('code.json','r',encoding = 'utf-8') as code:
        a = code.read()
        Name_code_dic = json.loads(a,strict = False)
except:
    print('可能文件有问题，删掉多余的逗号试试')
    
code_name_ls,code_ls = [],[]
for m,n in Name_code_dic.items():
    code_name_ls.append(m)
    code_ls.append(n)

# class ExamSearch:#以后可能要用
#     '''
#     总结期中考试以前的代码
    
#     '''
#     def __init__(self,code_name,code):
#         self.o1 = code_name
#         self.o2 = code
    
#     def listCode():
#         code_name_list = ['ASCII小写转化成大写']
#         print(*code_name_list)
        
        
#     def search(code_name):
#         print(Name_code_dic[code_name])
                
        
        
        
    
#窗体部分
window = tk.Tk()
window.title('函数查询')
window.geometry('800x800')


#输入文本框e
e = tk.Entry(window,show = None)
e.pack()

#定义按钮功能 
def insert_end():#按钮,文本输入进行运算,对应b1
    var = e.get()
    if var.lower() == '/help':
        t.insert('end','''
                 本小程序依靠bug运行
                 可以自己在json文件中添加以及修改自己的索引，供自己使用
                 输入/help提供指令帮助
                 输入/list查看可查询函数列表
                 使用方法：在输入框中正确输入查询名称，点击查询按钮即可
                 点击清空按钮可以清除文本框
                 出现其他问题找喵喵''')
        return
    if var.lower() == '/list':
        for i in code_name_ls:
            t.insert('end',i+'\n')
        return
    if var not in Name_code_dic.keys() and var != '':
        t.insert('end','没有此函数,输入/list查看函数列表\n')
    elif var in Name_code_dic.keys():
        t.insert('end',Name_code_dic[var])
        t.insert('end','\n')
    else:
        return

def clearBox():#按钮,清除文本框,对应b2
    t.delete('1.0','end')

#按钮，查询,b1
b1 = tk.Button(window,text = '查询',width=10, height=2, command = insert_end)

b1.pack()

#按钮，清空文本框,b2
b2 = tk.Button(window,text = '清空',width=10, height=2,command = clearBox)
b2.pack()

#输出文本框t
t = tk.Text(window,height = 600)
t.pack()

#显示窗口
window.mainloop()



