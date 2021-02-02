from time import sleep


def maior(*numero):
    print('-' * 30)
    for i in numero:
        print(i, end=' ', flush=True)
    print(f'\nForam passados {len(numero)} valores no total')
    print(f'O maior valor entre eles é {max(numero)}')
    sleep(0.5)


maior(3, 5, 6, 7, 2982, 2938, 3729, 11)
maior(1, 4, 3, 2, 6, 4, 3, 6)
maior(1, 2)
maior(0)
maior(2 + 5 + 8)
