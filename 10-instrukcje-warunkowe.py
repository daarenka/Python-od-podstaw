# age = int(input("Ile masz lat? "))
#
# if age >= 18:
#     print("Uzytkownik pełnoletni")
# else:
#     print("Użytkownik niepełnoletni")

light = input("Jakie jest światło? (zielone, żółte, czerwone) ")
if light == "zielone":
    print("Możesz jechać")
elif light == "żółte":
    print("Przygotuj się!")
elif light == "czerwone":
    print("Stój")
else:
    print("Niewłaściwy kolor")