from app.models.resumen import Resumen

class Invitacion(Resumen):
    """
    Clase para concentrar las invitaciones.
    """
    def __init__(self, monto: float, detalle: str, camarero: str):
        super().__init__()
        self.monto = monto
        self.detalle = detalle
        self.camarero = camarero