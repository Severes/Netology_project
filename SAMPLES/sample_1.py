# первичный ввод данных
wage = int(input('Введите сумму заработной платы в месяц: '))
mortgage = int(input('Введите сколько процентов уходит на ипотеку: '))
life = int(input('Введите сколько процентов уходит на жизнь: '))
bounty = int(input('Введите количество премий за год: '))

# рассчет ипотеки
mortgage_spent = wage * mortgage / 100
# рассчет денег на жизнь
life_spent = wage * life / 100
# рассчет премиальных накоплений
bounty_benefit = wage * bounty / 2
# рассчет накоплений
benefit = wage - mortgage_spent - life_spent

# вывод
print('На ипотеку было потрачено: ', mortgage_spent * 12)
print('Было накоплено:', benefit * 12 + bounty_benefit)
