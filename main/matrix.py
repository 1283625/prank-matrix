import os
import time

def EnterOS():
	os.system('cls')
	os.system('clear')
	while True:
		os_select = input('Выберите ОС:\n1.Termux\n2.Windows')
		if os_select == '1':
			print('Запускаем скрипт...')
			time.sleep(0.6)
			os.chdir('Termux')
			os.system('python Termux.py')

		elif os_select == '2':
			print('Запускаем скрипт...')
			time.sleep(0.6)
			os.chdir('Windows')
			os.system('py Windows.py')

		else:
			print('Вы не ввели ОС!')
EnterOS()
