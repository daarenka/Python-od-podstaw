# Lista jest uporządkowana, w set za kazdym razem inna kolejnosc
# Set nie pozwala na duplikaty
# Same puste {} to type dictionary a nie set!!!

names = {'Kamil', 'Mariusz', 'Dominik'}
names2 = {'Kamil', 'Paulina', 'Asia', "Rafał"}

# Suma zbiorów - union
# print(names.union(names2))
# #lub
# print(names | names2)

# Część współna - intersection
# print(names.intersection(names2))
# #lub
# print(names & names2)

# Różnica - difference
# print(names.difference(names2))
# print(names - names2)

# Symetryczna różnica - symetric difference
print(names.symmetric_difference(names2))
#lub
print(names ^ names2)

# Jak tworzymy pusty set
names = set()
print(type(names))


# names.add('Rafał')
# names.remove('Mariusz')
# print(names)

# for name in names:
#     print(name)

# names.update({'Adam', 'Rafał'}) # mozna tez dodac w liscie []
# print(names)

