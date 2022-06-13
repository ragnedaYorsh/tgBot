#КАЛЬКУЛЯТОР ИНДЕКСА МАССЫ ТЕЛА

from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.BLACK + "Приветик, добро пожаловать в калькулятор индекса массы тела!")
print(Back.GREEN)

weight = float(input("Какой у Вас вес?: "))
height = float(input("Какой у Вас рост?: "))
print("")

cal = float("{0:.2f}".format(weight / ((height / 100) * (height / 100))))

print(Back.RESET + "Ваш приблизительный индекс массы тела составляет " + str(cal))

if(cal <= 16 ):
	print(Back.RED + "(Выраженный дефицит массы тела)" + "-" + str(cal), end = '')

if(cal >= 16 and cal <= 18.5):
	print(Back.YELLOW + "(Недостаточная (дефицит) масса тела)" + "-" + str(cal), end = '')

if(cal >= 18.5 and cal <= 25):
	print(Back.GREEN + "(Норма)" + "-" + str(cal), end = '')

if(cal >= 25 and cal <= 30):
	print(Back.YELLOW + "(Избыточная масса тела (предожирение))" + "-" + str(cal), end = '')

if(cal >= 30 and cal <= 35):
	print(Back.RED + "(Ожирение 1-ой степени)" + "-" + str(cal), end = '')

if(cal >= 35 and cal <= 40):
	print(Back.RED + "(Ожирение 2-ой степени)" + "-" + str(cal), end = '') 

if(cal >= 40 and cal <= 100):
	print(Back.RED + "(Ожирение 3-ей степени (морбидное))" + "-" + str(cal), end = '')	

input()