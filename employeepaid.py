""" Asumir:
    * Se deben recibir la información en el formato del ejemplo. 
    Es decir, RENEMO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
    * Un empleado no puede hacer un turno que pertenezca a varias categorias para el mismo día. Es decir,
    que no para un día de la semana no pueda esta en el turno de 00:01 - 09:00 y de 09:01 - 18:00 por ejemplo.
    * No se entrega toda la información si un dato tien un error"""


def read_info():
    """
    Read txt file info

    This function reads the .txt file with all employee information and runs some validations

    Returns two lists with all names and shift validated employee's information
    """
    #Revisar por que el tipado estatico no está funcionando
    with open("./employee_info.txt", mode="r") as f:
        name = []
        shedule_info = []
        for general_index, i in enumerate(f):
            found = False
            last_shedule_info = 1
            for index, a in enumerate(i.upper()):
                if a == "=":
                    name.append(i[:index])
                    shedule_info.append(i[index + 1 :])
                    last_shedule_info = i[index + 1 :]
                    found = True
                    break
            name, shedule_info = validate_info(found,last_shedule_info,name,shedule_info, general_index)
        return name, shedule_info


def all_shifts(shedule_info_validation:str):
    """
    All shifts

    This function works to help other funtions. It organizes the shedule information on a formar that can be used easier later

    Parameters:
    - shedule_info_validation       -> A str value with worked hours for one employee. Ej: 'MO10:00-12:00,TU10:00-12:00'

    Returns a list with shedule information about an employee. Ej: [MO10:00-12:00,TU10:00-12:00]
    """
    bottom = True
    shifts = []
    index = 0
    while bottom:
        shifts.append(shedule_info_validation[index:index+13])
        index +=14
        if len(shedule_info_validation[index:index+13]) == 0:
            bottom = False
    return shifts


def validate_info(found:bool,last_shedule_info:str,name:list,shedule_info:list, general_index:int):
    """
    info validation

    This function validates the given information matches with the correct sintax and shift by using the
    sintaxis_validation and shift_validation

    Parameters:
    - found                 -> A bool value depeding on the "=" value is founded where is should be on the input data
    - last_shedule_info     -> A string value with current employee information to analize. Ej: "MO10:00-12:00,TU10:00-12:00" 
    - name                  -> A list value with the names of all employees.
    - shedule_info          -> A list value with worked hours for all employees. Ej: ["MO10:00-12:00,TU10:00-12:00","MO11:00-12:00,TU09:00-12:00"]
    - general_index         -> A int value used to indentify the number of the employee in the list of input data.

    Returns two lists with a validated information. One with currect validated name and other with currect validated shadule info.
    However, if the current employee don't fits with any validation process, it raises an error and prints an error message.
    """
    try:
        if found == False:
            raise AssertionError
        elif sintaxis_validation( last_shedule_info ) == False:
            name.pop()
            shedule_info.pop()
            raise AssertionError
        elif shift_validation( last_shedule_info ) == False:
            name.pop()
            shedule_info.pop()
            raise AssertionError
    except AssertionError:
        print("\n")
        print(f'El usuario #{general_index+1} no tiene un formato de horario valido.')
        print("\n")
    return name,shedule_info
        


def sintaxis_validation(shedule_info_validation:str):
    """
    Sintaxis validation

    This function validates the given information matches with the correct sintax of the input,
    which is the following:
                day of the week(MO, TU, WE...)+range of shift(10:00-12:00),same structure
                
    Parameters:
    - shedule_info_validation       -> A str value with worked hours for one employee. Ej: 'MO10:00-12:00,TU10:00-12:00'

    Returns true or false depeding on wheather sintax is valid or not.
    """
    shifts = all_shifts(shedule_info_validation)
    for i in shifts:
        #Validate ":" was used
        if i[4] != ":" and i[10] != ":":
            return False
        #Validate a valid day was used
        if i[0:2] == "MO":
            next
        elif i[0:2] == "TU":
            next
        elif i[0:2] == "WE":
            next
        elif i[0:2] == "TH":
            next
        elif i[0:2] == "FR":
            next
        elif i[0:2] == "SA":
            next
        elif i[0:2] == "SU":
            next
        else:
            return False
    return True


