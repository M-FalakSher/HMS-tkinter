DEFAULT_FONT = ("Segoe UI", 10)

def apply_default(widget):
    try:
        widget.configure(font=DEFAULT_FONT)
    except Exception:
        pass
