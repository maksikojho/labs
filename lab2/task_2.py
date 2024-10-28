salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # Подушка безопасности

for i in range(10):
    if i == 0:  #В первый месяц повышения цен нет
        money_capital += spend
    else:
        money_capital += spend * (1 + increase)
        spend *= (1 + increase)
    money_capital -= salary


# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
