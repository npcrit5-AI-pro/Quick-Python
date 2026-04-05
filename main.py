#!/usr/bin/env python3
"""
Python Runner - A lightweight Python IDE with split-pane layout.
Code editor on the left, output on the right.
Built with tkinter - no external dependencies required.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, simpledialog, filedialog
import sys
import io
import traceback
import threading
import os
import math
import random
import time
import turtle


class CustomInput:
    """Handle input() calls in the GUI environment."""
    
    def __init__(self, root):
        self.root = root
        
    def __call__(self, prompt=""):
        """Show a dialog to get user input."""
        result = [None]
        
        def get_input():
            result[0] = simpledialog.askstring(
                "Input Required", 
                prompt, 
                parent=self.root
            )
        
        self.root.after(0, get_input)
        while result[0] is None:
            self.root.update()
            import time
            time.sleep(0.1)
        return result[0] if result[0] is not None else ""


class PythonRunner:
    """Main application window - Python IDE with split-pane layout."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Python Runner")
        self.root.geometry("1100x650")
        self.root.minsize(800, 500)
        
        # Set app icon if available
        self.gui_input = CustomInput(root)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="5")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(0, 5))
        
        run_btn = ttk.Button(btn_frame, text="▶ Run (Ctrl+Enter)", command=self.run_code)
        run_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        clear_out_btn = ttk.Button(btn_frame, text="Clear Output", command=self.clear_output)
        clear_out_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        clear_editor_btn = ttk.Button(btn_frame, text="Clear Editor", command=self.clear_editor)
        clear_editor_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        save_btn = ttk.Button(btn_frame, text="💾 Save", command=self.save_file)
        save_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        open_btn = ttk.Button(btn_frame, text="📂 Open", command=self.open_file)
        open_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Paned window (split pane)
        paned = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)
        
        # Left frame - Editor
        left_frame = ttk.Frame(paned)
        paned.add(left_frame, weight=1)
        
        editor_label = ttk.Label(left_frame, text="📝 Code Editor", font=("Arial", 10, "bold"))
        editor_label.pack(fill=tk.X, pady=(0, 5))
        
        self.editor = scrolledtext.ScrolledText(
            left_frame,
            font=("Consolas", 11),
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="white",
            wrap=tk.WORD,
            undo=True
        )
        self.editor.pack(fill=tk.BOTH, expand=True)
        
        # Load example or default content
        default_code = '# Python Runner - Quick Test\nprint("Hello, World!")\n\n# Try your own code below\nfor i in range(5):\n    print(f"Count: {i}")\n'
        self.editor.insert(tk.END, default_code)
        
        # Right frame - Output
        right_frame = ttk.Frame(paned)
        paned.add(right_frame, weight=1)
        
        output_label = ttk.Label(right_frame, text="📤 Output", font=("Arial", 10, "bold"))
        output_label.pack(fill=tk.X, pady=(0, 5))
        
        self.output = scrolledtext.ScrolledText(
            right_frame,
            font=("Consolas", 11),
            bg="#1e1e1e",
            fg="#d4d4d4",
            state=tk.DISABLED,
            wrap=tk.WORD
        )
        self.output.pack(fill=tk.BOTH, expand=True)
        
        # Bind keyboard shortcuts
        self.editor.bind("<Control-Return>", lambda e: self.run_code())
        self.editor.bind("<Tab>", self.handle_tab)
        self.editor.bind("<Control-s>", lambda e: self.save_file())
        self.editor.bind("<Control-o>", lambda e: self.open_file())
        
        # Status bar
        self.status = ttk.Label(
            main_frame, 
            text="Ready | Ctrl+Enter: Run | Ctrl+S: Save | Ctrl+O: Open", 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        self.status.pack(fill=tk.X, pady=(5, 0))
        
        # File tracking
        self.current_file = None
        
    def handle_tab(self, event):
        """Handle tab key - insert 4 spaces."""
        self.editor.insert(tk.INSERT, "    ")
        return "break"
    
    def run_code(self):
        """Execute the code in the editor."""
        code = self.editor.get(1.0, tk.END).strip()
        if not code:
            self.show_output("⚠ No code to execute", "orange")
            return
            
        self.status.config(text="Running...")
        self.show_output("\n" + "="*60 + "\n▶ Executing...\n" + "="*60 + "\n", "cyan")
        
        # Run in thread to keep UI responsive
        threading.Thread(target=self._execute, args=(code,), daemon=True).start()
        
    def _execute(self, code):
        """Execute code and capture output."""
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        
        # Backup original input
        builtins_dict = __builtins__ if isinstance(__builtins__, dict) else __builtins__.__dict__
        old_input = builtins_dict.get('input')
        
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()
        
        # Replace input() with our GUI version
        builtins_dict['input'] = self.gui_input
        
        # Check if turtle is used - run on main thread to avoid conflicts
        uses_turtle = "turtle" in code
        
        def run_exec():
            try:
                exec(code, {
                    "__builtins__": __builtins__,
                    "math": math,
                    "random": random,
                    "time": time,
                    "turtle": turtle,
                })
                out = sys.stdout.getvalue()
                err = sys.stderr.getvalue()
                self.root.after(0, self._show_result, out, err)
            except Exception as e:
                err = sys.stderr.getvalue()
                if not err:
                    err = traceback.format_exc()
                out = sys.stdout.getvalue()
                self.root.after(0, self._show_result, out, err)
            finally:
                sys.stdout = old_stdout
                sys.stderr = old_stderr
                builtins_dict['input'] = old_input
        
        if uses_turtle:
            # Run turtle code on main thread
            self.root.after(0, run_exec)
        else:
            # Run normal code in background thread
            t = threading.Thread(target=run_exec, daemon=True)
            t.start()
            
    def _show_result(self, out, err):
        """Display execution results."""
        if out:
            self.show_output(out, "#4CAF50")
        if err:
            self.show_output(err, "#f44336")
        if not out and not err:
            self.show_output("✓ Code executed successfully (no output)", "#888")
        self.status.config(text="Ready | Ctrl+Enter: Run | Ctrl+S: Save | Ctrl+O: Open")
        
    def show_output(self, text, color=None):
        """Append text to output window."""
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, text)
        self.output.see(tk.END)
        self.output.config(state=tk.DISABLED)
        
    def clear_output(self):
        """Clear the output window."""
        self.output.config(state=tk.NORMAL)
        self.output.delete(1.0, tk.END)
        self.output.config(state=tk.DISABLED)
        
    def clear_editor(self):
        """Clear the editor."""
        self.editor.delete(1.0, tk.END)
        self.current_file = None
        self.root.title("Python Runner")
        
    def save_file(self):
        """Save current code to file."""
        from tkinter import filedialog
        code = self.editor.get(1.0, tk.END).strip()
        if not code:
            return
            
        filepath = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")],
            initialfile=self.current_file
        )
        if filepath:
            with open(filepath, 'w') as f:
                f.write(code)
            self.current_file = filepath
            self.root.title(f"Python Runner - {os.path.basename(filepath)}")
            self.show_output(f"✓ Saved to {filepath}\n", "#4CAF50")
        
    def open_file(self):
        """Open a Python file."""
        from tkinter import filedialog
        filepath = filedialog.askopenfilename(
            filetypes=[("Python files", "*.py"), ("All files", "*.*")]
        )
        if filepath:
            with open(filepath, 'r') as f:
                code = f.read()
            self.editor.delete(1.0, tk.END)
            self.editor.insert(tk.END, code)
            self.current_file = filepath
            self.root.title(f"Python Runner - {os.path.basename(filepath)}")
            self.show_output(f"✓ Opened {filepath}\n", "#4CAF50")


def main():
    """Entry point."""
    root = tk.Tk()
    app = PythonRunner(root)
    root.mainloop()


if __name__ == "__main__":
    main()
