# io_de2i.py

import time

class IO:
    def __init__(self):
        self.buttons = [0] * 3  # Simulando 3 botões de pressão (PB0, PB1, PB2)
        self.leds = [0] * 8  # Simulando 8 LEDs (LD0-LD7)
        self.displays = ["0000", "0000"]  # Simulando dois displays de 7 segmentos

    def get_PB(self, index):
        """Simula a leitura do botão de pressão."""
        return self.buttons[index]

    def put_ar_LD(self, values):
        """Simula a atualização dos LEDs."""
        self.leds = values

    def put_DP(self, index, value):
        """Simula a atualização dos displays de 7 segmentos."""
        self.displays[index] = value

    def simulate_button_press(self, index):
        """Método para simular a pressão de um botão (para testes)."""
        self.buttons[index] = 1
        time.sleep(0.1)
        self.buttons[index] = 0

    def simulate_display_update(self):
        """Método para simular a atualização do display (para testes)."""
        print(f"Display {1}: {self.displays[0]}")
        print(f"Display {2}: {self.displays[1]}")
        
    def simulate_led_update(self):
        """Método para simular a atualização dos LEDs (para testes)."""
        print(f"LEDs: {self.leds}")

# Código de teste para verificar a funcionalidade
if __name__ == "__main__":
    io = IO()
    io.simulate_button_press(0)
    print(f"Button 0: {io.get_PB(0)}")  # Espera-se 1 durante o tempo de pressão, depois 0
    io.put_ar_LD([1, 0, 0, 0, 0, 0, 0, 0])
    io.simulate_led_update()
    io.put_DP(0, "1234")
    io.simulate_display_update()
