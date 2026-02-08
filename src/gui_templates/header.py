import tkinter as tk
from tkinter import ttk

# Fuentes del programa
def header(version, root):
    fuente_metsa = ("Helvetica", 24, "bold")
    fuente_version = ("Helvetica", 20, "bold")
    fuente_acronimo = ("Helvetica", 14, "bold")

    header_frame = tk.Frame(root)
    header_frame.grid(
        row = 0,
        column = 0,
        columnspan = 5,
        sticky = "w",
        padx = 20,
        pady = (10, 2)        
    )

    metsa_texto = [
        ("m", "#fff700"),
        ("e", "#e38800"),
        ("t", "#e30000"),  
        ("s", "#89009e"),  
        ("a", "#00129e"),  
        ("V", '#2f8700'),
        ("II", '#ffffff')
    ]

    for char, color in metsa_texto:
        tk.Label(
            header_frame,
            text = char,
            fg = color,
            font = fuente_metsa
        ).pack(side="left")

    tk.Label(
        header_frame,
        text=f"v{version}",
        fg="black",
        font=fuente_version
    ).pack(side="left", padx=(8,0))

    subtitle_label = tk.Label(
        root,
        text="Monitoreando Escaramujo en Telemetría y eStatus con Automatización",
        font=fuente_acronimo,
        fg="black",
        anchor="w",
        justify="left"
    )
    subtitle_label.grid(
        row=1,
        column=0,
        columnspan=5,
        sticky="w",
        padx=20,
        pady=(0, 6)
    )

    separator = ttk.Separator(root, orient="horizontal")
    separator.grid(
        row=2,
        column=0,
        columnspan=5,
        sticky="ew",
        padx=20,
        pady=(0, 15)
    )

    return 2
