print("Estos son los tipos de producto: \n")
print("A: producto alimenticio")
print("B: producto electrónico")
print("C: Otro")
print("----------")
tipodeproducto=input("Ingrese su tipo de producto: ").upper()
while tipodeproducto!="A" and tipodeproducto!="B" and tipodeproducto!="C":
	tipodeproducto=input("Ingrese su tipo de producto: ").upper()
print("----------")
pesodeproducto=float(input("Ingrese peso del producto en Kg: "))
while pesodeproducto<0:
	pesodeproducto=float(input("Ingrese peso del producto en Kg: "))


print("----------")
fragilrobusto=input("Ingrese 'F' si su producto es frágil, o 'N' en caso contrario: ").upper()
while fragilrobusto!="F" and fragilrobusto!="N":
	fragilrobusto=input("Ingrese 'F' si su producto es frágil, o 'N' en caso contrario: ").upper()

if tipodeproducto=="A":
	if pesodeproducto>=20 and fragilrobusto=="F":
		print("El producto alimenticio es pesado y fragil. Manejar con extremo cuidado.")

	elif pesodeproducto>=10 and fragilrobusto=="F":
		print("El producto alimenticio es de peso mediano y fragil. Manejar con cuidado.")

	elif pesodeproducto<10:
		print("El producto alimenticio es ligero. Manejar con cuidado estándar.")
	 

elif tipodeproducto=="B":
	if fragilrobusto=="F":
		print("Producto electrónico frágil. Manejar con cuidado.")
	else:
		if pesodeproducto>=20:
			print("Producto electrónico pesado y no frágil. Manejar con precaución.")
		else:
			print("Producto electrónico no frágil. Manejo estándar.")

elif tipodeproducto=="C":
	if pesodeproducto>=20:
		if fragilrobusto=="F":
			print("Producto pesado y frágil. Manejar con precaución adicional.")

		else:
			print("Producto pesado y no frágil. Manejo estándar")
	else:
		print("Producto no pesado. Manejo estándar.")
else:
	print("Error. Opción inválida.")
