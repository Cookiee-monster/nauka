from datetime import date, timedelta

days = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

weeks_pattern = {
    "1st": 1,
    "2nd": 8,
    "3rd": 15,
    "4th": 22,
    "5th": 29,
    "teenth": 13
}


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    if week == "last":
        if month == 12:
            meetup_date = date(year+1, 1, 1) - timedelta(days=1)
        else:
            meetup_date = date(year, month + 1, 1) - timedelta(days=1)

        while meetup_date.isoweekday() != days[day_of_week]:
            meetup_date -= timedelta(days=1)
        return meetup_date
    else:
        if month == 2 and week == "5th":
            raise MeetupDayException("There is no 5th week in the month")
        else:
            meetup_date = date(year, month, weeks_pattern[week])
            while meetup_date.isoweekday() != days[day_of_week]:
                meetup_date += timedelta(days=1)
            return date(meetup_date.year, meetup_date.month, meetup_date.day)
