[[sd-get-prompt (Native C Version)](https://github.com/ScrapWare/sd-get-prompt)]

---
# SDGP(Stable-Diffusion-Get-Prompt)

Easy display for Stable Diffusion tEXt(Meitu iTXt) Exif data. Anyone can copy and paste from GTK+ dialog.

Sample picture is Japanese language but everybodは can understanding through SD(Stable Diffusion) icon picture on right click menu.

Showing Creation AI Configuration Info.

-----
# Usage (Python Module)

1. Use as Library

```markdown
from sdgp import sdgp

# return dict of iTXt contents
dict = sdgp(path)
```

2. commandline

```markdown
python -m sdgp -i PATH
```
-----
# Usage (Right Clickable)

How to use?

1. Run to python -m sdgp -i *PATH*

-----
## KDE

1. create .desktop file.
2. place to .kde/share/kde4/services/ServiceMenus/

````markdown
[Desktop Entry]  
Version=1.0  
Type=Application  
Name=sd-get-prompt  
Comment=Get tEXt parametor  
Exec=python -m sdgp -i %f
ServiceTypes=KonqPopupMenu/Plugin  
MimeType=image/png  
Icon=applications-graphics  
Path=  
Terminal=false  
StartupNotify=true  
````

& Apply to KDE Dolphin service dir and good changes.

-----
## XFce

1. Add right-click action for thunar(python -m sdgp -i %f)

![sample](https://raw.githubusercontent.com/ScrapWareOrg/sdgp/refs/heads/main/xfce-sample.png)

-----
## Others

for Other wm(window Manager) and file manager.

1. Should be reading your file manager manpages. May be could under run Linux Mint and other Cinnamon distribution and Gnome Nautilus, measure file manager too.

-----
## Microsoft Windows

GLib and GTK+ needed(MingW, CYgwin, Others).
