
# konvertē datu mērvienības
def megabyte_to_megabit(megabyte):
   result = megabyte * 8
   return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):

   result = (100 / kilometers) * litres
   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = (celsius * (9/5)) + 32
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    result = 0
    for x in range(tail + 1):
        result = result + x
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    if (grams < 1000):
        return str(grams) + "g"
    elif (grams < 100000):
        return str(int(grams / 1000)) + "kg"
    elif (grams < 1000000):
        return str(int(grams / 100000)) + "c"
    else:
        return str(int(grams / 1000000)) + "t"