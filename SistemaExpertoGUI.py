import tkinter as tk
from tkinter import ttk, messagebox
from SistemaExperto import BlackjackExpertSystem

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto de Blackjack")
        self.root.geometry("1000x800")
        self.root.configure(bg='#F5F5F5')  # Gris muy claro
        
        # Configurar la expansión de las filas y columnas
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Inicializar el sistema experto
        self.sistema = BlackjackExpertSystem()
        
        # Variables
        self.cartas_jugador = []
        self.carta_dealer = None
        
        # Estilo
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#F5F5F5')
        self.style.configure('TLabel', background='#F5F5F5', foreground='black')
        self.style.configure('TLabelframe', background='#F5F5F5', foreground='black')
        self.style.configure('TLabelframe.Label', background='#F5F5F5', foreground='black')
        self.style.configure('TButton', padding=5, font=('Helvetica', 10))
        
        # Estilos específicos para botones
        self.style.configure('Face.TButton', foreground='#E74C3C')  # Rojo para J, Q, K
        self.style.configure('Ace.TButton', foreground='#2ECC71')   # Verde para As
        self.style.configure('Number.TButton', foreground='black')  # Negro para números
        
        # Crear la interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame principal - configurado para expandirse con la ventana
        main_frame = ttk.Frame(self.root, padding="20", style='TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar la expansión de las filas y columnas del frame principal
        for i in range(5):  # Para las 5 filas principales
            main_frame.rowconfigure(i, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, 
                          text="Sistema Experto de Blackjack",
                          font=('Helvetica', 24, 'bold'),
                          foreground='black',
                          anchor="center")
        titulo.grid(row=0, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))
        
        # Frame para las cartas del jugador
        frame_jugador = ttk.LabelFrame(main_frame, 
                                     text="Cartas del Jugador",
                                     padding="15",
                                     style='TLabelframe')
        frame_jugador.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid en frame_jugador para responsividad
        for i in range(2):  # Para dos filas de botones
            frame_jugador.rowconfigure(i, weight=1)
        for i in range(7):  # Para siete columnas de botones
            frame_jugador.columnconfigure(i, weight=1)
        
        # Botones para las cartas del jugador
        self.crear_botones_cartas(frame_jugador, self.agregar_carta_jugador)
        
        # Frame para la carta del dealer
        frame_dealer = ttk.LabelFrame(main_frame,
                                    text="Carta del Dealer",
                                    padding="15",
                                    style='TLabelframe')
        frame_dealer.grid(row=1, column=1, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid en frame_dealer para responsividad
        for i in range(2):  # Para dos filas de botones
            frame_dealer.rowconfigure(i, weight=1)
        for i in range(7):  # Para siete columnas de botones
            frame_dealer.columnconfigure(i, weight=1)
        
        # Botones para la carta del dealer
        self.crear_botones_cartas(frame_dealer, self.establecer_carta_dealer)
        
        # Frame para mostrar las cartas seleccionadas
        frame_seleccion = ttk.LabelFrame(main_frame,
                                       text="Cartas Seleccionadas",
                                       padding="15",
                                       style='TLabelframe')
        frame_seleccion.grid(row=2, column=0, columnspan=2, pady=15, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid en frame_seleccion para responsividad
        frame_seleccion.columnconfigure(0, weight=1)
        
        self.label_cartas_jugador = ttk.Label(frame_seleccion,
                                            text="Sus cartas: ",
                                            font=('Helvetica', 12),
                                            foreground='black')
        self.label_cartas_jugador.grid(row=0, column=0, pady=5, sticky=(tk.W, tk.E))
        
        self.label_carta_dealer = ttk.Label(frame_seleccion,
                                          text="Carta del dealer: ",
                                          font=('Helvetica', 12),
                                          foreground='black')
        self.label_carta_dealer.grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))
        
        # Frame para la recomendación
        frame_recomendacion = ttk.LabelFrame(main_frame,
                                           text="Recomendación",
                                           padding="15",
                                           style='TLabelframe')
        frame_recomendacion.grid(row=3, column=0, columnspan=2, pady=15, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid en frame_recomendacion para responsividad
        frame_recomendacion.columnconfigure(0, weight=1)
        frame_recomendacion.rowconfigure(0, weight=1)
        frame_recomendacion.rowconfigure(1, weight=1)
        
        self.label_recomendacion = ttk.Label(frame_recomendacion,
                                           text="",
                                           wraplength=900,
                                           font=('Helvetica', 12),
                                           foreground='black')
        self.label_recomendacion.grid(row=0, column=0, pady=5, sticky=(tk.W, tk.E))
        
        self.label_explicacion = ttk.Label(frame_recomendacion,
                                         text="",
                                         wraplength=900,
                                         font=('Helvetica', 12),
                                         foreground='black')
        self.label_explicacion.grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))
        
        # Botones de control
        frame_control = ttk.Frame(main_frame, style='TFrame')
        frame_control.grid(row=4, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid en frame_control para responsividad
        frame_control.columnconfigure(0, weight=1)
        frame_control.columnconfigure(1, weight=1)
        
        # Estilo para botones
        self.style.configure('Action.TButton',
                           font=('Helvetica', 12, 'bold'),
                           padding=10)
        
        ttk.Button(frame_control,
                  text="Evaluar Mano",
                  command=self.evaluar_mano,
                  style='Action.TButton').grid(row=0, column=0, padx=10, sticky=(tk.W, tk.E))
        
        ttk.Button(frame_control,
                  text="Limpiar",
                  command=self.limpiar_mano,
                  style='Action.TButton').grid(row=0, column=1, padx=10, sticky=(tk.W, tk.E))
    
    def crear_botones_cartas(self, parent, command):
        cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i, carta in enumerate(cartas):
            btn = ttk.Button(parent,
                           text=carta,
                           command=lambda c=carta: command(c))
            btn.grid(row=i//7, column=i%7, padx=3, pady=3, sticky=(tk.W, tk.E, tk.N, tk.S))
            
            # Dar estilo a los botones de cartas
            if carta in ['J', 'Q', 'K']:
                btn.configure(style='Face.TButton')
            elif carta == 'A':
                btn.configure(style='Ace.TButton')
            else:
                btn.configure(style='Number.TButton')
    
    def agregar_carta_jugador(self, carta):
        if len(self.cartas_jugador) < 5:  # Límite de 5 cartas
            self.cartas_jugador.append(carta)
            self.actualizar_label_cartas()
        else:
            messagebox.showwarning("Advertencia", "No puede tener más de 5 cartas")
    
    def establecer_carta_dealer(self, carta):
        self.carta_dealer = carta
        self.actualizar_label_cartas()
    
    def actualizar_label_cartas(self):
        cartas_texto = ', '.join(self.cartas_jugador)
        self.label_cartas_jugador.config(
            text=f"Sus cartas: {cartas_texto}",
            foreground='black'
        )
        
        dealer_texto = self.carta_dealer if self.carta_dealer else 'No seleccionada'
        self.label_carta_dealer.config(
            text=f"Carta del dealer: {dealer_texto}",
            foreground='black'
        )
    
    def evaluar_mano(self):
        if not self.cartas_jugador:
            messagebox.showwarning("Advertencia", "Debe seleccionar al menos una carta")
            return
        if not self.carta_dealer:
            messagebox.showwarning("Advertencia", "Debe seleccionar la carta del dealer")
            return
        
        recomendacion, explicacion = self.sistema.evaluar_mano(self.cartas_jugador, self.carta_dealer)
        
        # Actualizar recomendación con estilo
        self.label_recomendacion.config(
            text=f"Recomendación: {recomendacion}",
            foreground='black'
        )
        
        # Actualizar explicación con estilo
        self.label_explicacion.config(
            text=f"Explicación: {explicacion}",
            foreground='black'
        )
        
        # Evaluar seguro si el dealer muestra un As
        if self.carta_dealer == 'A':
            seguro, explicacion_seguro = self.sistema.evaluar_seguro(self.carta_dealer)
            self.label_recomendacion.config(
                text=f"{self.label_recomendacion.cget('text')}\nRecomendación sobre seguro: {seguro}",
                foreground='black'
            )
            self.label_explicacion.config(
                text=f"{self.label_explicacion.cget('text')}\nExplicación del seguro: {explicacion_seguro}",
                foreground='black'
            )
    
    def limpiar_mano(self):
        self.cartas_jugador = []
        self.carta_dealer = None
        self.actualizar_label_cartas()
        self.label_recomendacion.config(text="")
        self.label_explicacion.config(text="")

    def actualizar_wraplength(self, event=None):
        width = self.root.winfo_width() - 100 
        if width > 100:  
            self.label_recomendacion.config(wraplength=width)
            self.label_explicacion.config(wraplength=width)

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    
    root.bind("<Configure>", app.actualizar_wraplength)
    
    root.mainloop()
