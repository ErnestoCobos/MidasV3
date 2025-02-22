from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal, Grid
from textual.widgets import (
    Header, Footer, Static, Button, Label,
    TabbedContent, TabPane, DataTable, Log
)

# -------------------------
# Definimos aquí la clase PriceDisplay (igual que antes)
# -------------------------
class PriceDisplay(Static):
    def __init__(self, label: str, value: str, trend: str = "", classes: str = ""):
        super().__init__(classes="price-display")
        self.label_text = label
        self.value_text = value
        self.trend = trend
        self.classes = classes

    def compose(self) -> ComposeResult:
        with Container():
            yield Static(self.label_text, classes="price-label")
            yield Static(self.value_text, classes=f"price-value {self.trend}")

# -------------------------
# Aquí ajustamos StatsBar
# -------------------------
class StatsBar(Static):
    """Barra de estadísticas personalizada con bloque izquierdo (rendimientos) y derecho (monedas)."""
    def compose(self) -> ComposeResult:
        # Contenedor horizontal principal, ocupa todo el ancho
        with Horizontal(id="stats-bar-content"):
            # Contenedor derecho: BTC, ETH, y lo que quieras
            with Horizontal(classes="stats-right"):
                yield PriceDisplay("BTC", "$45,123", "price-up")
            with Horizontal(classes="stats-right"):
                yield PriceDisplay("ETH", "$3,123", "price-up")
            with Horizontal(classes="stats-right"):
                yield PriceDisplay("24h", "$1,234", "price-up")
            # Contenedor izquierdo: rendimiento diario y semanal
            with Horizontal(classes="stats-left"):
                yield PriceDisplay("Rend. Diario", "+$123.00", "price-up")
            with Horizontal(classes="stats-left"):
                yield PriceDisplay("Rend. Semanal", "+$456.00", "price-up")
                # Si quieres añadir Rend. Mensual, lo agregas aquí:
                # yield PriceDisplay("Rend. Mensual", "+$789.00", "price-up")

# -------------------------
# Resto de tu código
# -------------------------
def create_transaction_table() -> DataTable:
    table = DataTable()
    table.add_columns("Hora", "Tipo", "Precio", "Cantidad", "P/L")
    table.add_rows([
        ("09:15:23", "Compra", "$45,123.45", "0.5 BTC", "-"),
        ("09:10:15", "Venta", "$44,987.65", "0.3 BTC", "+$234.56"),
        ("09:05:30", "Compra", "$44,856.78", "0.3 BTC", "-"),
    ])
    return table

class TradingPanel(Static):
    def compose(self) -> ComposeResult:
        with Vertical():
            with Static(classes="chart"):
                with Horizontal(classes="chart-header"):
                    yield Label("Gráfico de Precios", classes="label")
                    yield PriceDisplay("BTC/USD", "$45,123.45", "price-up")
            
            with Static(classes="tabs-container"):
                with TabbedContent():
                    with TabPane("Transacciones", id="transactions", classes="tab-content"):
                        yield create_transaction_table()
                    with TabPane("Logs del Sistema", id="system-logs", classes="tab-content"):
                        log = Log()
                        for msg in ["[green]Sistema iniciado[/]", "[blue]Conectado[/]"]:
                            log.write(msg)
                        yield log

class SidePanel(Static):
    def compose(self) -> ComposeResult:
        with Vertical(classes="controls"):
            yield Label("Control de Operaciones", classes="label")
            with Vertical():
                yield Label("Tipo de Orden", classes="label")
                with Grid(classes="order-type-grid"):
                    yield Button("Market", variant="primary", id="market-order")
                    yield Button("Limit", id="limit-order")
            
            with Vertical():
                yield Label("Parámetros", classes="label")
                yield PriceDisplay("Precio", "$45,123.45")
                with Grid(classes="input-grid"):
                    yield PriceDisplay("Stop Loss", "$44,500.00")
                    yield PriceDisplay("Take Profit", "$46,000.00")
            
            with Grid(classes="buttons-grid"):
                yield Button("Comprar", variant="primary")
                yield Button("Vender", variant="error")
            
            with Vertical():
                yield Label("Posición", classes="label")
                for label, value, trend in [
                    ("Posición Actual", "0.5 BTC", ""),
                    ("Precio Entrada", "$44,123.45", ""),
                    ("P/L Actual", "+$523.45", "price-up")
                ]:
                    yield PriceDisplay(label, value, trend)

class ScalpingApp(App):
    CSS_PATH = "styles/theme.tcss"  # O bien puedes asignar TRADING_THEME directamente

    def compose(self) -> ComposeResult:
        yield Header(id="header", show_clock=True, icon="💸")
        with Container(id="main-container"):
            yield StatsBar(id="stats-bar")
            with Container(id="content-container"):
                yield TradingPanel(id="main-content")
                yield SidePanel(id="side-panel")
        yield Footer(id="footer")

    def on_mount(self) -> None:
        self.title = "Midas Scalping V3"