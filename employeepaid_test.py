import unittest
from employeepaid import (
    calculate_amount,
    calculate_pay,
    shifts_per_week,
    pay_amount,
    shift_validation,
    sintaxis_validation,
    validate_info,
    all_shifts,
)


class TestEmployeePaid(unittest.TestCase):
    """Tests for the employee USD calculate"""

    def test_calculate_pay(self):
        """Confirm user receives the correct amount of USD with the example shifts distribution"""
        # Verificar la manera correctar de los comentarios de los tests
        week_shifts1 = ["10:00-12:00", "10:00-12:00", "01:00-03:00"]
        weekend_shifts1 = ["14:00-18:00", "20:00-21:00"]
        week_shifts2 = ["10:00-12:00", "12:00-14:00"]
        weekend_shifts2 = ["20:00-21:00"]
        self.assertEqual(calculate_pay(week_shifts1, weekend_shifts1), 215)
        self.assertEqual(calculate_pay(week_shifts2, weekend_shifts2), 85)

    def test_shifts_per_week(self):
        """Function should return two list with with shift distribution for week and weekends"""
        shedule_info1 = (
            "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n"
        )
        week_shifts1 = ["10:00-12:00", "10:00-12:00", "01:00-03:00"]
        weekend_shifts1 = ["14:00-18:00", "20:00-21:00"]
        shedule_info2 = "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n"
        week_shifts2 = ["10:00-12:00", "12:00-14:00"]
        weekend_shifts2 = ["20:00-21:00"]
        self.assertEqual(
            shifts_per_week(shedule_info1), (week_shifts1, weekend_shifts1)
        )
        self.assertEqual(
            shifts_per_week(shedule_info2), (week_shifts2, weekend_shifts2)
        )

    def test_pay_amount(self):
        """User should receive a correct USD amount for the week or weekend distribution"""
        shifts1 = ["14:00-18:00", "20:00-21:00"]
        shifts2 = ["10:00-12:00", "10:00-12:00", "01:00-03:00"]
        self.assertEqual(pay_amount(shifts1, weekend=True), 105)
        self.assertEqual(pay_amount(shifts2, weekend=False), 110)

    def test_calculate_amount(self):
        """Confirm USD amount for week and weekend are working"""
        self.assertEqual(calculate_amount(num_hours=1, weekend=True, price_type=1), 30)
        self.assertEqual(calculate_amount(num_hours=1, weekend=True, price_type=2), 20)
        self.assertEqual(calculate_amount(num_hours=1, weekend=True, price_type=3), 25)
        self.assertEqual(calculate_amount(num_hours=1, weekend=False, price_type=1), 25)
        self.assertEqual(calculate_amount(num_hours=1, weekend=False, price_type=2), 15)
        self.assertEqual(calculate_amount(num_hours=1, weekend=False, price_type=3), 20)

    def test_shift_validation(self):
        """User shouldn't be able to place shifts which are out of the standard shedule"""
        shedule_info_validation1 = (
            "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n"
        )
        shedule_info_validation2 = (
            "MO10:00-19:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n"
        )
        self.assertEqual(shift_validation(shedule_info_validation1), True)
        self.assertEqual(shift_validation(shedule_info_validation2), False)

    def test_sintaxis_validation(self):
        """User shouldn't be able to place shifts which have an incorrect sintax"""
        shedule_info_validation1 = (
            "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n"
        )
        shedule_info_validation2 = (
            "M310:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n"
        )
        shedule_info_validation3 = (
            "MO10:00-12:00,TU1000-12:00,T301:00-03:00,SA14:00-18:00,SU20:00-21:00\n"
        )
        shedule_info_validation4 = (
            "tr10:00-12:00,TU1000-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n"
        )
        self.assertEqual(sintaxis_validation(shedule_info_validation1), True)
        self.assertEqual(sintaxis_validation(shedule_info_validation2), False)
        self.assertEqual(sintaxis_validation(shedule_info_validation3), False)
        self.assertEqual(sintaxis_validation(shedule_info_validation4), False)

    def test_validate_info(self):
        """User shouldn't be able to place shifts which has sintax errors, shifts errors or those which don't have '='.
        Those cases should return two list with all names and shedule information except the incorrect employee information"""
        # Correct case
        last_shedule_info1 = (
            "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n"
        )
        name1 = ["RENE"]
        shedule_info1 = [
            "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n"
        ]
        general_index1 = 0
        self.assertEqual(
            validate_info(
                found=True,
                last_shedule_info=last_shedule_info1,
                name=name1,
                shedule_info=shedule_info1,
                general_index=general_index1,
            ),
            (name1, shedule_info1),
        )
        # validate found error ("=" wasn't provided)
        self.assertEqual(
            validate_info(
                found=False,
                last_shedule_info=last_shedule_info1,
                name=name1,
                shedule_info=shedule_info1,
                general_index=general_index1,
            ),
            (name1, shedule_info1),
        )
        # Validate sintax error
        last_shedule_info2 = "3O1000-12:00,T412:00-14:00,SU2000-21:00\n"
        name2 = ["RENE", "ASTRID"]
        shedule_info2 = [
            "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n",
            "3O1000-12:00,T412:00-14:00,SU2000-21:00\n",
        ]
        general_index2 = 1
        self.assertEqual(
            validate_info(
                found=True,
                last_shedule_info=last_shedule_info2,
                name=name2,
                shedule_info=shedule_info2,
                general_index=general_index2,
            ),
            (name1, shedule_info1),
        )
        # Validate shift error
        last_shedule_info3 = "MO10:00-12:00,TH12:00-20:00,SU20:00-21:00\n"
        name3 = ["RENE", "ASTRID"]
        shedule_info3 = [
            "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n",
            "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n",
        ]
        general_index3 = 1
        self.assertEqual(
            validate_info(
                found=True,
                last_shedule_info=last_shedule_info3,
                name=name3,
                shedule_info=shedule_info3,
                general_index=general_index3,
            ),
            (name1, shedule_info1),
        )

    def test_all_shifts(self):
        """Function should return a list with an specific format of information"""
        shedule_info_validation = (
            "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n"
        )
        shifts = [
            "MO10:00-12:00",
            "TU10:00-12:00",
            "TH01:00-03:00",
            "SA14:00-18:00",
            "SU20:00-21:00",
        ]
        self.assertEqual(all_shifts(shedule_info_validation), shifts)