def shift_validation(shedule_info_validation:str):
    """
    Shift validation

    This function validates the given information matches with ONE of the available worked hour's categorys,
    which are the following:
                00:01 - 09:00, 09:01 - 18:00, 18:01 - 00:00
                
    Parameters:
    - shedule_info_validation       -> A str value with worked hours for one employee. Ej: 'MO10:00-12:00,TU10:00-12:00'

    Returns true or false depeding on wheather shift is valid or not.
    """
    shifts = all_shifts(shedule_info_validation)
    for i in shifts:
        min = int(i[2:4])
        max = int(i[8:10])
        if 0 >= min and max<=9:
            return False
        if 9 <= min and min<=18 and max>18:
            return False
        elif 18 <= min and max>=24:
            return False
    return True


def calculate_amount(num_hours: int, weekend: bool, price_type: int):
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
    if weekend == False:
        if price_type == 1:
            return num_hours * 25
        if price_type == 2:
            return num_hours * 15
        if price_type == 3:
            return num_hours * 20
    elif weekend:
        if price_type == 1:
            return num_hours * 30
        if price_type == 2:
            return num_hours * 20
        if price_type == 3:
            return num_hours * 25
    else:
        print("Escriba una opción valida")


def pay_amount(shifts: list, weekend: bool):
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
    amount_type1, amount_type2, amount_type3 = [0, 0, 0]
    for actual_shift in shifts:
        min = int(actual_shift[0:2])
        max = int(actual_shift[6:8])
        num_hours = max - min
        if 0 <= min and 9 >= max:
            if weekend:
                amount_type1 = amount_type1 + calculate_amount(
                    num_hours, weekend, price_type=1
                )
            elif weekend == False:
                amount_type1 = amount_type1 + calculate_amount(
                    num_hours, weekend, price_type=1
                )
            else:
                print("Escriba un opción valida")
        if 9 <= min and 18 >= max:
            if weekend:
                amount_type2 = amount_type2 + calculate_amount(
                    num_hours, weekend, price_type=2
                )
            elif weekend == False:
                amount_type2 = amount_type2 + calculate_amount(
                    num_hours, weekend, price_type=2
                )
            else:
                print("Escriba un opción valida")
        if 18 <= min and 24 >= max:
            if weekend:
                amount_type3 = amount_type3 + calculate_amount(
                    num_hours, weekend, price_type=3
                )
            elif weekend == False:
                amount_type3 = amount_type3 + calculate_amount(
                    num_hours, weekend, price_type=3
                )
            else:
                print("Escriba un opción valida")
    return amount_type1 + amount_type2 + amount_type3


def shifts_per_week(shedule_info: str):
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
        if i == "M" and shedule_info[index + 1] == "O":
            week_shifts.append(shedule_info[index + 2 : index + 13])
        elif i == "T" and shedule_info[index + 1] == "U":
            week_shifts.append(shedule_info[index + 2 : index + 13])
        elif i == "T" and shedule_info[index + 1] == "H":
            week_shifts.append(shedule_info[index + 2 : index + 13])
        elif i == "W" and shedule_info[index + 1] == "E":
            week_shifts.append(shedule_info[index + 2 : index + 13])
        elif i == "F" and shedule_info[index + 1] == "R":
            week_shifts.append(shedule_info[index + 2 : index + 13])
        elif i == "S" and shedule_info[index + 1] == "A":
            weekend_shifts.append(shedule_info[index + 2 : index + 13])
        elif i == "S" and shedule_info[index + 1] == "U":
            weekend_shifts.append(shedule_info[index + 2 : index + 13])
    else:
        return week_shifts, weekend_shifts


def calculate_pay(week_shifts: list, weekend_shifts: list):
    """
    Calculate pay

    This function calculates the USD amount to be paid for each employee by using the functions pay_amount

    Parameters:
    - week_shifts       -> A list value with all week shedule information for one employee
    - weekend_shifts    -> A list value with all weekend shedule information for one employee 

    Returns two lists with worked hours of one employee. One for week hours and other for weekend hours.
    """
    week_pay_amount =       pay_amount(weekend_shifts, weekend=True)
    weekend_pay_amount =    pay_amount(week_shifts, weekend=False)
    return week_pay_amount + weekend_pay_amount


if __name__ == "__main__":

    #USAR COMENTARIOS PARA EXPLICAR MEJOR LAS FUNCIONES
    name, shedule_info =                 read_info()
    for actual_name, actual_shedule_info in zip(name, shedule_info):
        week_shift, weekend_shift =     shifts_per_week(actual_shedule_info)
        final_pay_amount =              calculate_pay(week_shift, weekend_shift)
        print(f"The amount to pay for {actual_name} is: {final_pay_amount}")
