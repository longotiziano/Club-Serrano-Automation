from models.resumen import Resumen
from datetime import date

class Gasto(Resumen):
    """
    Clase para concentrar los gastos diversos necesarios del bar, que abarcan desde pagos de sueldos
    hasta de insumos.
    """
    def __init__(self, fecha: date, encargado: str, cajero: str, monto: float, detalle: str):
        super().__init__(fecha, encargado, cajero)
        self.monto = monto
        self.detalle = detalle