def chuoistringint(n):
    b=[]
    for i in n:
        c=int(i)
        b.append(c)
    return b
dayso = input().split()

ktra = False

try:
    danhsachso=chuoistringint(dayso)
    ktra = True
except: 
    print ('Error!')
if ktra:
    print ('tổng dãy số là: ', sum(danhsachso))