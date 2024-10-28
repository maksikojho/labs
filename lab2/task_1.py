money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0 # Сколько месяцев удастся прожить

while money_capital >0:
    money_capital += salary
    money_capital -= spend*(1 + increase)
    spend *= (1+increase)
    month +=1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", month)
