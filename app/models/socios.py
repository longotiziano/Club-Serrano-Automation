from app.models.resumen import Resumen

class Socio(Resumen):
    """
    Clase para concentrar los gastos de socios.
    """
    def __init__(self, monto: float, detalle: str, camarero: str):
        super().__init__()
        self.monto = monto
        self.detalle = detalle
        self.camarero = camarero