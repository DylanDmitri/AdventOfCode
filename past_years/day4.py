s = '''
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
'''

s = open('data4.txt').read()

passports = s.strip().split('\n\n')


keys = '''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''.strip().split('\n')
keys = [k.split()[0] for k in keys]



fields = []
for p in passports:
    p = p.replace('\n', ' ').strip()

    this = {}
    for field in p.split(' '):
        if not field:
            continue
        k,v = field.split(':')
        this[k] = v

    fields.append(this)


import re

REGEX = {
        'byr': '\d{4}',
        'iyr': '\d{4}',
        'eyr': '\d{4}',
        'hgt': '\d+(in|cm)',
        'hcl': '#([0-9]|[a-f]){6}',
        'ecl': 'amb|blu|brn|gry|grn|hzl|oth',
        'pid': '\d{9}',
        'cid': '.*',
}

def between(s, lower, upper):
    return lower <= int(s) <= upper

def height_ok(s):
    amount, unit = s[:-2], s[-2:]
    if unit == 'cm':
        return between(amount, 150, 193)
    if unit == 'in':
        return between(amount, 59, 76)

VALIDATE = {
        'byr': lambda s: between(s, 1920, 2002),
        'iyr': lambda s: between(s, 2010, 2020),
        'eyr': lambda s: between(s, 2020, 2030),
        'hght': height_ok,
}

def kv_valid(key, value):
    pattern = '^' + REGEX[key] + '$'
    match = re.match(pattern, value)

    if not match: 
        return False

    check = VALIDATE.get(key)
    if check:
        return check(value)

    return True
    
def valid(kvs):

    keys = list(kvs.keys())
    if not any((
        len(keys) == 8,
        len(keys) == 7 and 'cid' not in keys,
        )):
        return False

    print(kvs)
    result =  all(kv_valid(k, v) for k,v in kvs.items())
    
    for k,v in kvs.items():
        if not kv_valid(k, v):
            print(k, v)

    print(result, '\n')
    return result

total = sum(valid(passport) for passport in fields)
print(total)





