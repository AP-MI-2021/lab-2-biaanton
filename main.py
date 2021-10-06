def get_temp(temp,unit1,unit2):
	'''
	Transformam dintr-o scara in alta
	temp reprezinta temperatura data
	unit1 reprezinta scara initiala
	unit2 reprezina scara in care vrem sa transformam temperatura data
	returnam temperatura calculata in scara dorita
	'''
	if unit1=='K':
		if unit2=="C":
			return temp-273.15
		else: return (temp-273.15)*1.8000+32.00
	elif unit1=='C':
		if unit2=='K':
			return temp+273.15
		else: return temp*1.8000+32.00
	elif unit1=='F':
		if unit2=='C':
			return (temp-32)//1.8000
		else: return (temp-32)//1.8000 + 273.15


def get_cmmmc_douanr(param1,param2):
	'''
	Calculam cmmmc-ul dintre doua numere
	param1 este primul numar
	param2 este al doilea numar
	returnam cmmmc ul dintre cele doua numere
	'''
	produs=param1*param2
	while param1!=param2:
		if param1>param2:
			param1=param1-param2
		else:
			param2=param2-param1
	return produs//param1


def get_cmmmc(lst):
	'''
	Calculam cmmmc-ul al n numere date
	returnam cmmmc-ul final
	'''
	cmmmc=lst[0]
	i=1
	for i in range(len(lst)):
		cmmmc=get_cmmmc_douanr(cmmmc,lst[i])
	return cmmmc


def get_prime(numar):
	'''
	Verificam daca un numar este prim
	'''
	if numar<2: return 0
	for i in range(2,numar):
		if numar%i==0: return 0
	return 1

def get_largest_prime_below(numar):
	'''
	Cautam ultimul numar prim mai mic decat numarul dat
	'''
	numar=numar-1
	while numar>1:
		if get_prime(numar)==1:
			return numar
		numar=numar-1

def test_get_temp():
	assert get_temp(300,'K','C') ==26.850000000000023
	assert get_temp(30,'C','F')==86.0
	assert get_temp(90,'F','K')!=900
	assert get_temp(27,'C','F')!=27


def test_get_cmmmc():
	assert get_cmmmc([8,12,20])==120
	assert get_cmmmc([3,6,18])==18


def test_get_largest_prime_below():
	assert get_largest_prime_below(4)==3
	assert get_largest_prime_below(9)==7


def main():
	while True:
		print('1.Transformare temperaturi')
		print('2.Cel mai mic multiplu comun')
		print('3.Ultimul numar prim mai mic decat un numar dat')
		print ('x.Iesire din program')
		optiune=input('Alege optiunea')
		if optiune=='1':
			temperatura_initiala= float(input('Dati temperatura'))
			scara1= str(input('Dati prima scara'))
			scara2= str(input('Dati scara in care vreti sa transformati'))
			temperatura_finala= get_temp(temperatura_initiala,scara1,scara2)
			print(f'Temperatura finala este de {temperatura_finala} grade {scara2}.')
		elif optiune == '2':
			numere_str=input('dati numerele separate prin spatiu')
			numere_str_lst=numere_str.split(' ')
			numere_int_lst= []
			for nr_str in numere_str_lst:
				numere_int_lst.append(int(nr_str))
			cmmmc=get_cmmmc(numere_int_lst)
			print(f'Cel mai mare multiplu comun al listei este {cmmmc}.' )
		elif optiune == '3':
			numar_dat = int(input('Introduceti numarul'))
			numarul_dorit = get_largest_prime_below(numar_dat)
			print(f'Ultimul numar prim mai mic decat {numar_dat} este {numarul_dorit}.')
		elif optiune=='x':
			break


test_get_temp()
test_get_cmmmc()
test_get_largest_prime_below()
main()