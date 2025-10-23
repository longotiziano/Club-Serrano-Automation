from app.models.resumen import Resumen

class Anulacion:
    """
    Clase para concentrar las anulaciones.
    """
    def __init__(self, monto: float, detalle: str, camarero: str):
        self.monto = monto
        self.detalle = detalle
        self.camarero = camarero