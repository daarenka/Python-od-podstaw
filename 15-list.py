# names = []
names1 = ['Kamil', 'Mariusz', 'Dominika'] ## Lista pozwala na duplikaty
# names1.append('Dominika') # przy pomocy append nie mozeny dodac wiecej niz 1 element
# names1.extend(['Paulina', 'Rafał']) # metoda extend oczekuje listy, wiec elementy musza byc w []
# print(names)
print(names1)


#Podmianka
names1[1] = "Adam"

# print(names1[1])


# WYŚWIETLANIE ELEMENTÓW
# for name in names1:
#     print(name)


# USUWANIE ELEMENTÓW
# del names1[1]
# print(names1)

# names1.remove('Dominika') #Tylko pierwsze wystąpienie będzie usunięte
# print(names1)

print(names1.count('Dominika'))
print(len(names1))
names1.sort()
print(names1)

names1.sort(reverse = True)
print(names1)