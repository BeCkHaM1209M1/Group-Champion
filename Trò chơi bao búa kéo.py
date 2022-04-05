import random
n= int(input("Nhập số lần chơi : "))
i=0
while True:
    if i==0:
        print("Begin".center(20,"-"),'\n')
    print(f"Game {i+1}")
    print("1: Bao\n2: Búa\n3: Kéo\n4: Exit") #Bảng giá trị
    giatri={1:'Bao',2:"Búa",3:"Kéo",4:"Exit"}
    me= int(input("Nhập số: "))  #Nhap du lieu vao
    #print("Kết quả".center(20,"-"))        #C1
    nguoi=giatri.get(me,'Lỗi')
    if nguoi=="Lỗi":
        print("ERRORS".center(20,"-") ,"\nNo Data\n")
    elif me==4:
        print("End".center(20,"-"),"\nExit....")
        break
    else:
        print("{:-^20}".format("Sự lựa chọn"))  #C2
        print("\nBạn chọn: ",nguoi) #Xác định giá trị chọn
        maytinhdoanso=random.choice([1,2,3])   # Máy Lấy giá trị
        maytinh=giatri.get(maytinhdoanso,"Lỗi")
        print("Máy tính: ",maytinh)
        print("\n{:-^20}".format("Kết quả"))
        if me==maytinhdoanso:  #So sánh
            print("Bạn Hoà\n")
        elif me>maytinhdoanso:
            print('Bạn thua rồi\n')
        else:
            print("Bạn Thắng\n")
        i+=1