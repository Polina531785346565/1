salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
i = 0
j = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долго
while i < months:
    j = spend - salary + j
    spend = spend * (1 + increase)
    i = i + 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(j))
