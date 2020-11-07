import re
s='1 - 2 * ( (60-30 + (-40/5) * (9-2*5/3 + 7/3*99/4*2998 +10 * 568/14 ))-(-4*3)/ (16-3*2))'
#def atom_cal(exp):
#    if '*' in exp:
#        a,b=exp.split('*')
#        return str(float(a) * float(b))
#    elif '/' in exp:
#        a,b=exp.split('/')
#        return str(float(a) / float(b))
#    
#def format_exp(exp):
#    exp=exp.replace('--','+')
#    exp=exp.replace('-+','-')
#    exp=exp.replace('++','+')
#    exp=exp.replace('--','-')
#    return exp
#
#def mul_div(exp):
#    while True:
#        ret=re.search('\d+(\.\d+)?[/*]-?\d+(\.\d+)?',exp)
#        if ret:
#            atom=ret.group()
#            res=atom_cal(atom)
#            exp=exp.replace(atom,res)
#        else:
#            return exp
#        
#def add_sub(exp):
#    ret=re.findall('[+-]?\d+(?:\.\d+)?',exp)
#    num_sum=0
#    for i in ret:
#        num_sum=float(i)+num_sum
#    return num_sum
#
#def cal(exp):
#    exp=mul_div(exp)
#    exp=format_exp(exp)
#    num_sum=add_sub(exp)
#    return num_sum
#
#def main(exp):
#    exp=exp.replace(' ','')
#    while True:
#        ret=re.search("\([^()]+\)",exp)
#        if ret:
#            inner=ret.group()
#            res=str(cal(inner))
#            exp=exp.replace(inner,res)
#            exp=format_exp(exp)
#        else:
#            break
#    return cal(exp)

def atom_cal(exp):
    if '*' in exp:
        a,b=exp.split('*')
        return str(float(a) * float(b))
    elif '/' in exp:
        a,b=exp.split('/')
        return str(float(a) / float(b))

def mul_div(exp):
    while True:
        ret=re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?',exp)
        if ret:
            atom=ret.group()
            res=atom_cal(atom)
            exp=exp.replace(atom,res)
        else:
            return exp

def format_cal(exp):
    exp=exp.replace('++','+')
    exp=exp.replace('--','+')
    exp=exp.replace('+-','-')
    exp=exp.replace('-+','-')
    return exp

def add_cal(exp):
    ret=re.findall('[+-]?\d+(?:\.\d+)?',exp)
    num_sum=0
    for i in ret:
        num_sum+=float(i)
    return num_sum

def cal(exp):
    exp=mul_div(exp)
    exp=format_cal(exp)
    num_sum=add_cal(exp)
    return num_sum

def main(exp):
    exp=exp.replace(' ','')
    while True:
        ret=re.search('\([^()]+\)',exp)
        if ret:
            atom=ret.group(0)
            res=str(cal(atom))
            exp=exp.replace(atom,res)
            exp=format_cal(exp)
        else:
            break
    return cal(exp)

print(main(s))
            
            
            


    
    
    
    
    
    
    
    
    
    










































