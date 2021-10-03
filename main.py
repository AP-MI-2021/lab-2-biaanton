def get_temp(n,unit1,unit2):
	if unit1=='K':
		if unit2=="C":
			return n-273.15
		else: return (n-273.15)*1.8000+32.00
	elif unit1=='C':
		if unit2=='K':
			return n+273.15
		else: return n*1.8000+32.00
	elif unit1=='F':
		if unit2=='C':
			return (n-32)//1.8000
		else: return (n-32)//1.8000 + 273.15
def get_cmmmc_douanr(a,b):
	p=a*b
	while a!=b:
		if a>b:
			a=a-b
		else:
			b=b-a
	return p//a
def get_cmmmc(lst):
	cmmmc=lst[0]
	i=1
	for i in range(len(lst)):
		cmmmc=get_cmmmc_douanr(cmmmc,lst[i])
	return cmmmc
def test_get_temp():
	assert get_temp(300,'K','C') ==26.850000000000023
	assert get_temp(30,'C','F')==86.0
	assert get_temp(90,'F','K')!=900
	assert get_temp(27,'C','F')!=27
def test_get_cmmmc():
	assert get_cmmmc([8,12,20])==120
	assert get_cmmmc([3,6,18])==18
def main():
	while True:
		print('1.Transformare temperaturi')
		print('2.Cel mai mic multiplu comun')
		print ('x.Iesire din program')
		optiune=input('Alege optiunea')
		if optiune=='1':
			temperatura_initiala= float(input('Dati temperatura'))
			scara1= str(input('Dati prima scara'))
			scara2= str(input('Dati scara in care vreti sa transformati'))
			temperatura_finala= get_temp(temperatura_initiala,scara1,scara2)
			print(f'Temperatura finala este de {temperatura_finala} grade {scara2}')
		elif optiune == '2':
			numere_str=input('dati numerele separate prin spatiu')
			numere_str_lst=numere_str.split(' ')
			numere_int_lst= []
			for nr_str in numere_str_lst:
				numere_int_lst.append(int(nr_str))
			cmmmc=get_cmmmc(numere_int_lst)
			print(f'Cel mai mare multiplu comun al listei este {cmmmc}' )
		elif optiune=='x':
			break
test_get_temp()
test_get_cmmmc()
main()