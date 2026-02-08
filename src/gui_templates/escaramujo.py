import tkinter as tk
from tkinter import ttk

def escaramujo(i, root, data_ref, update_interval):


    fuente_ID = ("Helvetica", 16, "bold")
    fuente_titulo = ("Helvetica", 16, "bold")
    fuente_name_canales = ("Helvetica", 12, "bold")
    fuente_valores = ("Helvetica", 14)


    ID_label = ttk.Label(
        root,
        text="ID de adquisición: --",
        font=fuente_ID
    )
    ID_label.grid(
        row=i + 1, column=0, columnspan=5,
        sticky="w", padx=20, pady=5
    )


    title_label = ttk.Label(
        root,
        text="Conteo actual de eventos",
        font=fuente_titulo,
        anchor="center"
    )
    title_label.grid(
        row=i + 2, column=0, columnspan=5,
        sticky="w", padx=20, pady=5
    )


    column_titles = [
        "Canal 0",
        "Canal 1",
        "Canal 2",
        "Canal 3",
        "Coincidencias"
    ]

    for col, title in enumerate(column_titles):
        lbl = ttk.Label(
            root,
            text=title,
            font=fuente_name_canales,
            anchor="center"
        )
        lbl.grid(row=i + 3, column=col, padx=20, pady=5)


    value_labels = []

    for col in range(5):
        frame = tk.Frame(
            root,
            background="white",
            relief="solid",
            borderwidth=1
        )
        frame.grid(
            row=i + 4, column=col,
            padx=20, pady=0,
            sticky="nsew"
        )

        label = tk.Label(
            frame,
            text="--",
            font=fuente_valores,
            background="white",
            width=10,
            anchor="center"
        )
        label.pack(padx=10, pady=10)

        value_labels.append(label)

    read_label = ttk.Label(
        root,
        text="Última lectura (UTC):",
        font=fuente_titulo,
        anchor="center"
    )
    read_label.grid(
        row=i + 5, column=2, columnspan=2,
        sticky="e", padx=20, pady=20
    )

    read_data_label = ttk.Label(
        root,
        text="--",
        font=fuente_valores,
        anchor="center"
    )
    read_data_label.grid(
        row=i + 5, column=4, columnspan=1,
        sticky="w", padx=20, pady=20
    )


    update_label = ttk.Label(
        root,
        text="Última actualización (UTC):",
        font=fuente_titulo,
        anchor="center"
    )
    update_label.grid(
        row=i + 6, column=2, columnspan=2,
        sticky="e", padx=20, pady=20
    )     

    update_data_label = ttk.Label(
        root,
        text="--",
        font=fuente_valores,
        anchor="center"
    )
    update_data_label.grid(
        row=i + 6, column=4, columnspan=1,
        sticky="w", padx=20, pady=20
    )  


    def refresh():
        ID_label.config(
            text=f"ID de adquisición: {data_ref.get('ID', '--')}"
        )

        read_data_label.config(
            text=f"{data_ref.get("date", "--")} {data_ref.get("utc", "--")}"
        )
        
        update_data_label.config(
            text=f"{data_ref.get("date", "--")} {data_ref.get("utc", "--")}"
        )

        value_labels[0].config(text=data_ref.get("ch0", "--"))
        value_labels[1].config(text=data_ref.get("ch1", "--"))
        value_labels[2].config(text=data_ref.get("ch2", "--"))
        value_labels[3].config(text=data_ref.get("ch3", "--"))
        value_labels[4].config(text=data_ref.get("C", "--"))

        root.after(update_interval, refresh)

    refresh()

