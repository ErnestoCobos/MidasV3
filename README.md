# Trading Scalping Terminal

A modern TUI (Terminal User Interface) for scalping trading built with Textual.

## Features
- Real-time price visualization
- Quick buy/sell actions
- Open positions table
- Modern TUI interface
- Dark theme optimized for trading

## Prerequisites

Install `uv` for package management:
```bash
pip install uv
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd terminal_app
```

2. Create and activate virtual environment with uv:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Development Setup

For development, install additional tools:
```bash
uv pip install -r requirements-dev.txt
```

## Usage

Run the application:
```bash
python main.py
```

## Controls
- Use mouse or TAB to navigate
- ENTER to activate buttons
- Q to quit
- CTRL+C for emergency exit

## Project Structure
```
terminal_app/
├── trading_ui/           # UI package
│   ├── components/       # Reusable UI components
│   ├── styles/          # Theme and styles
│   └── app.py           # Main app class
├── main.py              # Entry point
└── requirements.txt     # Dependencies
```

## Contributing
1. Create a virtual environment
2. Install development dependencies
3. Make your changes
4. Run tests
5. Submit a pull request

## License
MIT
