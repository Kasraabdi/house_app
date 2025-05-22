import re
def house_validator(house):
    errors = []
    if not (type(house[0]) == int and house[0]>0):
        errors.append('house ID must be an integer > 0')

    if not (type(house[1]) == int and re.match(r"^[0-9\s]{4}$", house[1])):
        errors.append('House M is Invalid')


    if not (type(house[2]) == int and re.match(r"^[0-9\s]{2}$", house[2])):
        errors.append('House area is Invalid')

    if not (type(house[3]) == str and house[3]>0):
        errors.append('House address must be an string > 0')

    if not (type(house[4]) == str and house[4]>0):
        errors.append('House option must be string > 0')

    if not (type(house[5]) == str and house[5]>0):
        errors.append('House option must be string > 0')

    return errors

