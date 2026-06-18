Algoritmo pseudocodigoClase2
	
	Definir precio Como Real
	Definir precioDescuento Como Real
	Definir precioFinal Como Real
	
	Escribir 'Ingrese el precio del artículo:'
	Leer precio
	
	precioDescuento <- precio*0.80
	precioFinal <- precioDescuento*1.21
	
	Escribir 'Precio con descuento: ', precioDescuento
	Escribir 'Precio final con IVA: ', precioFinal
FinAlgoritmo
