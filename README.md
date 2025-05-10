# Unidad 3 Tarea 4
# Sistema Experto para Black Jack 21

## Integrantes
### Chaparro Castillo Christopher
### Peñuelas López Luis Antonio

Este proyecto implementa un sistema experto para el juego de Blackjack que proporciona recomendaciones estratégicas basadas en reglas establecidas.

## Descripción

El sistema experto analiza la mano del jugador y la carta visible del dealer para proporcionar la mejor recomendación posible según las estrategas del Blackjack. El sistema puede recomendar las siguientes acciones:
ias básic
- Pedir carta (Hit)
- Plantarse (Stand)
- Doblar apuesta (Double Down)
- Dividir mano (Split)

## Componentes Principales

### Clase BlackjackExpertSystem

La clase principal que implementa la lógica del sistema experto. Sus métodos principales son:

#### `evaluar_mano(cartas_jugador, carta_dealer, es_mano_dividida=False)`
Evalúa la mano del jugador y la carta del dealer para dar una recomendación. Retorna una tupla con la recomendación y su explicación.

#### `_evaluar_division(carta, valor_dealer)`
Evalúa si se debe dividir la mano cuando el jugador tiene un par. Considera:
- Nunca dividir pares de 10s (10, J, Q, K)
- Siempre dividir Ases y 8s
- Dividir 9s contra dealer 2-6, 8
- Dividir 2s, 3s, 7s contra dealer 2-7
- Dividir 6s contra dealer 2-6

#### `_evaluar_mano_con_as(valores, valor_dealer, num_cartas)`
Evalúa manos que contienen un As (manos suaves). Considera:
- Doblar con manos suaves de 2-6 contra dealer 3-6
- Doblar con manos suaves de 7 contra dealer 3-6
- Plantarse con manos suaves de 7 contra dealer 2, 7, 8
- Pedir carta en otros casos

#### `_evaluar_mano_normal(suma, valor_dealer, num_cartas)`
Evalúa manos sin As. Considera:
- Siempre pedir carta con suma ≤ 8
- Doblar con 9 contra dealer 3-6
- Doblar con 10-11 contra dealer 2-9
- Plantarse con 12 contra dealer 4-6
- Plantarse con 13-16 contra dealer 2-6
- Siempre plantarse con 17 o más

#### `evaluar_seguro(carta_dealer)`
Evalúa si se debe tomar seguro cuando el dealer muestra un As. El sistema recomienda no tomar seguro en la mayoría de los casos.

## Interfaz Gráfica

El sistema incluye una interfaz gráfica (`SistemaExpertoGUI.py`) que permite:
- Seleccionar las cartas del jugador
- Seleccionar la carta visible del dealer
- Ver las recomendaciones y explicaciones
- Evaluar múltiples manos

## Uso

1. Ejecutar la interfaz gráfica:
```bash
python3 SistemaExpertoGUI.py
```

2. Seleccionar las cartas del jugador (máximo 5 cartas)
3. Seleccionar la carta visible del dealer
4. Hacer clic en "Evaluar Mano" para obtener la recomendación
5. Usar "Limpiar" para evaluar una nueva mano

### Ejemplo de ejecución

