# 🐍 Python Runner

No setup, no dependencies, just `python main.py`.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Features

- **🎯 Zero Dependencies** — Built entirely with Python's standard library (`tkinter`)
- **⚡ Instant Setup** — No `pip install` required, just run and go
- **📝 Code Editor** — Dark theme, syntax-friendly, undo support, auto-indent
- **📤 Real-time Output** — Color-coded output (green for stdout, red for errors)
- **💬 Input Support** — `input()` works via popup dialogs
- **💾 File Operations** — Open and save `.py` files
- **⌨️ Keyboard Shortcuts** — Efficient workflow with hotkeys

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher (comes with `tkinter` built-in)

### Run

```bash
python main.py
```

That's it. No installation needed.

## 📖 Usage

| Action | Method |
|--------|--------|
| **Run Code** | Click `▶ Run` or press `Ctrl+Enter` |
| **Save File** | Click `💾 Save` or press `Ctrl+S` |
| **Open File** | Click `📂 Open` or press `Ctrl+O` |
| **Clear Output** | Click `Clear Output` |
| **Clear Editor** | Click `Clear Editor` |
| **Indent** | Press `Tab` (inserts 4 spaces) |

## 🎨 Interface

```
┌─────────────────────────────────────────────────────────────┐
│  [▶ Run] [Clear Output] [Clear Editor] [💾 Save] [📂 Open]  │
├──────────────────────────┬──────────────────────────────────┤
│  📝 Code Editor          │  📤 Output                       │
│                          │                                  │
│  print("Hello, World!")  │  Hello, World!                   │
│                          │                                  │
│                          │                                  │
│                          │                                  │
└──────────────────────────┴──────────────────────────────────┘
```

## 🧪 Example Code

Try these in the editor:

### Hello World
```python
print("Hello, World!")
```

### User Input
```python
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")
```

### Math & Loops
```python
for i in range(1, 6):
    print(f"{i}² = {i**2}")
```

### Error Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught error: {e}")
```

## 🛠️ Technical Details

- **GUI Framework**: `tkinter` (Python standard library)
- **Code Execution**: `exec()` with captured `stdout`/`stderr`
- **Threading**: Background execution keeps UI responsive
- **Input Handling**: Custom `input()` override with dialog popup

## 📁 Project Structure

```
pyruner/
├── main.py           # Main application
├── README.md         # This file
├── requirements.txt  # Empty — no dependencies needed!
└── LICENSE           # MIT License
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🐛 Issues & Feature Requests

Found a bug or have a feature idea? Open an [issue](https://github.com/yourusername/python-runner/issues) on GitHub.

---

Made with ❤️ using Python's built-in tools
