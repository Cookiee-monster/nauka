import re

def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print(is_phone_number('415-555-4242'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print('Phone number found: {} in {}'.format(chunk, message))
print('Done')

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo = phone_num_regex.search(message)
print('Phone number found:  {}'.format(mo.group(1)))
print('Phone number found:  {}'.format(mo.groups()))

regex = re.compile(r'dupa|blada')

mr = regex.findall('Dupa blada blada dupa')
print('{}'.format(mr))

regex = re.compile(r'Bat(man|mobile|copter)')

mr = regex.search("Batwoman, Batcopter, Batman")

print(mr.group())

regex = re.compile(r'(Ha){4,8}')

mr = regex.search("HaHaHaHaHaHa Dupa")
print(mr.group())

regex = re.compile(r'[^a-dA-D]')

mr = regex.findall('Adam ada mamsdsda')
print(mr)

regex = re.compile (r'\d+$')

mr = regex.search('Twój numer to 45')
print(mr.group())