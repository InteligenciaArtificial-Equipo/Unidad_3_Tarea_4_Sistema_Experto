class BlackjackExpertSystem:
    def __init__(self):
        self.actions = {
            'PEDIR': 'Pedir carta',
            'PLANTARSE': 'Plantarse',
            'DOBLAR': 'Doblar apuesta',
            'DIVIDIR': 'Dividir mano',
            'SEGURO': 'Tomar seguro',
            'NO_SEGURO': 'No tomar seguro'
        }
        self.explicaciones = {
            'PEDIR': 'La suma de su mano es baja o el dealer tiene una carta fuerte. Es mejor pedir otra carta.',
            'PLANTARSE': 'Tiene una mano fuerte o el dealer tiene una carta débil. Es mejor mantenerse con lo que tiene.',
            'DOBLAR': 'Tiene una buena oportunidad de ganar. Doblar su apuesta maximizará sus ganancias.',
            'DIVIDIR': 'Tiene un par que puede ser dividido para mejorar sus posibilidades de ganar.',
            'SEGURO': 'El dealer muestra un As. Tomar seguro puede proteger su apuesta.',
            'NO_SEGURO': 'Aunque el dealer muestra un As, las probabilidades indican que no es favorable tomar seguro.'
        }

    def evaluar_mano(self, cartas_jugador, carta_dealer, es_mano_dividida=False):
        """
        Evalúa la mano del jugador y la carta del dealer para dar una recomendación.
        
        Args:
            cartas_jugador (list): Lista de cartas del jugador
            carta_dealer (int): Valor de la carta visible del dealer
            es_mano_dividida (bool): Indica si es una mano dividida
        
        Returns:
            tuple: (Recomendación, Explicación)
        """
        # Convertir cartas a valores numéricos
        valores_jugador = [self._convertir_carta(c) for c in cartas_jugador]
        valor_dealer = self._convertir_carta(carta_dealer)
        
        # Verificar si hay As
        tiene_as = 11 in valores_jugador
        
        # Calcular suma de la mano
        suma_mano = sum(valores_jugador)
        
        # Ajustar suma si hay As y se pasa de 21
        if tiene_as and suma_mano > 21:
            suma_mano -= 10
        
        # Verificar si es mano dividida
        if len(cartas_jugador) == 2 and not es_mano_dividida:
            if self._es_par_igual(cartas_jugador):
                accion = self._evaluar_division(cartas_jugador[0], valor_dealer)
                explicacion = f"Tiene un par de {cartas_jugador[0]}s. " + self.explicaciones[accion]
                return self.actions[accion], explicacion
        
        # Evaluar mano con As
        if tiene_as:
            accion = self._evaluar_mano_con_as(valores_jugador, valor_dealer, len(cartas_jugador))
            explicacion = f"Tiene una mano suave (con As) que suma {suma_mano}. " + self.explicaciones[accion]
            return self.actions[accion], explicacion
        
        # Evaluar mano normal
        accion = self._evaluar_mano_normal(suma_mano, valor_dealer, len(cartas_jugador))
        explicacion = f"Su mano suma {suma_mano} y el dealer muestra {carta_dealer}. " + self.explicaciones[accion]
        return self.actions[accion], explicacion

    def _convertir_carta(self, carta):
        """Convierte una carta a su valor numérico."""
        if carta in ['J', 'Q', 'K']:
            return 10
        elif carta == 'A':
            return 11
        return int(carta)

    def _es_par_igual(self, cartas):
        """Verifica si las dos cartas son iguales."""
        return len(cartas) == 2 and cartas[0] == cartas[1]

    def _evaluar_division(self, carta, valor_dealer):
        """Evalúa si se debe dividir la mano."""
        # Si es una carta de valor 10 (10, J, Q, K)
        if carta in ['10', 'J', 'Q', 'K']:
            return 'PLANTARSE'  # Nunca dividir pares de 10s
        
        if carta == 'A':
            return 'DIVIDIR'
        elif carta == '8':
            return 'DIVIDIR'
        elif carta == '9':
            if 2 <= valor_dealer <= 5 or 7 <= valor_dealer <= 8:
                return 'DIVIDIR'
            return 'PLANTARSE'
        elif carta in ['2', '3', '7']:
            if 2 <= valor_dealer <= 7:
                return 'DIVIDIR'
            return 'PEDIR'
        elif carta == '6':
            if 2 <= valor_dealer <= 6:
                return 'DIVIDIR'
            return 'PEDIR'
        return 'PEDIR'

    def _evaluar_mano_con_as(self, valores, valor_dealer, num_cartas):
        """Evalúa una mano que contiene un As."""
        suma = sum(valores)
        if suma > 21:
            suma -= 10
        
        if num_cartas == 2:
            if suma in [2, 3]:
                if 5 <= valor_dealer <= 6:
                    return 'DOBLAR'
            elif suma in [4, 5]:
                if 4 <= valor_dealer <= 6:
                    return 'DOBLAR'
            elif suma == 6:
                if 3 <= valor_dealer <= 6:
                    return 'DOBLAR'
            elif suma == 7:
                if 3 <= valor_dealer <= 6:
                    return 'DOBLAR'
                elif 9 <= valor_dealer <= 11:
                    return 'PEDIR'
                else:
                    return 'PLANTARSE'
        
        return 'PEDIR'

    def _evaluar_mano_normal(self, suma, valor_dealer, num_cartas):
        """Evalúa una mano normal (sin As)."""
        if suma <= 8:
            return 'PEDIR'
        elif suma == 9:
            if num_cartas == 2 and 3 <= valor_dealer <= 6:
                return 'DOBLAR'
            return 'PEDIR'
        elif suma in [10, 11]:
            if num_cartas == 2 and 2 <= valor_dealer <= 9:
                return 'DOBLAR'
            return 'PEDIR'
        elif suma == 12:
            if 4 <= valor_dealer <= 6:
                return 'PLANTARSE'
            return 'PEDIR'
        elif 13 <= suma <= 16:
            if 2 <= valor_dealer <= 6:
                return 'PLANTARSE'
            return 'PEDIR'
        elif suma >= 17:  # 17-21
            return 'PLANTARSE'
        return 'PEDIR'  # Por defecto, pedir carta

    def evaluar_seguro(self, carta_dealer):
        """Evalúa si se debe tomar seguro contra el As del dealer."""
        if carta_dealer == 'A':
            return self.actions['NO_SEGURO'], self.explicaciones['NO_SEGURO']
        return None, None


