#my answer
def g(I):
    b5=10e4*0.1+10e4*0.075+20e4*0.05+20e4*0.03+40e4*0.015
    b4=10e4*0.1+10e4*0.075+20e4*0.05+20e4*0.03
    b3=10e4*0.1+10e4*0.075+20e4*0.05
    b2=10e4*0.1+10e4*0.075
    b1=10e4*0.1
    if I>=100e4:
        b=(I-100e4)*0.01+b5
    elif I>=60e4:
        b=(I-60e4)*0.015+b4
    elif I>=40e4:
        b=(I-40e4)*0.03+b3
    elif I>=20e4:
        b=(I-20e4)*0.05+b2
    elif I>=10e4:
        b=(I-10e4)*0.075+b1
    else:
        b=I*0.1
    print(b)

#standard answer
i=int(input('net profits:'))
arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        #print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)
