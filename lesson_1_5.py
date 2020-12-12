revenue = int(input('Please give me your revenue \n')) #ввод выручки
expenses = int(input('Please give me your expenses \n')) #ввод издержек

if expenses > revenue: # выясняем прибыльно предприятие или нет
    print('You are not good for this business')
elif revenue > expenses:
    print('Not bad, not bad. Your profitability is ', (revenue-expenses)/revenue)
    staff=int(input('Now give me the number of your staff'))
    print('For one person profit is  ', (revenue-expenses)/staff)
