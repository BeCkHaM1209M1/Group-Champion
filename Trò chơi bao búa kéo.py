import random
n= int(input("Nhập số lần chơi : "))
i=0
#Bảng giá trị
print("1: Bao\n2: Búa\n3: Kéo")
giatri={1:'Bao',2:"Búa",3:"Kéo"}
while i <n:
    me= int(input("Nhập số: "))
    #print("Kết quả".center(20,"-"))        #C1
    nguoi=giatri.get(me,'Lỗi')
    if nguoi=="Lỗi":
        print("No Data")
    else:
        print("{:-^20}".format("Sự lựa chọn"))  #C2
        #Lấy giá trị
        
        print("\nBạn chọn: ",nguoi)
        maytinhdoanso=random.choice([1,2,3])
        maytinh=giatri.get(maytinhdoanso,"Lỗi")
        print("Máy tính: ",maytinh)

        print("\n{:-^20}".format("Kết quả"))

        #So sánh
        if me==maytinhdoanso:
            print("Hòa")
        elif me>maytinhdoanso:
            print('Bạn thua rồi ')
        else:
            print("Bạn Thắng ")
        i+=1
        if n>=10 and i %5==0:
            a=input("DO you want to stop :(Y or next click) : ").upper()
            if a=='Y':
                break
            elif  a==" ":
                continue