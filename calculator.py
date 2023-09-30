class calculator():
    def __init__(self):
        c=[] #here we have taken list to show performed operations
        a=int(input('enter a value'))
        c.append(a)
        self.a=a
        self.c=c
    def add(self):
        ad=int(input('enter ad value'))
        self.a +=ad
        self.c.append('+')
        self.c.append(ad)
        self.c.append(self.a)
        print(self.a)
    def mul(self):
        into=int(input('enter into value'))
        self.a *=into
        self.c.append('*')
        self.c.append(into)
        self.c.append(self.a)
        print(self.a) 
    def sub(self):
        minus=int(input('enter minus value'))
        self.a -=minus
        self.c.append('-')
        self.c.append(minus)
        self.c.append(self.a)
        print(self.a)
    def div(self):
        dwide=int(input('enter dwide value'))
        self.a /=dwide
        self.c.append('/')
        self.c.append(dwide)
        self.c.append(self.a)
        print(self.a)
    def power(self):
        pow=int(input('enter pow value'))
        self.a **=pow
        self.c.append('**')
        self.c.append(pow)
        self.c.append(self.a)
        print(self.a)
    def operations(self):
        print('initial value',self.c[0])
        #print(self.c)
        for i in range(len(self.c)):
            try:
                if i%3==0:
                    print(self.c[i],self.c[i+1],self.c[i+2],'=',self.c[i+3],sep='')
            except:
                print('final value',self.c[-1])
x=calculator()
while True:
    x1=int(input('1-add() 2-mul() 3-sub() 4-div() 5-power() 6-operations() press any other int to exit'))
    if x1==1:
        x.add()
    elif x1==2:
        x.mul()
    elif x1==3:
        x.sub()
    elif x1==4:
        x.div()
    elif x1==5:
        x.power()
    elif x1==6:
        x.operations()
    else:
        break