class Tarjeta:
    def __init__(self, numero, titular, fecha_expiracion):
        self.numero = numero
        self.titular = titular
        self.fecha_expiracion = fecha_expiracion

    def mostrar_informacion(self):
        print(f"Tarjeta de crédito: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Fecha de expiración: {self.fecha_expiracion}")
    
    def validar_tarjeta(self):
        # Aquí podrías implementar una lógica de validación, como el algoritmo de Luhn
        if len(self.numero) == 16 and self.numero.isdigit():
            return True
        return False
    
    def pagar(self, cantidad):
        if self.validar_tarjeta():
            print(f"Pago de {cantidad} realizado con éxito.")
        else:
            print("Tarjeta no válida. No se pudo realizar el pago.")

class TarjetaDescuento(Tarjeta):
    def __init__(self, numero, titular, fecha_expiracion, descuento):
        super().__init__(numero, titular, fecha_expiracion)
        self.descuento = descuento

    def aplicar_descuento(self, cantidad):
        cantidad_con_descuento = cantidad * (1 - self.descuento)
        print(f"Cantidad original: {cantidad}")
        print(f"Descuento aplicado: {self.descuento * 100}%")
        print(f"Cantidad con descuento: {cantidad_con_descuento}")
        return cantidad_con_descuento
    
    def pagar(self, cantidad):
        cantidad_con_descuento = self.aplicar_descuento(cantidad)
        super().pagar(cantidad_con_descuento)
# Ejemplo de uso
tarjeta1 = Tarjeta("1234567812345678", "Juan Pérez", "12/25")
tarjeta1.mostrar_informacion()
tarjeta1.pagar(100)
tarjeta_descuento = TarjetaDescuento("8765432187654321", "María López", "11/24", 0.15)
tarjeta_descuento.mostrar_informacion()
tarjeta_descuento.pagar(200)

