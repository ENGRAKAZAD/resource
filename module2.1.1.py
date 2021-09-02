###marks=['Chem',56,78,'Dhaka',90,56]
##name=['Asik','Kamal','jamal','Motin']
###print(marks.count(56))
##for i in range(len(marks)):
##    if(marks[i])=='Dhaka':
##            marks[i]='Chittagong'
##print(marks)
##marks.app
name_typle=('Asik','Kamal','jamal','Motin')
name_list=list(name_typle)
name_list.append('karim')

name_list.insert(3,'karim')

name_typle=tuple(name_list)
print(name_typle)
