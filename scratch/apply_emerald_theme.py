import os
import re

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

# Global hex replacements (Previous Green to New Emerald)
# We will do a generic hex replace, then refine specific CSS files.
# #15803D -> #047857 (Primary)
# #166534 -> #065F46 (Darker)
# #14532D -> #064E3B (Deep)
# #16A34A -> #059669 (Main)
# #22C55E -> #10B981 (Bright/Success)
# #DCFCE7 -> #D1FAE5 (Soft)
# #F0FDF4 -> #ECFDF5 (Very Soft)
# #F6FBF7 -> #F5FAF7 (Bg)
# #DDE8E0 -> #D8E8DE (Border)

global_replacements = [
    (r"(?i)#15803D", "#047857"),
    (r"(?i)#166534", "#065F46"),
    (r"(?i)#14532D", "#064E3B"),
    (r"(?i)#16A34A", "#059669"),
    (r"(?i)#22C55E", "#10B981"),
    (r"(?i)#DCFCE7", "#D1FAE5"),
    (r"(?i)#F0FDF4", "#ECFDF5"),
    (r"(?i)#F6FBF7", "#F5FAF7"),
    (r"(?i)#DDE8E0", "#D8E8DE"),
    # RGB values
    (r"21,\s*128,\s*61", "4, 120, 87"),  # #047857
    (r"22,\s*163,\s*74", "5, 150, 105"), # #059669
    
    # Old semantics to new semantics (just in case)
    (r"(?i)#DC2626", "#EF4444"), # old danger back to original red
    (r"(?i)#D97706", "#F59E0B"), # old warning back to original orange
]

for filepath in files:
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    for pattern, replacement in global_replacements:
        content = re.sub(pattern, replacement, content)
        
    # Specific styling for dashboard.css
    if filename == "dashboard.css":
        # Sidebar background
        content = re.sub(r"(\.sidebar\s*\{[\s\S]*?background:\s*)[^;]+;", r"\1linear-gradient(180deg, #064E3B 0%, #065F46 100%);", content)
        
        # Sidebar nav active
        active_css = r""".nav-item.active {
    background: rgba(16, 185, 129, 0.18);
    border-color: transparent;
    border-left: 3px solid #34D399;
    color: #ffffff;
    font-weight: 700;
}"""
        content = re.sub(r"\.nav-item\.active\s*\{[\s\S]*?box-shadow:[^}]*\}", active_css, content)
        
        # Sidebar nav icon active
        content = re.sub(r"(\.nav-item\.active\s*\.icon\s*\{\s*color:\s*)[^;]+;", r"\1#34D399;", content)
        
        # Sidebar hover
        content = re.sub(r"(\.nav-item:hover\s*\{\s*background:\s*)[^;]+;", r"\1rgba(16, 185, 129, 0.12);", content)
        
        # Tables header
        table_th_css = r"""\.premium-table th\s*\{[\s\S]*?\}"""
        new_th_css = """.premium-table th {
    background-color: #064E3B;
    color: #ffffff;
    font-weight: 700;
    padding: 1rem 1.25rem;
    border-bottom: 2px solid #065F46;
    text-transform: uppercase;
    font-size: 0.72rem;
    letter-spacing: 0.06em;
}"""
        content = re.sub(table_th_css, new_th_css, content)
        
        # Fullscreen modal header
        content = re.sub(r"(\.result-fullscreen-modal\s+\.modal-header\s*\{\s*background:\s*)[^;]+;", r"\1#064E3B;", content)

    if filename == "style.css":
        # btn-primary background
        content = re.sub(r"(--accent-gradient:\s*)linear-gradient[^;]+;", r"\1linear-gradient(135deg, #059669 0%, #047857 100%);", content)
        content = re.sub(r"(\.btn-primary:not\(:disabled\):hover\s*\{\s*background:\s*)linear-gradient[^;]+;", r"\1linear-gradient(135deg, #10B981 0%, #059669 100%);", content)
        content = re.sub(r"(\.btn-general:not\(:disabled\):hover\s*\{\s*background:\s*)linear-gradient[^;]+;", r"\1linear-gradient(135deg, #10B981 0%, #059669 100%);", content)
        content = re.sub(r"(\.btn-general\s*\{\s*background:\s*)linear-gradient[^;]+;", r"\1linear-gradient(135deg, #059669 0%, #047857 100%);", content)
        
        # Add active state for buttons
        if ".btn-primary:not(:disabled):active" not in content:
            content += "\n.btn-primary:not(:disabled):active { background: #047857; }\n"
        if ".btn-general:not(:disabled):active" not in content:
            content += "\n.btn-general:not(:disabled):active { background: #047857; }\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Emerald theme applied.")
