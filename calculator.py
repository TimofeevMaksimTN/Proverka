from tkinter import *
from calcDesign import *

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    if a<0 or b<0: return
    L = a if a > b else b
    while L <= a * b:
        if L%a == 0 and L%b ==0:
            return L
        L+=1

def hcf(a,b):
    if a<0 or b<0: return
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H ==0:
            return H
        H-=1

def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                list.delete(0,END)
                list.insert(END, 'Результат: ', r)
            except:
                list.delete(0,END)
                list.insert(END,'Что-то пошло не так, пожалуйста, введите данные ещё раз')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'Что-то пошло не так, пожалуйста, введите данные ещё раз')

operations = {'ADD':add,'ADDITION':add, 'SUM':add, 'PLUS':add,
            'SUB':sub, 'DIFFERENCE':sub, 'MINUS': sub, 'SUBTRACT':sub,
            'LCM':lcm, 'HCF':hcf, 'PRODUCT':mul, 'MULTIPLICATION':mul,
            'MULTIPLY':mul, 'DIVISION':div, 'DIV':div, 'DIVIDE':div,
            'MOD':mod,'REMAINDER':mod, 'MODULUS':mod}
