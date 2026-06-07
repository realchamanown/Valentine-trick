import tkinter as tk
import random

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("💌 Love Message 💌")
    popup.config(bg="#FFD1DC")  # pinkbg

    label = tk.Label(popup, text="You are the reason my heart beats! 💖", 
                     font=("Comic Sans MS", 16, "bold"), 
                     bg="#FFD1DC", fg="#D81B60")
    label.pack(padx=20, pady=20)

# NO
def move_button(event):
    x = random.randint(50, 300)
    y = random.randint(50, 300)
    no_button.place(x=x, y=y)

# heart
def create_falling_heart():
    x = random.randint(10, 390)  # ตำแหน่ง
    size = random.randint(14, 24)  # ขนาด
    heart = canvas.create_text(x, 0, text="💖", font=("Arial", size))  # สร้างหัวใจ
    animate_heart(heart, random.randint(2, 5))  # ความเร็ว

# fall action
def animate_heart(heart, speed):
    canvas.move(heart, 0, speed)  # ขยับหัวใจ
    if canvas.coords(heart)[1] < 400:  # ถ้ายังไม่ถึงล่างสุด
        root.after(50, animate_heart, heart, speed)
    else:
        canvas.delete(heart)  # ลบออกเมื่อถึงขอบล่าง
        create_falling_heart()  # สร้างหัวใจใหม่

# windows
root = tk.Tk()
root.title("💖 Love Confession 💖")
root.geometry("400x400")

# สร้าง Canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white", highlightthickness=0)
canvas.place(x=0, y=0)

# ข้อความ
question_label = tk.Label(root, text="Do you like me? 💞", 
                          font=("Lily Script One", 20, "bold"), 
                          bg="#FFE4E1", fg="#D81B60")
question_label.pack(pady=20)

# เยส
yes_button = tk.Button(root, text="Yes 💘", 
                       font=("Comic Sans MS", 16, "bold"), 
                       bg="#FF69B4", fg="black", 
                       activebackground="#FF1493", 
                       activeforeground="pink",
                       command=show_popup)
yes_button.pack(pady=10)


no_button = tk.Button(root, text="No 💔", 
                      font=("Comic Sans MS", 14, "bold"), 
                      bg="#FFC0CB", fg="black")
no_button.pack()

no_button.bind("<Enter>", move_button)

for _ in range(15):
    root.after(random.randint(100, 2000), create_falling_heart)

root.mainloop()
