time = ('Time 1','Time 2','Time 3','Time 4','Time 5','Time 6','Time 7','Time 8','Time 9','Time 10','Time 11','Time 12','Time 13','Time 14','Time 15','Time 16','Time 17','Time 18','Time 19','Time 20')
print('-='*20)
print(f'Lista de times do Brasileirão: {time}')
print('-='*20)
print(f'Os primeiros 5 colocados são {time[:5]}')
print('-='*20)
print(f'Os últimos 4 colocados são {time[16:]}')
print('-='*20)
print(f'Os times em ordem alfabética são: {sorted(time)}')
print('-='*20)
print(f'O {time[6]} está na posição {time.index(time[6])+1}')
print('-='*20)



