userString = input("String: ")

acronymString = []


x = userString.split()


for eachWord in x:
    # eachWord[0].upper
    acronymString.append(eachWord[0])

acronymString = [x.capitalize() for x in acronymString]
print(''.join(acronymString))
