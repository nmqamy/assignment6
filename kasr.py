num1=int(input('please enter numerator1:'))
deno1=int(input('please enter denominator1:'))
num2=int(input('please enter numerator2:'))
deno2=int(input('please enter denominator2:'))

class fraction:
    def __init__(self,num1,deno1,num2,deno2):
        self.fract1=num1/deno1
        self.fract2=num2/deno2

    def sum(self):
        sum=self.fract1+self.fract2
        print('summation is: ',sum)

    def mul(self):
        mul=self.fract1*self.fract2
        print('multiplication is: ',mul)

    def sub(self):
        sub=self.fract1-self.fract2
        print('subtraction is: ',sub)

    def div(self):
        div=self.fract1/self.fract2
        print('division is: ',div)



while True:
    print('1-sum:')
    print('2-mul:')
    print('3-sub:')
    print('4-div:')
    p=fraction(num1,deno1,num2,deno2)

    n=int(input('please enter ure choose:'))
    if n==1:
        p.sum()
    elif n==2:
        p.mul()
    elif n==3:
        p.sub()
    elif n==4:
        p.div()
    elif n==5:
        exit()
    else:
        print('try again')
