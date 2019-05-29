from datetime import datetime
import calendar


def add_gigasecond(moment):
    moment_in_future = calendar.timegm(moment.utctimetuple()) + float(10 ** 9)
    return datetime.utcfromtimestamp(moment_in_future)
