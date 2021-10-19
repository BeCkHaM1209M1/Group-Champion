age  = int(input("Your age  : "))
#Def
def printideaw(a,b):
    print(f"Your ideal weight is :{a} -{b} kg")
# weightidea của Female
def weightideaF(h):
    if 148<=h<150:
        printideaw(45,49)
    elif 150<=h<152:
        printideaw(46,50)
    elif 152<=h<154:
        printideaw(47,52)
    elif 154<=h<156:
        printideaw(48,53)
    elif 156<=h<158:
        printideaw(49,54)
    elif 158<=h<160:
        printideaw(51,56)
    elif 160<=h<162:
        printideaw(52,57)
    elif 162<=h<164:
        printideaw(53,59)
    elif 164<=h<166:
        printideaw(55,60)
    elif 166<=h<168:
        printideaw(56,62)
    elif 168<=h<170: 
        printideaw(57,63)
    elif 170<=h<172:
        printideaw(59,65)
    elif 172<=h<174:
        printideaw(60,66)
    elif 174<=h<176:
        printideaw(61,67)
    else:
        print("No Data")
# weightidea của Male
def weightideaM(a):
    if 140<=a<142:
        printideaw(30,39)
    elif 142<=a<144:
        printideaw(33,40)
    elif 144<=a<147:
        printideaw(35,44)
    elif 147<=a<150:
        printideaw(38,46)
    elif 150<=a<152:
        printideaw(40,50)
    elif 152<=a<155:
        printideaw(42,53)
    elif 155<=a<157:
        printideaw(45,55)
    elif 157<=a<160:
        printideaw(48,59)
    elif 160<=a<162:
        printideaw(50,61)
    elif 162<=a<165:
        printideaw(53,65)
    elif 165<=a<168:
        printideaw(56,68)
    elif 168<=a<170:
        printideaw(58,70)
    elif 170<=a<173:
        printideaw(60,74)
    elif 173<=a<175:
        printideaw(63,76)
    elif 175<=a<178:
        printideaw(65,80)
    elif 180<=a<183:
        printideaw(75,85)
    elif 183<=a<184:
        printideaw(75,89)
    else:
        print("No Data")
def solo(h):
    sex=input("sex : ").capitalize()
    a= True
    if sex.startswith("Ma")==True:
        weightideaM(h)
    elif sex.startswith("Fe")==True:
        weightideaF(h)
    else :
        while a:
            b=input("Nhap lai sex(Femal or Male): ")
            if b.capitalize().startswith("Ma")==True:
                a = False
                weightideaM(h)
            elif b.capitalize().startswith("Fe")==True:
                a = False
                weightideaF(h)
#Tinh BMI
def bmi(a,b):
    c = round(a/((b/100)**2),2)
    return c 
#Tình trạng 
def bmiss(a):
    if 18.5<=a<=24.9:
        print("Your body is normal") 
    elif 18.5> a:
        print("Your body is underweight")
    elif a ==25:
        print("Your body is overweight")
    elif 25 <a<= 29.9:
        print("Your body is Obesity money")
    elif 30<= a<= 34.9:
        print("Your body is Grade I obesity")
    elif 35<= a <=39.9:
        print("Your body is Grade II obesity")
    elif a ==40:
        print("Your body is Grade III obesity")
    else:
        print("Your are Monster !!")
# print("If you are an infant(age smaller 1), you do not need to enter your height and your weight!")
#Caculator
if age <= 1:
    cnss = float(input("Birth weight (kg) : "))
    stt = int(input("Number of months old : "))
    if stt<=6:
        Infant=cnss + (stt*0.6)
        print(f"Your ideal weight is : {Infant} kg ")
    elif 7 <= stt<= 12:
        baby =cnss+3.6+(0.5*stt)
        print(f"Your ideal weight is : {baby} kg")
elif 2 <= age <=16:
    w= float(input("weight (kg): "))
    a= float(input("Height (cm) : "))
    #Công thức chri số lượng cơ thể (BMI)
    bmi1 =bmi(w,a)
    print("Result".center(30,"-")+f"\n>> Your BMI : {bmi1}\n"+"".ljust(30,"-"))
    
    bmiss(bmi1)
    solo(a)
elif age >16:
    w= float(input("weight (kg): "))
    a= float(input("Height (cm) : "))
    #Công thức chri số lượng cơ thể (BMI)
    bmi2= bmi(w,a)
    print("Result".center(30,"-")+f"\n>> Your BMI : {bmi2}\n"+"".ljust(30,"-"))
    bmiss(bmi2)
    solo(a)
