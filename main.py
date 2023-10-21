import tkinter as tk
from tkinter import messagebox
import segno
from PIL import Image, ImageTk

def generate_qrcode():
    link = link_entry.get()
    qrcode = segno.make_qr(link)
    qrcode.save("output.png", scale=20)
    qr_image = Image.open("basic_qrcode.png")
    tk_image = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=tk_image)
    qr_label.image = tk_image
    qr_label.pack()
    qr_label.pack()


app = tk.Tk()
app.title("QR Code Generator")

app.geometry("600x750")  
app.configure(bg="#ffffff")


header_label = tk.Label(app, text="QR Code Generator", font=("Helvetica", 16, "bold"), bg="#32c6eb", fg="white")
header_label.pack(pady=10)

instruction_label = tk.Label(app, text="Enter the link and click the button to generate a QR code.", bg="#32c6eb", fg="white")
instruction_label.pack()

link_entry = tk.Entry(app, width=40)
link_entry.pack(pady=10)

generate_button = tk.Button(app, text="Generate QR Code", command=generate_qrcode, bg="#93c995", fg="white", relief="solid")
generate_button.pack()

qr_label = tk.Label(app, bg="#32c6eb")

app.protocol("WM_DELETE_WINDOW", app.quit)

app.mainloop()
