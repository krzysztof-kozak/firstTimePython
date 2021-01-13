name = "kris"
age = 30

print(f'Hello {name}. Your age is {age}\n')

numberArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, value in enumerate(numberArray):
    if (value % 2) == 0:
        print(f'Even value of {value} at index #{index}')
    else:
        print(f'Odd value of {value} at index #{index}')
    if index % 2 != 0:
        print('---\n')


userAge = input("Podaj wiek: ")

if userAge.isdigit():
  if int(userAge) < 5:
    print("A gdzie są twoi rodzice?")

  else:
    ageArray = list(userAge)
    lastDigit = ageArray[len(ageArray)-1]
    ageDescription = 'lat';

    if int(userAge) > 21:
      if lastDigit in ["2", "3", "4"]:
        ageDescription = "lata"

    print(f'Masz {int(userAge)} {ageDescription}')

else:
  print(f'{userAge} nie jest liczbą całkowitą. Musisz podać liczbę całkowitą.')
