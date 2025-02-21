from textual.widgets import Static
from textual.reactive import reactive
import random

class PriceWidget(Static):
    """Widget para mostrar precios en tiempo real."""
    value = reactive(0.0)
    
    def on_mount(self) -> None:
        self.update_timer = self.set_interval(1, self.update_price)

    def update_price(self) -> None:
        self.value += random.uniform(-0.5, 0.5)
        self.update(f"${self.value:.2f}")
