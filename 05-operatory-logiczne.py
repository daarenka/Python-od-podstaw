from operator import truediv

isSkyBlue = True
isPythonDifficult = False

# print(isSkyBlue and isPythonDifficult) #operator logiczny "and" zwraca True jesli i jedno i drugie jest True
# print(isSkyBlue or isPythonDifficult) #jesli chociaz jedno bedzie True otrzymamy True

a = 5
b = 2

# print(a > b and b > 0)
# print(a > b and b >3)
# print(a > 10 or b > 0)
# print(a > 10 or (b > 0 and a> b))

c = 4
print(c % 2 == 0) # czy jest to liczba parzysta - zwraca True albo False (liczba nieparzysta)

print(not c % 2 == 0) #odwrotna logika - True dla nieparzystej, False dla parzystej

user_logged_in = True
if user_logged_in:
    print("Użytkownik zalogowany")

if not user_logged_in:
    print("Użytkownik niezalogowany")