from datetime import date, timedelta


LABOR_DAY_NAMES = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado")
WEEKDAY_NAME_MAP = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo",
}


def get_day_name(target_date):
    return WEEKDAY_NAME_MAP[target_date.weekday()]


def get_operational_week(reference_date=None):
    current_date = reference_date or date.today()
    week_start = current_date - timedelta(days=current_date.weekday())
    week_end = week_start + timedelta(days=5)
    return week_start, week_end


def is_within_operational_week(target_date, reference_date=None):
    week_start, week_end = get_operational_week(reference_date=reference_date)
    return week_start <= target_date <= week_end
