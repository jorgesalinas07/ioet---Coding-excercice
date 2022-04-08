""" Asumir:
    * Se deben recibir la información en el formato del ejemplo. 
    Es decir, RENEMO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
    * Un empleado no puede hacer un turno que pertenezca a varias categorias para el mismo día. Es decir,
    que no para un día de la semana no pueda esta en el turno de 00:01 - 09:00 y de 09:01 - 18:00 por ejemplo.
    * No se entrega toda la información si un dato tien un error"""



def read_info():
    """
    Read txt file info

    This function reads the .txt file with all employee information

    Returns two lists with all names and shifts employee's information
    """
    #Corregir la documentación de todos los alterados
    #Revisar por que el tipado estatico no está funcionando
    #Usar el for de esta función para validar la información y que solo pase la información que si está validada. EL resto se queda
    # Por lo tanto, solo se hace el proceso con la info correcta. Se deja un mensaje de error con las informaciones que no cumplen con los criteriors
    with open("./employee_info.txt", mode="r") as f:
        name = []
        shedule_info = []
        first_validate = True
        for general_index, i in enumerate(f):
            found = False
            for index, a in enumerate(i.upper()):
                if a == "=":
                    name.append(i[:index])
                    shedule_info.append(i[index + 1 :])
                    last_shedule_info = i[index + 1 :]
                    found = True
                    break
            try:
                if found == False:
                    raise AssertionError
                elif name_validation( name ) == False:
                    name.pop()
                    shedule_info.pop()
                    raise AssertionError
                elif sintaxis_validation( last_shedule_info ) == False:
                    name.pop()
                    shedule_info.pop()
                    raise AssertionError
                elif shift_validation( i ) == False:
                    name.pop()
                    shedule_info.pop()
                    raise AssertionError
            except AssertionError:
                #first_validate = False
                print("\n")
                print(f'El usuario #{general_index+1} no tiene un formato de horario valido.')
                print("\n")

        return (name, shedule_info, first_validate)


def all_shifts(shedule_info_validation:str):
    bottom = True
    shifts = []
    index = 0
    while bottom:
        shifts.append(shedule_info_validation[index:index+13])
        index +=14
        if len(shedule_info_validation[index:index+13]) == 0:
            bottom = False
    return shifts


def sintaxis_validation(shedule_info_validation):
    #Separar en grupos de 13 el string. Los dos primeros deben ser las letras del ejercicio una después de la que corresponde
    #Se valida que tiene estas letras y si no se eleva error. Después se valida que en la posición _ hay un :. Después se
    #Valida que las posiciónes _ _ _ _ son números. Basta con que una sintasis este mal para no continuar así que en el for
    # Debe haber un break o algo que se salga cuando esto ocurra.
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


def shift_validation(shedule_info):
    return True


def name_validation(name):
    return True

# def validate_info(name,shedule_info):
#     sintax_validation = validate_sintaxis(shedule_info)
#     shift_validation = validate_shift(shedule_info)
#     name_validation = validate_name(name)
#     if sintax_validation == True and shift_validation == True and name_validation == True:
#         return True
#     else:
#         return False


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


def shifts_per_week(shedule_info: str, validation:bool):
    """
    shifts per week

    This function clasify shifts on week and weekends.

    Parameters:
    - shedule_info     -> A list with the worked hours for one employee (weekend and not weekend)

    Returns two lists with worked hours of one employee, one for week hours and other for weekend hours.
    """
    week_shifts = []
    weekend_shifts = []
    all_shifts = []
    for index, i in enumerate(shedule_info):
        if i == "M" and shedule_info[index + 1] == "O":
            week_shifts.append(shedule_info[index + 2 : index + 13])
            all_shifts.append(shedule_info[index : index + 13])
        elif i == "T" and shedule_info[index + 1] == "U":
            week_shifts.append(shedule_info[index + 2 : index + 13])
            all_shifts.append(shedule_info[index : index + 13])
        elif i == "T" and shedule_info[index + 1] == "H":
            week_shifts.append(shedule_info[index + 2 : index + 13])
            all_shifts.append(shedule_info[index : index + 13])
        elif i == "W" and shedule_info[index + 1] == "E":
            week_shifts.append(shedule_info[index + 2 : index + 13])
            all_shifts.append(shedule_info[index : index + 13])
        elif i == "F" and shedule_info[index + 1] == "R":
            week_shifts.append(shedule_info[index + 2 : index + 13])
            all_shifts.append(shedule_info[index : index + 13])
        elif i == "S" and shedule_info[index + 1] == "A":
            weekend_shifts.append(shedule_info[index + 2 : index + 13])
            all_shifts.append(shedule_info[index : index + 13])
        elif i == "S" and shedule_info[index + 1] == "U":
            weekend_shifts.append(shedule_info[index + 2 : index + 13])
            all_shifts.append(shedule_info[index : index + 13])
        # else:
        #     print("Escriba un formato de horario valido")
    if validation == True:
        return all_shifts
    else:
        return week_shifts, weekend_shifts


def calculate_pay(week_shifts: list, weekend_shifts: list):
    """
    Calculate pay

    This function calculates the USD amount to be paid for each employee by using the functions pay_amount and shift_per_week

    Parameters:
    - shedule_info     -> A list with the worked hours for one employee (weekend and not weekend)

    Returns two lists with worked hours of one employee, one for week hours and other for weekend hours.
    """
    week_pay_amount =       pay_amount(weekend_shifts, weekend=True)
    weekend_pay_amount =    pay_amount(week_shifts, weekend=False)
    return week_pay_amount + weekend_pay_amount


if __name__ == "__main__":

    #USAR COMENTARIOS PARA EXPLICAR MEJOR LAS FUNCIONES
    name, shedule_info, first_validate =                 read_info()
    #info_validate =                                      validate_info(name,shedule_info)
    #try:
    #if info_validate and first_validate:
    for actual_name, actual_shedule_info in zip(name, shedule_info):
        week_shift, weekend_shift =     shifts_per_week(actual_shedule_info, validation=False)
        final_pay_amount =              calculate_pay(week_shift, weekend_shift)
        print(f"The amount to pay for {actual_name} is: {final_pay_amount}")
    #     else:
    #         #INTENTAR MOSTRAR UN ERROR MENSSAGE DIFERENTE PARA CADA CASO
    #         raise AssertionError
    # except AssertionError:
    #     print("Uno o mas datos no tiene un formato de horario valido.")
