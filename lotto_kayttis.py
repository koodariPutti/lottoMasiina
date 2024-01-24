import tkinter as tk
from tkinter import messagebox

def todennakoisyys(pallo, maara):
    tulos = 1
    for i in range(maara):
        tulos *= (pallo - i)
        tulos //= (i + 1)
    return tulos

def vertailu(luku1, luku2):
    if luku1 <= 0 or luku2 <= 0:
        messagebox.showerror("Error", "The number of balls must be a positive number.")
        return False
    elif luku1 < luku2:
        messagebox.showerror("Error", "At most the total number of balls can be drawn.")
        return False

    return True

def calculate_probability():
    lottopallo = int(entry_lottopallo.get())
    arvonta_maara = int(entry_arvonta_maara.get())

    if vertailu(lottopallo, arvonta_maara):
        tulos = todennakoisyys(lottopallo, arvonta_maara)
        probability_label.config(text=f"The probability of guessing all {arvonta_maara} balls correctly is 1/{tulos}")

# Luo pääikkuna
root = tk.Tk()
root.title("Lottery Probability Calculator")

# Luo ja aseta käyttöliittymäelementit
label_info = tk.Label(root, text="Enter the total number of lottery balls and the number of drawn balls:")
label_info.pack(pady=10)

label_lottopallo = tk.Label(root, text="Total number of lottery balls:")
label_lottopallo.pack()

entry_lottopallo = tk.Entry(root)
entry_lottopallo.pack()

label_arvonta_maara = tk.Label(root, text="Number of drawn balls:")
label_arvonta_maara.pack()

entry_arvonta_maara = tk.Entry(root)
entry_arvonta_maara.pack()

calculate_button = tk.Button(root, text="Calculate Probability", command=calculate_probability)
calculate_button.pack(pady=10)

probability_label = tk.Label(root, text="")
probability_label.pack()

# Käynnistä pääsilmukka
root.mainloop()
