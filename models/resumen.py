from datetime import date

class Resumen:
    """
    Clase principal donde se almacenan los datos principales del arqueo de caja+
    """
    def __init__(self, fecha: date, encargado: str, cajero: str):
        self.fecha = fecha
        self.encargado = encargado
        self.cajero = cajero
    
        