#### Pedir
![image](https://github.com/user-attachments/assets/4e76d978-6c5c-4277-9c2d-3d95b2de59cc)

#### Plantarce

![image](https://github.com/user-attachments/assets/0d79d3f2-eace-4039-a14f-290b8465421c)

#### Doblar

![image](https://github.com/user-attachments/assets/2c0c7beb-e7f0-4a84-b2c9-1b53d16bbacb)

#### Dividir

![image](https://github.com/user-attachments/assets/6dc41e63-955f-4af1-8842-1c2a2a1885c2)

## Reglas Implementadas

El sistema implementa las siguientes reglas estratégicas:
1. **Seguro contra A del dealer**
   - `DealerMuestra(A) ⇒ ¬PagarSeguro`

2. **Dividir A-A**
   - `JugadorTiene(A, A) ⇒ Dividir`

3. **Dividir 9-9 si dealer tiene 2–5 o 7–8; si no, plantarse**
   - `JugadorTiene(9, 9) ∧ (DealerEntre(2, 5) ∨ DealerEntre(7, 8)) ⇒ Dividir`
   - `JugadorTiene(9, 9) ∧ ¬(DealerEntre(2, 5) ∨ DealerEntre(7, 8)) ⇒ Plantarse`

4. **Dividir 8-8**
   - `JugadorTiene(8, 8) ⇒ Dividir`

5. **Dividir 7-7, 2-2, 3-3 si dealer tiene 2–7; si no, pedir**
   - `(JugadorTiene(2, 2), JugadorTiene(3, 3), JugadorTiene(7, 7)) ∧ DealerEntre(2, 7) ⇒ Dividir`
   - `(JugadorTiene(2, 2), JugadorTiene(3, 3), JugadorTiene(7, 7)) ∧ ¬DealerEntre(2, 7) ⇒ Pedir`

6. **Dividir 6-6 si dealer tiene 2–6; si no, pedir**
   - `JugadorTiene(6, 6) ∧ DealerEntre(2, 6) ⇒ Dividir`
   - `JugadorTiene(6, 6) ∧ ¬DealerEntre(2, 6) ⇒ Pedir`

7. **Suma 8 = Pedir**
   - `Suma(8) ⇒ Pedir`

8. **A-2 o A-3 → Doblar si 2 cartas y dealer = 5 o 6; si no, pedir**
   - `As ∧ DosCartas ∧ (Suma(2) ∨ Suma(3)) ∧ DealerEntre(5, 6) ⇒ Doblar`
   - `As ∧ (Suma(2) ∨ Suma(3)) ∧ (¬DosCartas ∨ ¬DealerEntre(5, 6)) ⇒ Pedir`

9. **A-4 o A-5 → Doblar si dealer 4–6 y 2 cartas; si no, pedir**
   - `As ∧ DosCartas ∧ (Suma(4) ∨ Suma(5)) ∧ DealerEntre(4, 6) ⇒ Doblar`
   - `As ∧ (Suma(4) ∨ Suma(5)) ∧ (¬DosCartas ∨ ¬DealerEntre(4, 6)) ⇒ Pedir`

11. **A-6 → Doblar si dealer 3–6 y 2 cartas; si no, pedir**
    - `As ∧ DosCartas ∧ Suma(6) ∧ DealerEntre(3, 6) ⇒ Doblar`
    - `As ∧ ¬DosCartas ∧ Suma(6) ∧ ¬DealerEntre(3, 6) ⇒ Pedir`

13. **A-7 → Doblar si dealer 3–6 y 2 cartas; pedir si dealer 9–A; si no, plantarse**
    - `As ∧ DosCartas ∧ Suma(7) ∧ DealerEntre(3, 6) ⇒ Doblar`
    - `As ∧ Suma(7) ∧ DealerEntre(9, A) ⇒ Pedir`
    - `As ∧ Suma(7) ∧ DealerEntre(2, 8) ⇒ Plantarse`

15. **Suma 9 → Doblar si dealer 3–6 y 2 cartas; si no, pedir**
    - `Suma(9) ∧ DosCartas ∧ DealerEntre(3, 6) ⇒ Doblar`
    - `Suma(9) ∧ ¬DosCartas ∧ DealerEntre(3, 6) ⇒ Pedir`

16. **Suma 10 o 11 → Doblar si dealer 2–9 y 2 cartas; si no, pedir**
    - `(Suma(10) ∨ Suma(11)) ∧ DosCartas ∧ DealerEntre(2, 9) ⇒ Doblar`
    - `(Suma(10) ∨ Suma(11)) ∧ ¬(DosCartas ∨ DealerEntre(2, 9)) ⇒ Pedir`

17. **Suma 12 → Plantarse si dealer 4–6; si no, pedir**
    - `Suma(12) ∧ DealerEntre(4, 6) ⇒ Plantarse`
    - `Suma(12) ∧ ¬DealerEntre(4, 6) ⇒ Pedir`

18. **Suma 13–16 → Plantarse si dealer 2–6; si no, pedir**
    - `SumaEntre(13, 16) ∧ DealerEntre(2, 6) ⇒ Plantarse`
    - `SumaEntre(13, 16) ∧ ¬DealerEntre(2, 6) ⇒ Pedir`

19. **Suma 17–21 → Siempre plantarse**
    - `SumaEntre(17, 21) ⇒ Plantarse`
