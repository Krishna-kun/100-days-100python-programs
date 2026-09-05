#Project: Smart Unit & Temperature Converter with Precision Handling

def cel_to_ferh(celsius): #celsius to fahrenheit
    ferh=(celsius*9/5)+32
    return ferh 

def ferh_to_cel(fahrenheit): # fahrenheit to celsius
    cel=(ferh-32)*5/9
    return cel

def m_to_cm(meter): # meter to centimeter 
    cm=meter*100
    return cm

def rup_to_dol(ruppee): # ruppees to dollar
    dollar=ruppee/88
    return dollar 

while True:
    print("----MINI CONVERTOR----")
    print("1) celsius to fahrenheit")
    print("2) fahrenheit to celsius")
    print("3) meter to centimeter")
    print("4) ruppees to dollar")
    print("-"*30)
    
    choice=int(input(" Enter your choice(1,2,3,4): "))

    if (choice==1):
        cel=float(input("Enter celsius value: "))
        ferh=cel_to_ferh(cel)
        print("Celsius value in farenhite is:",round(ferh,2))
        input("\nPress enter to continue")

    elif (choice==2):
        ferh=float(input("Enter value in farenhite: "))
        cel=ferh_to_cel(ferh)
        print(" farenhite value in Celsius is:",round(cel,2))
        input("\nPress enter to continue")

    elif (choice==3):
        m=float(input("Enter meter value: "))
        cm=m_to_cm(m)
        print("Meter value in centimeter is:",round(cm,2))
        input("\nPress enter to continue")

    elif (choice==4):
        rup=int(input("Enter ruppees value: "))
        dol=rup_to_dol(rup)
        print("Ruppees in dollars is:",round(dol,2))
        input("\nPress enter to continue")
        

    else:
        print("INVALID INPUT")
        input("\nPress enter to continue")
