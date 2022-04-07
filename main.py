
from array import array
from datetime import datetime
from os import listdir


def read_info():
    """ 
    Read txt file info

    This function reads the .txt file with all employee information

    Returns two lists with all names and shifts employee's information
    """
    with open('./employee_info.txt', mode='r') as f:
        name=[]
        shedule_info=[]
        for i in f:
            for index,a in enumerate(i):
                if a == "=":
                    name.append(i[:index])
                    shedule_info.append(i[index+1:])
                    break
        return(name,shedule_info)

def calculate_amount(num_hours:int, weekend:bool, price_type:int):
    """ 
    Calculate amount

    This function calculates the amount of money depeding on the worked hour's category: 
                00:01 - 09:00 25 USD, 09:01 - 18:00 15 USD, 18:01 - 00:00 20 USD - For week days
                00:01 - 09:00 30 USD, 09:01 - 18:00 20 USD ,18:01 - 00:00 25 USD - For weekends

    Parameters:
    - num_hours     -> A int value with worked hours for one employee
    - weekend       -> A bool value depending wheather it is a weekend shift or not
    - price_type    -> A int value depeding on the worked category mencioned before
    
    Returns the amount of USD depeding on the worked hours (num_hours) and hour value.
    """
    if weekend==False:
        if price_type==1:
            return num_hours*25
        if price_type==2:
            return num_hours*15
        if price_type==3:
            return num_hours*20
    elif weekend:
        if price_type==1:
            return num_hours*30
        if price_type==2:
            return num_hours*20
        if price_type==3:
            return num_hours*25
    else:
        print("Escriba una opción valida")


def pay_amount(shifts:list,weekend:bool):
    """ 
    Pay amount

    This function clasify shifts on the correct range and day of the week according to the following information: 
                00:01 - 09:00, 09:01 - 18:00, 18:01 - 00:00 - For week days
                00:01 - 09:00, 09:01 - 18:00, 18:01 - 00:00 - For weekends
    It also adds the USD amounts on every category by using the function calculate_amount

    Parameters:
    - shifts        -> A list with the weekend or not weekend worked hours for one employee
    - weekend       -> A bool value depending wheather it is a weekend shift or not
    
    Returns a USD addition of all type of hours for the given employee and weekend conditions.
    """
    amount_type1, amount_type2, amount_type3 = [0,0,0]
    for actual_shift in shifts:
        min = int(actual_shift[0:2])
        max = int(actual_shift[6:8])
        num_hours = max-min
        if 0<=min and 9>=max:
            if weekend:
                amount_type1 = amount_type1 + calculate_amount(num_hours, weekend, price_type=1)
            elif weekend==False:
                amount_type1 = amount_type1 + calculate_amount(num_hours, weekend, price_type=1)
            else:
                print("Escriba un opción valida")
        if 9<=min and 18>=max:
            if weekend:
                amount_type2 = amount_type2 + calculate_amount(num_hours, weekend, price_type=2)
            elif weekend==False:
                amount_type2 = amount_type2 + calculate_amount(num_hours, weekend, price_type=2)
            else:
                print("Escriba un opción valida")
        if 18<=min and 24>=max:
            if weekend:
                amount_type3 = amount_type3 + calculate_amount(num_hours, weekend, price_type=3)
            elif weekend==False:
                amount_type3 = amount_type3 + calculate_amount(num_hours, weekend, price_type=3)
            else:
                print("Escriba un opción valida")
    return amount_type1+amount_type2+amount_type3

def shifts_per_week(shedule_info:list):
    """ 
    shifts per week

    This function clasify shifts on week and weekends.

    Parameters:
    - shedule_info     -> A list with the worked hours for one employee (weekend and not weekend)
    
    Returns two lists with worked hours of one employee, one for week hours and other for weekend hours.
    """
    week_shifts = []
    weekend_shifts = []
    for index, i in enumerate(shedule_info):
        if i == "M" and shedule_info[index+1]=="O":
            week_shifts.append(shedule_info[index+2:index+13])
        if i == "T" and shedule_info[index+1]=="U":
            week_shifts.append(shedule_info[index+2:index+13])
        if i == "T" and shedule_info[index+1]=="H":
            week_shifts.append(shedule_info[index+2:index+13])
        if i == "W" and shedule_info[index+1]=="E":
            week_shifts.append(shedule_info[index+2:index+13])
        if i == "F" and shedule_info[index+1]=="R":
            week_shifts.append(shedule_info[index+2:index+13])
        if i == "S" and shedule_info[index+1]=="A":
            weekend_shifts.append(shedule_info[index+2:index+13])
        if i == "S" and shedule_info[index+1]=="U":
            weekend_shifts.append(shedule_info[index+2:index+13])
    return week_shifts, weekend_shifts

#def calculate_pay(shedule_info: list):
def calculate_pay(week_shifts: list, weekend_shifts:list):
    """ 
    Calculate pay

    This function calculates the USD amount to be paid for each employee by using the functions pay_amount and shift_per_week 

    Parameters:
    - shedule_info     -> A list with the worked hours for one employee (weekend and not weekend)
    
    Returns two lists with worked hours of one employee, one for week hours and other for weekend hours.
    """
    #week_shifts, weekend_shifts = shifts_per_week(shedule_info)
    week_pay_amount = pay_amount(weekend_shifts, weekend=True)
    weekend_pay_amount = pay_amount(week_shifts, weekend=False)
    return week_pay_amount+weekend_pay_amount

if __name__=="__main__":
    name, shedule_info = read_info()
    for actual_name, actual_shedule_info in zip(name,shedule_info):
        week_shift, weekend_shift = shifts_per_week(actual_shedule_info)
        #final_pay_amount=calculate_pay(actual_shedule_info)
        final_pay_amount=calculate_pay(week_shift, weekend_shift)
        print(f"The amount to pay for {actual_name} is: {final_pay_amount}")
