from app.models.resumen import Resumen

class Gasto(Resumen):
    """
    Clase para concentrar los gastos diversos necesarios del bar, que abarcan desde pagos de sueldos
    hasta de insumos.
    """
    def __init__(self, monto: float, detalle: str):
        self.monto = monto
        self.detalle = detalle