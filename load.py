import os

def parser(string, pemisah):
    res = []              
    tmp = ''              
    for ch in string:
        if ch == pemisah: 
            res += [tmp]
            tmp  = ''     
        else:
            tmp += ch
    res += [tmp]          
    return res

def csv_list(filename):
    raw = open(filename).read()
    res = []
    for el in parser(raw, '\n'):
        res += [parser(el, ';')]
    return res

os.chdir(os.getcwd() + r'\files')

User = csv_list('user.csv')
Gadget = csv_list('gadget.csv')   
Consumable = csv_list('consumable.csv')
Consum_hist = csv_list('consumable_history.csv')
Gadget_borrow = csv_list('gadget_borrow_history.csv')
Gadget_return = csv_list('gadget_return_history.csv')

