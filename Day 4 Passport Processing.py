# validar que cada pasaporte contenga los campos requeridos

def doubleCheck(input):
    doublechecked_passports = 0    

    for item in input:
        validByr = 'byr' in item and 1920 <= int(item["byr"]) <= 2002
        validIyr = 'iyr' in item and 2010 <= int(item["iyr"]) <= 2020
        validEyr = 'eyr' in item and 2020 <= int(item["eyr"]) <= 2030
        validEcl = 'ecl' in item and item['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        if 'hgt' in item and item['hgt'][-2:] == 'cm':
            if 150 <= int(item['hgt'][:-2]) <= 193:
                validHgt = True                
            else:
                validHgt = False
        elif 'hgt' in item and item['hgt'][-2:] == 'in':
            if 59 <= int(item['hgt'][:-2]) <= 76:
                validHgt = True
            else:
                validHgt = False
        else:
            validHgt = False

        if 'hcl' in item and len(item['hcl']) == 7 and item['hcl'][:1] == '#':
            for character in item['hcl'][1:].lower():
                if character not in '0123456789abcdef':
                    validHcl = False
                    break
                else:
                    validHcl = True
        else:
            validHcl = False

        if 'pid' in item and len(item['pid']) == 9:
            for digit in item['pid']:
                if digit in '0123456789':
                    validPid = True
                else:
                    validPid = False
                    break
        else:
            validPid = False

        if (validByr and validEcl and validEyr and validHcl and validHgt and validIyr and validPid):
            doublechecked_passports += 1

    return doublechecked_passports

def checkPassports(passports):
    fields = ['byr', 'iyr','eyr','hgt','hcl','ecl','pid']
    validPassports = 0
    for x in passports:
        if 'cid' not in x:
            if all(elem in x for elem in fields):
                validPassports += 1
        elif all(elem in x for elem in fields):
            validPassports += 1
    return validPassports

def dictionary_convert(pass_list):
    dictionary = {}
    for item in pass_list:
        item = item.split(":")
        key = item[0]
        value = item[1]
        dictionary[key] = value
    return dictionary

with open('./files/day4.txt') as raw_input:
    split_1 = raw_input.read().split('\n\n') # divide cada pasaporte con doble salto de linea
    split_2 = [string.replace('\n',' ') for string in split_1] # reemplaza los salto de linea por espacio
    split_3 = [string.split() for string in split_2] # separa cada item de cada pasaporte
    passports = [dictionary_convert(item) for item in split_3] # transforma la lista en un diccionario
    print('1st solution: ', checkPassports(passports)) # solucion 1
    print('2nd solution: ', doubleCheck(passports)) # solucion 2