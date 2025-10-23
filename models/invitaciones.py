from models.resumen import Resumen
from datetime import date

class Invitacion(Resumen):
    """
    Clase para concentrar las invitaciones.
    """
    def __init__(self, fecha: date, encargado: str, cajero: str, monto: float, detalle: str, camarero: str):
        super().__init__(fecha, encargado, cajero)
        self.monto = monto
        self.detalle = detalle
        self.camarero = camarero