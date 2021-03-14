from datetime import datetime


def reverse_interpolate_date(val: datetime, start: datetime, end: datetime):
    start_end_delta = (end-start).total_seconds()
    start_val_delta = (val-start).total_seconds()
    delta = start_val_delta/start_end_delta
    return delta


def interpolate(delta: float, start: float, end: float):
    return start+(end-start)*delta
