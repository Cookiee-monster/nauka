import re

def split_elements(date):

    date_regex = re.compile(r'''
    (\d+)       # pierwszy człon daty
    (\W)        # separator
    (\d+)       # drugi człon daty
    (\W)        # separator
    (\d+)       # trzeci człon daty
    
    ''', re.VERBOSE)

    dates_raw = date_regex.search(date)
    return dates_raw

def date_new_format(dates_raw):
    final_date = ''
    if dates_raw:
        if len(dates_raw.group(1)) == 4:
            final_date = "{}.{}.{}".format(dates_raw.group(3), dates_raw.group(5), dates_raw.group(1))

    print(final_date)

def main():
    date = str(input('Podaj datę w dowolnym formacie: '))
    dates_raw = split_elements(date)
    date_new_format(dates_raw)

main()