from tkinter import *
from tkinter import ttk
expression = "" 


root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(width=False, height=False)

def clear(): 
	global expression 
	expression = "" 
	nimadir.set("") 

def equalpress(): 

	try: 

		global expression 

		total = str(eval(expression)) 

		nimadir.set(total) 
		expression = "" 

	except: 

		nimadir.set(" error ") 
		expression = ""

def press(num): 

	global expression 


	expression = expression + str(num) 


	nimadir.set(expression) 

for c in range(5): root.columnconfigure(index=c, weight=1)
for r in range(8): root.rowconfigure(index=r, weight=1)

nimadir = StringVar()
field = ttk.Entry(root, textvariable=nimadir)
field.grid(row=0, column=0, rowspan=2 , columnspan=5, sticky='wesn')

mc=ttk.Button(root, text='Mc')
mc.grid(row=2,column=0, sticky='wesn')
mr=ttk.Button(root, text='Mr')
mr.grid(row=2,column=1, sticky='wesn')
ms=ttk.Button(root, text='Ms')
ms.grid(row=2,column=2, sticky='wesn')
mpilus=ttk.Button(root, text='M+')
mpilus.grid(row=2,column=3, sticky='wesn')
mminus=ttk.Button(root, text='M-')
mminus.grid(row=2,column=4, sticky='wesn')


back = ttk.Button(root, text='➡')
back.grid(row=3, column=0 , sticky='wesn')
ce = ttk.Button(root, text='Ce')
ce.grid(row=3, column=1 , sticky='wesn')
c = ttk.Button(root, text='C',command=clear)
c.grid(row=3, column=2 , sticky='wesn')
plusminus = ttk.Button(root, text='+-',command=lambda: press(''))
plusminus.grid(row=3, column=3 , sticky='wesn')
ildiz = ttk.Button(root, text='√',command=lambda: press('√'))
ildiz.grid(row=3, column=4 , sticky='wesn')

yetti = ttk.Button(root, text='7',  command=lambda: press(7))
yetti.grid(row=4, column=0 , sticky='wesn')
sakkkiz = ttk.Button(root, text='8',  command=lambda: press(8))
sakkkiz.grid(row=4, column=1 , sticky='wesn')
toqiz= ttk.Button(root, text='9',  command=lambda: press(9))
toqiz.grid(row=4, column=2 , sticky='wesn')
bolish = ttk.Button(root, text='/',command=lambda: press('/'))
bolish.grid(row=4, column=3 , sticky='wesn')
foiz = ttk.Button(root, text='%',command=lambda: press('%'))
foiz.grid(row=4, column=4 , sticky='wesn')


tort = ttk.Button(root, text='4',  command=lambda: press(4))
tort.grid(row=5, column=0 , sticky='wesn')
besh = ttk.Button(root, text='5',  command=lambda: press(5))
besh.grid(row=5, column=1 , sticky='wesn')
olti= ttk.Button(root, text='6',  command=lambda: press(6))
olti.grid(row=5, column=2 , sticky='wesn')
kopaytirish = ttk.Button(root, text='*',command=lambda: press('*'))
kopaytirish.grid(row=5, column=3 , sticky='wesn')
x = ttk.Button(root, text='1/x')
x.grid(row=5, column=4 , sticky='wesn')


birr = ttk.Button(root, text='1', command=lambda: press(1))
birr.grid(row=6, column=0 , sticky='wesn')
ikki = ttk.Button(root, text='2',  command=lambda: press(2))
ikki.grid(row=6, column=1 , sticky='wesn')
uch= ttk.Button(root, text='3',  command=lambda: press(3))
uch.grid(row=6, column=2 , sticky='wesn')
minus = ttk.Button(root, text='-',command=lambda: press('-'))
minus.grid(row=6, column=3 , sticky='wesn')
teng = ttk.Button(root, text='=',command=equalpress)
teng.grid(row=6, rowspan=2, column=4 , sticky='wesn')

nol = ttk.Button(root, text='0', command=lambda: press(0))
nol.grid(row=7, column=0 , columnspan=2, sticky='wesn')
vergul = ttk.Button(root, text=',',command=lambda: press(','))
vergul.grid(row=7, column=2 , sticky='wesn')
pilus= ttk.Button(root, text='+',command=lambda: press('+'))
pilus.grid(row=7, column=3, sticky='wesn')




root.mainloop()
