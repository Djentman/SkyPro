lohi = ['tsyba',
        'tsyba',
        'tsyba',
        'tsyba',
        'tsyba',
        'tsyba',
        'tsyba']

totalLohov = len(lohi)

print('У нас есть определенное количество лохов. На данный момент их', totalLohov)

otvet = int(input('сколько всего лохов? '))

if otvet == totalLohov:
    print('да, их 7')
else:
    print('нихуя, их', totalLohov)
