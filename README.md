# ioet---Coding-exercise
Coding exercise as part of a python developer position

# Solution provided

The solution was provided by using TDD (test-driven development) and had the following considerations:

    1. The information provided should have the example format which is:
    RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00.
    2. Employes cannot have a shift that belongs to more than one shift category for the same day. So,
    There won't be any users of the 00:01 - 09:00 and de 09:01 shift for the same day.
    3. Employee information will be given only to those who don't have any syntax or shift error.

# Run program locally

Once you pull all files from github, you should click on the employee_info.txt.
This file provides the shifts information of every employee so you should go ahead
and add or remove some. Remember to press enter every time to switch to another
employee. Also, remember the considerations for the input information that is given
in the SOLUTIONS PROVIDED section because it contains the valid information which is
going to be considered.

The next step is to run the python tests on the employeepaid_test.py by using the following
command:

python -m unittest employeepaid_test.py

This will make some tests to the solution provided. Please confirm all tests ran correctly.

The last step is to run the employeepaid.py file. This file contains the business logic of
the coding exercise. If the given information is correct, you will receive an output with all the USD amounts for every employee.

# Explanation of approach

The coding exercise business logic is developed on the employeepaid.py file and it was done by using the TDD. Its
methodology is the following:

    1. The first step is to read the information from the .txt file by the function "read_info". This read includes a
    validation process that discriminates between the correct and incorrect given information. This function only
    returns the information that meets all the requirements.
    The validated errors are:
        * The information provided should have the example format which is:
    RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00.
        * Employes cannot have a shift that belongs to more than one shift category for the same day. So, there won't
    be any user which is the 00:01 - 09:00 and de 09:01 shift for the same day.
    The validation process is done by the function "validate_info" which uses "sintaxis_validation", "shift_validation"
    and "all_shifts". They basically organize the information in an easy format to work with, evaluates the existence of
    some important characters for the syntax (MO, TU, :, =, ...), and confirm if the shift belongs to a valid format.
    For more detail, please feel free to check the documentation and code of each function on the employeepaid.py file.

    2. Once the information is readen, the schedule information is classified within week and weekend by using the
    function "shifts_per_week". It will help in further steps because of the different USD amounts attached to the
    week of the weekend day.

    3. Now the information is classified within week and weekend, "pay_amount" is used to calculate the USD amount by
    taking into account whether it is a week or weekend day and the shift classifies. It returns an addition of total
    USD for every type of fee. It is done by the same function for both, week and weekend, because of their similarities
    on the hour's range, which are:
        00:01 - 09:00, 09:01 - 18:00, 18:01 - 00:00
    However, they are different from the paid tips and that's where the function "calculate_amount" takes place. It
    takes the number of worked hours and calculates the USD amount with the correct week and price type fee for every shift
    of the employee. For more detail, please feel free to check the documentation and code of each function.
