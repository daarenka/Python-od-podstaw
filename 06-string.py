name = 'Kasia'
# name = 'Kamil\'s name' # jeśli mamy apostrof "'" w zmiennej to aby nie było blędów musimy użyć przed "\"
#do stringa mozna uzyc "" albo '', do dluższych tesktów raczej "" a do zmiennych '' ale można wymiennie
last_name = 'Brzeziński'
channel_name = ('Jak nauczyć się programowania')
# text = "Bardzo lubię kanał Jak nauczyć się programowania"
# print(name)

# long_text = '''to jest
# bardzo długi
# tekst
# w kilku
# liniach'''
#
# print(long_text)


text = f"Bardzo lubię kanał {channel_name}" #interpolacja stringa dajemy f jesli chcemy uzyc zmiennej{}
print(text)