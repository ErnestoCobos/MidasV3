from textual.widgets import Static, DataTable
from textual.app import ComposeResult

class TradingPosition(Static):
    """Widget para mostrar posiciones abiertas."""
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Símbolo", "Tipo", "Entrada", "SL", "TP", "P/L")
        table.add_row("BTC/USD", "LONG", "41250.00", "41200.00", "41350.00", "+$25.50")
