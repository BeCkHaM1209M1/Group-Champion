age  = int(input("Your age  : "))
#Def
def printideaw(a,b):
    print(f"Your ideal weight is :{a} -{b} kg")
def weightidea(h):
    if 140<=h<142:
        printideaw(30,39)
    elif 142<=h<144:
        printideaw(33,40)
    elif 144<=h<147:
        printideaw(35,44)
    elif 147<=h<150:
        printideaw(38,46)
    elif 150<=h<152:
        printideaw(40,50)
    elif 152<=h<155:
        printideaw(42,53)
    elif 155<=h<157:
        printideaw(45,55)
    elif 157<=h<160:
        printideaw(48,59)
    elif 160<=h<162:
        printideaw(50,61)
    elif 162<=h<165:
        printideaw(53,65)
    elif 165<=h<168:
        printideaw(56,68)
    elif 168<=h<170:
        printideaw(58,70)
    elif 170<=h<173:
        printideaw(60,74)
    elif 173<=h<175:
        printideaw(63,76)
    elif 175<=h<178:
        printideaw(65,80)
    elif 180<=h<183:
        printideaw(75,85)
    elif 183<=h<184:
        printideaw(75,89)
def bmi(a,b):
    c = round(a/((b/100)**2),2)
    return c 
def bmiss(a):
    if 18.5<=a<=24.9:
        return ("Your body is normal") 
    elif 18.5> a:
        return("Your body is underweight")
    elif a ==25:
        return("Your body is overweight")
    elif 25 <a<= 29.9:
        return("Your body is Obesity money")
    elif 30<= a<= 34.9:
        return("Your body is Grade I obesity")
    elif 35<= a <=39.9:
        return("Your body is Grade II obesity")
    elif a ==40:
        return("Your body is Grade III obesity")
print("If you are an infant(age smaller 1), you do not need to enter your height and your weight!")
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
    h= float(input("Height (cm) : "))
    #Công thức chri số lượng cơ thể (BMI)
    bmi1 =bmi(w,h)
    print("{:->40}".format()+f"\n>> Your BMI : {bmi1}\n"+"{:->40}".format())
    treem=bmiss(bmi1)
    print(treem)
    weightidea(h)
elif age >16:
    w= float(input("weight (kg): "))
    h= float(input("Height (cm) : "))
    #Công thức tính cân nặng lý tưởng(KG)
    cnlt=50+0.75*((h*1000)-150)
    print(f"Your ideal weight is : {cnlt} kg ")
    #Công thức chri số lượng cơ thể (BMI)
    bmi2= bmi(w,h)
    print("{:->40}".format()+f"\n>> Your BMI : {bmi2}\n"+"{:->40}".format())
    nguoilon = bmiss(bmi2)
    print(nguoilon)
    weightidea(h)