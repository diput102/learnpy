def compday():
    Y=int(input('year'))
    M=int(input('Month'))
    D=int(input('day'))
    days1=[31,28,31,30,31,30,31,31,30,31,30,31]
    days2=[31,29,31,30,31,30,31,31,30,31,30,31]
   # i=0
  #  days=0
  #  count=0
    if ((Y%400==0)|(Y%4==0)&(Y%100!=0)):
        print('润')
        for i in range(0,M-1):
            days+=days1[i]
    else:
         print('平')
         for i in range(0,M-1):
             days+=days2[i]
    count=days+D
    return count
         
    
