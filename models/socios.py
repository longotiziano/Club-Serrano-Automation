from models.resumen import Resumen

class Socio(Resumen):
    """
    Clase para concentrar los gastos de socios.
    """
    def __init__(self, fecha, encargado, cajero, monto: float, detalle: str, camarero: str):
        super().__init__(fecha, encargado, cajero)
        self.monto = monto
        self.detalle = detalle
        self.camarero = camarero