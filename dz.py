def month_to_season(nomer):
    if nomer ==12 or 1<=nomer <=2:
             print("Зима")
    elif 3<=nomer <=5:
             print("Весна")
    elif 6<=nomer <=8:
             print("Лето")
    elif 9<=nomer <=11:
             print("Осень")
    else:
        print("не найдено")
nomer=int(input("Ведите номер месяца -->"))
month_to_season(nomer)
