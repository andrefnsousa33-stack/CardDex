# CardDex
A trading card collection management application currently being developed using **Python** and modern UI libraries.

## Features (so far)
- Graphical User Interface built with **CustomTkinter**.
- File system integration for storing and managing collection data.
- Standardized window structure using a **BaseFrame** system.
- Simple navigation between application screens.

## Project Structure
```text
CardDex/
├── src/
│   ├── frames/      # All 13+ GUI screens (Menu, Adcex, etc.)
│   └── logic/       # Application logic
├── CHANGELOG.md
├── LICENSE
├── main.py          # Application entry point
├── README.md
└── requirements.txt
```
## Installation
1. Clone the repository:
```bash
git clone https://github.com/andrefnsousa33-stack/CardDex.git
cd CardDex
```
2. Create a virtual environment:
```bash
python -m venv .venv
```
3. Activate the virtual environment:
Windows
```powershell
.venv\Scripts\activate
```
Linux / Mac
```bash
source .venv/bin/activate
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
Run the project with:
```bash
python main.py
```

## Project Status
The project is currently **under active development** and new features will be added over time.

## License
This project is licensed under the MIT License.
