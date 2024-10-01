import qrcode
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def widgets():
    global entry, qr_label
    label = tk.Label(root, 
                    text="Hello, you can paste the URL from which you want to create a QRcode into the box below.",)
    label.pack(side="top", pady=10)

    entry = tk.Entry(root, width=60)
    entry.pack(pady=10)

    button = tk.Button(root, text="Generate QR", height=1, width=15, font=('Arial', 18), command=generate_qr)
    button.pack(pady=10)

    qr_label = tk.Label(root)  
    qr_label.pack(pady=20)

def generate_qr():
    url = entry.get()
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("generated_qr.png")

        show_qr()

def show_qr():
    qr_img = Image.open("generated_qr.png")
    qr_img = qr_img.resize((150, 150), Image.Resampling.LANCZOS)

    qr_img_tk = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_img_tk)
    qr_label.image = qr_img_tk

root = tk.Tk()
root.geometry("600x400")
root.title("QR Code Generator")

widgets()

root.mainloop()
