import os
import re

css_dir = r"c:\Users\ADMIN\Desktop\HTML & JS\meelad_software_0.1\css"

replacements = [
    # Primary colors
    (r"(?i)#7C3AED", "#15803D"),
    (r"(?i)#6D28D9", "#166534"),
    (r"(?i)#5B21B6", "#14532D"),
    (r"(?i)#8B5CF6", "#16A34A"),
    (r"(?i)#A78BFA", "#22C55E"),
    (r"(?i)#4F46E5", "#166534"),
    (r"(?i)#4338CA", "#14532D"),
    (r"(?i)#6366f1", "#16A34A"),
    (r"(?i)#818cf8", "#22C55E"),
    (r"(?i)#a5b4fc", "#DCFCE7"),
    (r"(?i)#c7d2fe", "#F0FDF4"),
    
    # RGBs for primaries
    (r"124,\s*58,\s*237", "21, 128, 61"),
    (r"139,\s*92,\s*246", "22, 163, 74"),
    (r"99,\s*102,\s*241", "21, 128, 61"),
    
    # Neutrals
    (r"(?i)#F8FAFC", "#F6FBF7"),
    (r"(?i)#F1F5F9", "#F0FDF4"),
    (r"(?i)#0F172A", "#17251B"),
    (r"(?i)#64748B", "#64756A"),
    (r"(?i)#94A3B8", "#64756A"),
    (r"(?i)#E2E8F0", "#DDE8E0"),
    (r"(?i)#CBD5E1", "#DDE8E0"),
    (r"(?i)#475569", "#64756A"),
    (r"(?i)#1E293B", "#17251B"),
    (r"(?i)#334155", "#64756A"),
    
    # RGB for neutrals
    (r"15,\s*23,\s*42", "23, 37, 27"),
    
    # Semantics
    (r"(?i)#EF4444", "#DC2626"),
    (r"(?i)#10B981", "#16A34A"),
    (r"(?i)#F59E0B", "#D97706"),
    
    # RGB for semantics
    (r"239,\s*68,\s*68", "220, 38, 38"),
    (r"16,\s*185,\s*129", "22, 163, 74"),
    (r"245,\s*158,\s*11", "217, 119, 6"),
]

css_dir = r"c:\Users\ADMIN\Desktop\HTML & JS\meelad_software_0.1\css"
js_dir = r"c:\Users\ADMIN\Desktop\HTML & JS\meelad_software_0.1\js"
pages_dir = r"c:\Users\ADMIN\Desktop\HTML & JS\meelad_software_0.1\pages"
root_dir = r"c:\Users\ADMIN\Desktop\HTML & JS\meelad_software_0.1"

import glob
files = (
    glob.glob(os.path.join(css_dir, "*.css")) + 
    glob.glob(os.path.join(js_dir, "*.js")) + 
    glob.glob(os.path.join(pages_dir, "*.html")) + 
    glob.glob(os.path.join(root_dir, "*.html"))
)

for filepath in files:
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Specific sidebar replacement for dashboard.css
    if filename == "dashboard.css":
        content = re.sub(r"(\.sidebar\s*\{[^}]*background:\s*)#17251b", r"\1#14532D", content, flags=re.IGNORECASE)
        
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
        
    if filename == "dashboard.css":
        content = re.sub(r"(\.sidebar\s*\{[^}]*background:\s*)#17251B", r"\1#14532D", content, flags=re.IGNORECASE)
        content = re.sub(r"(\.result-fullscreen-modal\s+\.modal-header\s*\{[^}]*background:\s*)#17251B", r"\1#14532D", content, flags=re.IGNORECASE)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Files updated.")
