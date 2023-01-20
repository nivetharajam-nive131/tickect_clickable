import tkinter as tk

def cash_callback():
    online_payment_label.pack_forget()
    online_payment_dropdown.pack_forget()

def online_callback():
    online_payment_label.pack()
    online_payment_dropdown.pack()
    
def submit():
    movie = movie_var.get()
    seats = ticket_var.get()
    payment = payment_var.get()
    name = name_var.get()
    phone = phone_var.get()
    online_payment = online_payment_var.get()

    # Code to save the booking details to a database or file (omitted)

    result_label.config(text=f"Booking Confirmed!\nMovie: {movie}\nSeats: {seats}\nPayment: {payment}\nName: {name}\nPhone: {phone}\nOnline Payment: {online_payment}")
    result_label.pack()
    ok_button.pack()

def on_ok_click():
    root.destroy()

root = tk.Tk()
root.title("Movie Ticket Booking")

movie_var = tk.StringVar(value="Select a movie")
ticket_var = tk.StringVar(value="1")
payment_var = tk.StringVar(value="Cash")
name_var = tk.StringVar()
phone_var = tk.StringVar()
online_payment_var = tk.StringVar(value="gpay")

movie_label = tk.Label(root, text="Select a movie:")
movie_label.pack()
movie_dropdown = tk.OptionMenu(root, movie_var, "Varisu", "Thunivu")
movie_dropdown.pack()

ticket_label = tk.Label(root, text="Number of seats:")
ticket_label.pack()
ticket_entry = tk.Entry(root, textvariable=ticket_var)
ticket_entry.pack()

payment_label = tk.Label(root, text="Payment method:")
payment_label.pack()
cash_rb = tk.Radiobutton(root, text="Cash", variable=payment_var, value="Cash", command=cash_callback)
cash_rb.pack()
online_rb = tk.Radiobutton(root, text="Online", variable=payment_var, value="Online", command=online_callback)
online_rb.pack()

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.pack()

phone_label = tk.Label(root, text="Enter your phone number:")
phone_label.pack()
phone_entry = tk.Entry(root, textvariable=phone_var)
phone_entry.pack()

online_payment_label = tk.Label(root, text="Online Payment:")
online_payment_dropdown = tk.OptionMenu(root, online_payment_var, "gpay", "paytm", "internet banking")

submit_button = tk.Button(root, text="Submit",command=submit)
submit_button.pack()

result_label = tk.Label(root)
ok_button = tk.Button(root, text="OK", command=on_ok_click)
root.mainloop() 