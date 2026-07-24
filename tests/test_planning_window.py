import unittest
from datetime import date

from planning_window import get_day_name, get_operational_week, is_within_operational_week


class PlanningWindowTests(unittest.TestCase):
    def test_operational_week_covers_monday_to_saturday(self):
        week_start, week_end = get_operational_week(reference_date=date(2026, 7, 15))

        self.assertEqual(week_start, date(2026, 7, 13))
        self.assertEqual(week_end, date(2026, 7, 18))

    def test_is_within_operational_week_excludes_sunday(self):
        reference_date = date(2026, 7, 15)

        self.assertTrue(is_within_operational_week(date(2026, 7, 13), reference_date=reference_date))
        self.assertTrue(is_within_operational_week(date(2026, 7, 18), reference_date=reference_date))
        self.assertFalse(is_within_operational_week(date(2026, 7, 19), reference_date=reference_date))

    def test_get_day_name_returns_expected_spanish_name(self):
        self.assertEqual(get_day_name(date(2026, 7, 13)), "Lunes")
        self.assertEqual(get_day_name(date(2026, 7, 19)), "Domingo")


if __name__ == "__main__":
    unittest.main()
