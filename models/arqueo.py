from models.anulaciones import Anulacion 
from models.gastos import Gasto 
from models.invitaciones import Invitacion 
from models.resumen import Resumen
from models.socios import Socio 
from models.transacciones import Transaccion
from datetime import date

class Arqueo(Resumen):
    """
    Clase donde se almacenan los datos del arqueo.
    """
    def __init__(self, encargado: str, cajero: str):
        super().__init__(date.today(), encargado, cajero)
        
        # Cantidades generales
        self.cantidad_facturado = 0
        self.cantidad_efectivo = 0
        self.cantidad_transaccion = 0
        self.cantidad_anulaciones = 0
        self.cantidad_invitaciones = 0
        self.cantidad_gastos = 0
        self.cantidad_socios = 0
        
        # Registros
        self.registro_tarjetas = []
        self.registro_anulaciones = []
        self.registro_invitaciones = []
        self.registro_gastos = []
        self.registro_socios = []
    
    def actualizar_arqueo(
        self,
        facturado: float = 0,
        efectivo: float = 0,
        transaccion: Transaccion = None,
        anulacion: Anulacion = None,
        invitacion: Invitacion = None,
        gasto: Gasto = None,
        socio: Socio = None,
    ):
        """
        Actualiza el arqueo agregando cantidades y registrando los objetos asociados.
        Todos los parámetros son opcionales; solo se actualiza lo que se pase.
        """
        # Actualizar totales generales
        self.cantidad_facturado += facturado
        self.cantidad_efectivo += efectivo

        # Actualizar y registrar transacciones
        if transaccion:
            self.cantidad_transaccion += transaccion.monto
            self.registro_tarjetas.append(transaccion)

        # Actualizar y registrar anulaciones
        if anulacion:
            self.cantidad_anulaciones += anulacion.monto
            self.registro_anulaciones.append(anulacion)

        # Actualizar y registrar invitaciones
        if invitacion:
            self.cantidad_invitaciones += invitacion.monto
            self.registro_invitaciones.append(invitacion)

        # Actualizar y registrar gastos
        if gasto:
            self.cantidad_gastos += gasto.monto
            self.registro_gastos.append(gasto)

        # Actualizar y registrar socios
        if socio:
            self.cantidad_socios += socio.monto
            self.registro_socios.append(socio)
     
    
    def guardado_de_arqueo(self):
        """
        En esta función realizaré un guardado en Excel del arqueo, que sirva como 
        checkpoint.
        """
        pass
    