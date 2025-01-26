import datetime
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

FONT = ('algerian', 20, 'italic')
FONT2 = ('calibre', 10)
bg = 'lightblue'
foreground = "#220099"
button_width = 20


def watermark_image():  # used for adding watermark
    original_image = entry.get()
    if original_image:
        img = Image.open(original_image)

        watermark_size = img.size
        watermark = Image.new("RGBA", size=watermark_size, color=(255, 255, 255, 0))

        draw = ImageDraw.Draw(watermark)
        font = ImageFont.load_default(10)

        for i in range(0, 2000):
            draw.text((random.randint(1, 3000), random.randint(1, 3000)),
                      fill=(128, 128, 128, 128),
                      text="@Shiv",
                      font=font)

        img_converted = img.convert("RGBA")
        print(img_converted.mode)
        print(watermark.mode)

        combined = Image.alpha_composite(img_converted, watermark)

        messagebox.showinfo("success", "watermark is added to image")
        combined.show()
        choice = messagebox.askyesno(title="Important", message=" would you like to save this image? ")
        if choice:
            combined.save(f"watermarked_img_{datetime.date.today()}.png")
            print("image is saved.")
    else:
        messagebox.showerror("Error", "Put image path first!!")


def rotate_image():     # used for rotating image
    path = entry.get()
    if path:
        original_image = Image.open(path)
        rotated_image = original_image.rotate(45)
        messagebox.showinfo("success", "Your image is rotated:)")
        rotated_image.show()
    else:
        messagebox.showerror("Error", "Enter the image path first")


def upload_image():     # uploading image on the canvas in the window
    image_path = entry.get()
    if image_path:
        with Image.open(image_path) as img:
            resize_img = img.resize((300, 500))
            # resize_img.show()
            photo_img = ImageTk.PhotoImage(resize_img)
            # height, width = resize_img.size

        canvas.config(height=resize_img.width, width=resize_img.height)
        canvas.delete('all')
        canvas.create_image(100, -50, anchor='nw', image=photo_img)
        canvas.image = photo_img
    else:
        messege = messagebox.showerror("Error", "please provide image path")


def exit_screen():   # used for close window
    window.destroy()


def create_label():     # used for creating label on window
    label = tk.Label(text="Watermark the image", bg=bg, font=FONT, foreground=foreground)
    label.grid(column=1, row=0)

    info_label = tk.Label(text="<<----See the image here before the further process",
                          font=FONT2,
                          bg=bg,
                          foreground=foreground)
    info_label.grid(column=2, row=1)

    info2 = tk.Label(text="<---- Paste the path of image here!", bg=bg, foreground=foreground)
    info2.grid(column=2, row=2)

    welcome = tk.Label(text="Photo Watermarking Application", font=FONT2, bg=bg)
    welcome.grid(column=0, row=0)


def create_button():
    #   Button
    upload_button = tk.Button(text="Upload image", command=upload_image, width=button_width)
    upload_button.grid(column=1, row=4)

    exit_button = tk.Button(text="Exit", command=exit_screen, width=button_width)
    exit_button.grid(column=1, row=5)

    add_watermark_button = tk.Button(text="Add watermark", command=watermark_image, width=button_width)
    add_watermark_button.grid(column=2, row=4)

    rotate_img_button = tk.Button(text="Rotate Image", command=rotate_image, width=button_width)
    rotate_img_button.grid(column=2, row=5)

    compress_img_button = tk.Button(text="Compress Image", command=compress_image_size, width=button_width)
    compress_img_button.grid(column=0, row=5)


def create_canvas():    # used for create canvas for the execution of watermark image
    #   Canvas
    global canvas, entry
    create_label()
    create_button()
    canvas = tk.Canvas(highlightthickness=0, height=200, width=500, bg=bg)
    canvas.grid(column=1, row=1)
    image = "project_image.ppm"
    photo_img = tk.PhotoImage(file=image)
    image_canvas = canvas.create_image(250, 100, image=photo_img)
    canvas.image = photo_img

    #   Entry
    entry = tk.Entry(width=50)
    entry.grid(column=1, row=2)


def compress_image_size():
    real_image_path = entry.get()
    if real_image_path:
        real_image = Image.open(real_image_path)
        print(f"real image size: {real_image.size}")
        width, height = real_image.size
        ratio = (width, height)
        n_width = int(ratio[0]/2)
        n_height = int(ratio[1]/2)
        compress_image = real_image.resize((n_width, n_height), Image.LANCZOS)
        print(f"compress image size: {compress_image.size}")
        success = messagebox.showinfo(title="success", message="your image is successfully compressed!!")
        compress_image.show()
        choice = messagebox.askyesno(title="Important", message="Want to save the image?")
        if choice:
            compress_image.save(f"compressed_img{datetime.date.today()}.png")
            print("image is saved.")
    else:
        msg = messagebox.showerror(title="Error", message="first enter the path of the image!!")


window = tk.Tk()
window.title("watermarking application")
window.minsize(width=800, height=500)
window.configure(bg=bg)

create_canvas()

window.mainloop()
