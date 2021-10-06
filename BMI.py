age  = int(input("Your age  : "))
#Def
def weightidea(h):
    if 140<=h<142:
        print("Your ideal weight is :30 -39 kg")
    elif 142<=h<144:
        print("Your ideal weight is :33 -40 kg")
    elif 144<=h<147:
        print("Your ideal weight is :35 -44 kg")
    elif 147<=h<150:
        print("Your ideal weight is :38 -46 kg")
    elif 150<=h<152:
        print("Your ideal weight is :40 -50 kg")
    elif 152<=h<155:
        print("Your ideal weight is :43 -53 kg")
    elif 155<=h<157:
        print("Your ideal weight is :45 -55 kg")
    elif 157<=h<160:
        print("Your ideal weight is :48 -59 kg")
    elif 160<=h<162:
        print("Your ideal weight is :50 -61 kg")
    elif 162<=h<165:
        print("Your ideal weight is :53 -65 kg")
    elif 165<=h<168:
        print("Your ideal weight is :56 -68 kg")
    elif 168<=h<170:
        print("Your ideal weight is :58- 70 kg")
    elif 170<=h<173:
        print("Your ideal weight is :60 -74 kg")
    elif 173<=h<175:
        print("Your ideal weight is :63 -76 kg")
    elif 175<=h<178:
        print("Your ideal weight is :65 -80 kg")
    elif 180<=h<183:
        print("Your ideal weight is :70 -85 kg")
    elif 183<=h<184:
        print("Your ideal weight is :72 -89 kg")
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
    print(f"Your BMI : {bmi1}")
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
    print(f"Your BMI : {bmi2}")
    nguoilon = bmiss(bmi2)
    print(nguoilon)
    weightidea(h)