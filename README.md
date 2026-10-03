# 🐍 Quick Python (Python Runner)

A tiny desktop app for writing and running Python code. Type code on the left, click **▶ Run**, and see the output on the right. It is one file (`main.py`) and needs nothing except Python itself.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

**New to this?** The step-by-step guide is in **[docs/TUTORIAL.md](docs/TUTORIAL.md)**.

## ✨ Features

- **No installs needed:** uses only Python's standard library (`tkinter`)
- **Split screen:** dark-themed code editor on the left, output on the right (drag the divider to resize)
- **Errors shown in the output:** tracebacks appear right under your program's output
- **`input()` works:** a small pop-up window asks for the value
- **Turtle graphics:** code that uses `turtle` runs on the main window thread so drawings work
- **Ready-made imports:** `math`, `random`, `time`, and `turtle` are already available without an `import` line (adding the `import` yourself is fine too)
- **Open and save `.py` files**
- **Keyboard shortcuts:** Ctrl+Enter to run, Ctrl+S to save, Ctrl+O to open, Tab inserts 4 spaces
- **Undo:** Ctrl+Z in the editor

## 🚀 Quick start

You need **Python 3.8+** with **tkinter** (included with the python.org installers for Windows and macOS).

```bash
git clone https://github.com/npcrit5-AI-pro/Quick-Python.git
cd Quick-Python
python main.py
```

Linux users may need tkinter first, for example `sudo apt install python3-tk` (Debian/Ubuntu) or `sudo dnf install python3-tkinter` (Fedora).

## 📖 Using it

| Action | How |
|--------|-----|
| **Run code** | Click `▶ Run (Ctrl+Enter)` or press `Ctrl+Enter` in the editor |
| **Save file** | Click `💾 Save` or press `Ctrl+S` |
| **Open file** | Click `📂 Open` or press `Ctrl+O` |
| **Clear output** | Click `Clear Output` |
| **Clear editor** | Click `Clear Editor` (also forgets the current file name) |
| **Indent** | Press `Tab` (inserts 4 spaces) |
| **Undo** | `Ctrl+Z` |

```
┌─────────────────────────────────────────────────────────────────────┐
│ [▶ Run (Ctrl+Enter)] [Clear Output] [Clear Editor] [💾 Save] [📂 Open] │
├──────────────────────────────┬──────────────────────────────────────┤
│ 📝 Code Editor               │ 📤 Output                            │
│                              │                                      │
│ print("Hello, World!")       │ ====================                 │
│                              │ ▶ Executing...                       │
│                              │ ====================                 │
│                              │ Hello, World!                        │
├──────────────────────────────┴──────────────────────────────────────┤
│ Ready | Ctrl+Enter: Run | Ctrl+S: Save | Ctrl+O: Open               │
└─────────────────────────────────────────────────────────────────────┘
```

A full walkthrough with example programs (including turtle drawing) is in **[docs/TUTORIAL.md](docs/TUTORIAL.md)**.

## ⚙️ Configuration

There are no settings files, environment variables, or API keys. Window size, fonts, and colors are set in `PythonRunner.setup_ui()` in `main.py` if you want to change them.

## 🛠️ How it works

- **GUI:** `tkinter` with a `ttk.PanedWindow` split view
- **Running code:** your code runs with `exec()` in the same Python process as the app. `print` output and errors are captured and shown when the program finishes.
- **Threads:** normal code runs in a background thread so the window stays responsive. If your code contains the word `turtle`, it runs on the main thread instead (turtle requires that).
- **`input()`:** replaced while your code runs with a function that opens a `simpledialog` pop-up

## ⚠️ Good to know

- **Output appears when your program finishes,** not line by line. A program that runs for a long time shows nothing until it ends.
- **There is no Stop button.** An infinite loop keeps running in the background. Close the app window to stop it.
- **Code runs with full access to your computer,** just like running a `.py` file normally. Only run code you trust.
- **Don't press Cancel on an `input()` pop-up.** Cancelling makes the app keep waiting. Type something (even just a space) and press OK.

## 🧯 Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'tkinter'` (or `_tkinter`) | Install tkinter: `sudo apt install python3-tk` (Debian/Ubuntu), `sudo dnf install python3-tkinter` (Fedora), or `brew install python-tk` (Homebrew Python on macOS). The python.org installers already include it. |
| `python` not found | Use `python3 main.py` (macOS/Linux) or `py main.py` (Windows). |
| The app froze after an `input()` prompt | You probably pressed Cancel. Close and reopen the app, and answer prompts with OK. |
| Nothing shows up in Output | Your program may still be running (for example a long loop or `time.sleep`). Wait, or close the app to stop it. |
| The turtle window opens behind the app or stays open | That's normal turtle behavior. Close the turtle window when you're done, or end your code with `turtle.done()`. |

More detail: [docs/TUTORIAL.md#troubleshooting](docs/TUTORIAL.md#troubleshooting).

## 📁 Project structure

```
Quick-Python/
├── main.py           # The whole application
├── requirements.txt  # Notes only. No packages to install
├── LICENSE           # MIT License
└── README.md
```

## 🤝 Contributing

1. Fork the repository
2. Create a branch (`git checkout -b feature/my-idea`)
3. Commit your changes
4. Push and open a Pull Request

Ideas: a Stop button, live (streaming) output, colored error text, syntax highlighting, auto-indent after `:`.

## 📄 License

MIT. See [LICENSE](LICENSE).

## 🐛 Issues & feature requests

Open an [issue](https://github.com/npcrit5-AI-pro/Quick-Python/issues).
