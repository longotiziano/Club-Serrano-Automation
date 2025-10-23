from models.resumen_arqueo import Resumen
from typing import Literal

class Transaccion(Resumen):
    """
    Clase en la cual se concentran los atributos y métodos de las tarjetas generales.
    """
    def __init__(
        self, 
        tipo_pago: Literal["mercado_pago", "otros"], 
        num_op: int, 
        monto: float,
        mesa: int,
        camarero: str
        ):
        super().__init__()
        self.tipo_pago = tipo_pago
        self.num_op = num_op    
        self.monto = monto
        self.mesa = mesa
        self.camarero = camarero
        
    def verificar_operacion(self) -> bool:
        """
        Verifica que el número de operación sea correcto
        """
        if self.tipo_pago == "mercado_pago":
            return False if self.num_op != 12 else True
        return 
    
class Tarjeta(Transaccion):
    """
    Especificación para las tarjetas.
    """
    def __init__(self, tipo_tarjeta: str, ultimos_digitos: int):
        super().__init__()  
        self.tipo_tarjeta = tipo_tarjeta
        self.ultimos_digitos = ultimos_digitos

    def verificar_num_tarjeta(self) -> bool:
        """
        Verifica que los últimos dígitos sean correctos
        """
        return False if self.ultimos_digitos != 4 else True
            
class Qr(Transaccion):
    """
    Especificación para los QRs.
    """
    pass
    