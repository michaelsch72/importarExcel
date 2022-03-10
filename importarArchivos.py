import numpy
import pandas as pd
import openpyxl
archivo_excel=("/home/santiago/Escritorio/empleado.xlsx")
datos=pd.read_excel(archivo_excel)

print(datos['NOMBRE'])

print(datos['salario'])
#suma
suma_salarios=sum(datos['salario'])
print('el total de los salarios de la base de datos es :',suma_salarios)
#maximo salario
max_salario=max(datos['salario'])
print('el salario mas alto es :',max_salario)

min_salario=min(datos['salario'])
print('el salario mas bajo es :',min_salario)
#promedio 
prom=int(numpy.mean(datos['salario']))
print('el promedio de los salarios es :',prom)
cantidad_datos=len(datos)
prom1=suma_salarios/cantidad_datos
print(prom1)
eps=suma_salarios*(8/100)
print('los aportes de los empleados a eps es :',eps)
pension=suma_salarios*(16/100)
print('los aportes de pension de los empleados es :',pension)
total_aportes=eps+pension
print('el total de los aportes de los empleados es :',total_aportes)
resultados=[('total salario',suma_salarios),('maximo Salario',max_salario),('minimo salario',min_salario),
            ('promedio salario',prom),('cantidad de datos',cantidad_datos),
            ('eps',eps),
            ('pension',pension),
            ('total aportes',total_aportes)]

wb=openpyxl.Workbook()
hoja=wb.active
hoja.append(('titulo','resultados'))
for resultados in resultados:
    hoja.append(resultados)
wb.save('/home/santiago/Escritorio/consulta.xlsx')