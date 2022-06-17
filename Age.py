#finding age
from datetime import date
birthYear = int(input('Enter Your year '))
#currentYear = 2021
currentYear = date.today().year
Age = currentYear - birthYear
print('yours is here : ',Age)