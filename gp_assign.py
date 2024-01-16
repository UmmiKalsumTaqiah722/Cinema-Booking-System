import tkinter as tk
from tkinter import ttk
from tkinter import ttk, messagebox
import mysql.connector
import random

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cinema_system"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

class CinemaSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cinema System")
        self.root.geometry("500x700")
        self.root.configure(bg="lightgoldenrod1")  # Set the background color for the main window

        # GUI for Main Menu
        self.root_frame = ttk.Frame(root)
        self.root_frame.pack()
        self.root_label = tk.Label(self.root_frame, text="WELCOME TO HAUU CINEMA!", font=("Impact", 20), bg="navajowhite2")
        self.root_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Buttons for Membership, Ticket, and Movie
        self.membership_button = tk.Button(self.root_frame, text="Membership", command=self.show_membership,bg="moccasin")
        self.membership_button.grid(row=1, column=0, padx=5)

        self.movie_button = tk.Button(self.root_frame, text="Movie", command=self.show_movie,bg="moccasin")
        self.movie_button.grid(row=1, column=1, padx=5)

        self.ticket_button = tk.Button(self.root_frame, text="Ticket", command=self.show_ticket,bg="moccasin")
        self.ticket_button.grid(row=1, column=2, padx=5)

        self.current_module_frame = None

        # Variable to store the selected movie
        self.selected_movie = tk.StringVar()

        # Dictionaries to store data
        self.membership_data = {}
        self.movie_data = {}
        self.ticket_data = {}

    def show_membership(self):
        self.destroy_current_module()
        self.current_module_frame = ttk.Frame(self.root_frame)
        self.current_module_frame.grid(row=2, column=0, columnspan=3)
        self.create_membership_tab(self.current_module_frame)

    def show_ticket(self):
        self.destroy_current_module()
        self.current_module_frame = ttk.Frame(self.root_frame)
        self.current_module_frame.grid(row=2, column=0, columnspan=3)
        self.create_ticket_tab(self.current_module_frame)

    def show_movie(self):
        self.destroy_current_module()
        self.current_module_frame = ttk.Frame(self.root_frame)
        self.current_module_frame.grid(row=2, column=0, columnspan=3)
        self.create_movie_tab(self.current_module_frame)

    # to destroy the current frame for example from membership frame to ticket frame
    def destroy_current_module(self):
        if self.current_module_frame:
            self.current_module_frame.destroy()

    def calculate_age(self):
        # Retrieve the entered IC number
        ic_number = self.ic_number_entry.get()
        category= self.category_entry.get()

        # Extract birth year from IC number
        birthyear = int(ic_number[:2])
        currentyear = 24  # Assuming the current year is 2024
        age = currentyear - birthyear

        # Store the calculated age as an integer attribute in the class
        self.calculated_age = age

        # Categorize age into groups
        if age < 13:
            category = "Child"
        elif 13 <= age < 18:
            category = "Teenager"
        else:
            category = "Adult"

        # Update the age entry widget with the calculated age and category
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, int(age))
        self.category_entry.delete(0, tk.END)
        self.category_entry.insert(0, category)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#module 1 (membership)

    def create_membership_tab(self, parent):
        membership_tab = ttk.Frame(parent)

        # Membership Module Widgets
        self.ic_number_label = ttk.Label(membership_tab, text="IC Number (generate age):") 
        self.ic_number_entry = ttk.Entry(membership_tab)
        self.ic_number_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ic_number_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.name_label = ttk.Label(membership_tab, text="Name:")
        self.name_entry = ttk.Entry(membership_tab)
        self.name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.email_label = ttk.Label(membership_tab, text="E-mail:")
        self.email_entry = ttk.Entry(membership_tab)
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.state_label = ttk.Label(membership_tab, text="State:")
        self.state_entry = ttk.Entry(membership_tab)
        self.state_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.state_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.age_label = ttk.Label(membership_tab, text="Age:")
        self.age_entry = ttk.Entry(membership_tab)
        self.age_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.age_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.category_label = ttk.Label(membership_tab, text="Category:")
        self.category_entry = ttk.Entry(membership_tab)
        self.category_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.category_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")


        calculate_age_button = ttk.Button(membership_tab, text="Calculate Age", command=self.calculate_age)
        submit_button = ttk.Button(membership_tab, text="Submit", command=self.submit_membership)
        calculate_age_button.grid(row=6, column=0, columnspan=2, pady=5)
        submit_button.grid(row=7, columnspan=2, pady=10)

        update_button = ttk.Button(membership_tab, text="Update", command=self.update_membership)
        delete_button = ttk.Button(membership_tab, text="Delete", command=self.delete_membership)
        update_button.grid(row=8, column=0, pady=5)
        delete_button.grid(row=8, column=1, pady=5)

        # Add a label to display success message
        self.success_label = ttk.Label(membership_tab, text="")
        self.success_label.grid(row=9, column=0, columnspan=2, pady=10)

        membership_tab.grid()

    def submit_membership(self):
        # Retrieve the entered data from membership module
        ic_number = self.ic_number_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        state = self.state_entry.get()
        age = int(self.age_entry.get())
        category= self.category_entry.get()

        # Store the collected data in the instance variable
        self.membership_data = {
            "IC": ic_number,
            "Name": name,
            "Email": email,
            "State": state,
            "Age": age,
            "Category": category
        }

        sql = "INSERT INTO membership (IC_Number, Name, Email, State, Age, Category) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (ic_number, name, email, state, age, category)
        mycursor.execute(sql, val)
        mydb.commit()

        # Display success message
        self.success_label.config(text="Your data has been successfully saved")
        
    def update_membership(self):
        # Retrieve the entered data from membership module
        ic_number = int(self.ic_number_entry.get())
        name = self.name_entry.get()
        email = self.email_entry.get()
        state = self.state_entry.get()
        age = int(self.age_entry.get())

    # Update the collected data in the instance variable
        self.membership_data = {
            "IC": ic_number,
            "Name": name,
            "Email": email,
            "State": state,
            "Age": age,
        }

        # Update the record in the database
        sql = "UPDATE membership SET Name=%s, Email=%s, State=%s, Age=%s WHERE IC_Number=%s"
        val = (name, email, state, age, ic_number)
        mycursor.execute(sql, val)
        mydb.commit()

        # Display success message
        self.success_label.config(text="Your data has been successfully updated")

    def delete_membership(self):
        # Retrieve the entered data from membership module
        ic_number = self.ic_number_entry.get()

        # Delete the record from the database
        sql = "DELETE FROM membership WHERE IC_Number=%s"
        val = (ic_number,)
        mycursor.execute(sql, val)
        mydb.commit()

        # Display success message
        self.success_label.config(text="Your data has been successfully deleted")

        # Clear the entry fields after deletion
        self.ic_number_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.state_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)

#------------------------------------------------------------------------------------------------------------------------------------
#module 2 (movie)

    def create_movie_tab(self, parent):
        movie_tab = ttk.Frame(parent)
        movieinfo_text = tk.Text(movie_tab, height=8, width=35)
        movieinfo_text.grid(row= 0, column= 1, columnspan= 7, pady= 10)
        movieinfo_text.insert(tk.END, "Movie & Price: \n\n")
        movieinfo_text.insert(tk.END, "Trolls: RM 15 \n\n")
        movieinfo_text.insert(tk.END, "Wish: RM 16 \n\n")
        movieinfo_text.insert(tk.END, "The Marvels: RM 17 \n\n")
        movieinfo_text.configure(state='disabled')

        # Movie Module Widgets
        self.movie_name_label = ttk.Label(movie_tab, text="Movie:")
        self.movie_names = ["Trolls", "Wish", "The Marvels"]
        self.movie_name_entry = ttk.Combobox(movie_tab, values=self.movie_names, textvariable=self.selected_movie)
        self.movie_name_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.movie_name_entry.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.duration_label = ttk.Label(movie_tab, text="Duration:")
        self.duration_entry = ttk.Entry(movie_tab)
        self.duration_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.duration_entry.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        self.genre_label = ttk.Label(movie_tab, text="Genre:")
        self.genre_entry = ttk.Entry(movie_tab)
        self.genre_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.genre_entry.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        self.classification_label = ttk.Label(movie_tab, text="Classification:")
        self.classification_entry = ttk.Entry(movie_tab)
        self.classification_label.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.classification_entry.grid(row=4, column=2, padx=5, pady=5, sticky="w")

        submit_button = ttk.Button(movie_tab, text="Submit", command=self.submit_movie)
        submit_button.grid(row=6, columnspan=5, pady=10)

        # Bind the update_movie_info method to the <<ComboboxSelected>> event
        self.movie_name_entry.bind("<<ComboboxSelected>>", self.update_movie_info)

        # Add a label to display success message
        self.success_label = ttk.Label(movie_tab, text="")
        self.success_label.grid(row=8, column=0, columnspan=5, pady=5)

        movie_tab.grid()

    def update_movie_info(self, event):
        selected_movie = self.selected_movie.get()

        # Movie information dictionary
        movie_info = {
            "Trolls": {"duration": "93 minutes", "genre": "Musical/Animation", "classification": "PG13"},
            "Wish": {"duration": "95 minutes", "genre": "Animation/Comedy", "classification": "P12"},
            "The Marvels": {"duration": "105 minutes", "genre": "Action/Fantasy", "classification": "PG13"}
        }

        # movie information based on the selected movie
        if selected_movie in movie_info:
            info = movie_info[selected_movie]
            self.duration_entry.delete(0, tk.END)
            self.duration_entry.insert(0, str(info["duration"]))
            self.genre_entry.delete(0, tk.END)
            self.genre_entry.insert(0, info["genre"])
            self.classification_entry.delete(0, tk.END)
            self.classification_entry.insert(0, info["classification"])

    def submit_movie(self):
        # Retrieve the entered data from movie module
        selected_movie = self.selected_movie.get()
        duration = self.duration_entry.get()
        genre = self.genre_entry.get()
        classification = self.classification_entry.get()

        # Store the collected data in the instance variable
        self.movie_data = {
            "Selected Movie": selected_movie,
            "Duration": duration,
            "Genre": genre,
            "Classification": classification
        }

         # To insert your Data to your database
        sql = "INSERT INTO movie (Movie_Name, Duration, Genre, Classification) VALUES (%s, %s, %s, %s)"
        val = (selected_movie, duration, genre, classification)
        mycursor.execute(sql, val)
        mydb.commit()

        # Display success message
        self.success_label.config(text="Movie Added Successfully!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#module 3 (ticket)
        
    def create_ticket_tab(self, parent):
        ticket_tab = ttk.Frame(parent)

        #Serve as the container for the seat layout.
        self.seat_layout_frame = tk.Canvas(ticket_tab, width=250, height=70, bg="white")
        self.seat_layout_frame.grid(row=0, column=0, columnspan=2, pady=10)

        seat_width = 40  # Adjust the width of each seat
        seat_height = 20  # Adjust the height of each seat
        rows = 2
        columns = 5

        for row in range(rows):
            for seat_number in range(1, columns + 1):
                x1 = 10 + (seat_number - 1) * (seat_width + 7) 
                y1 = 10 + row * (seat_height + 7)
                x2 = x1 + seat_width
                y2 = y1 + seat_height

                #10 is for margin # 7 is refererd to padding
                #x1 for top left corner of the seat
                #y1 for top side of the canvas
                #x2 for bottom right corner of the seat(width of the seat)
                #y2 for bottom right corner of the seat(height of the seat)

                self.seat_layout_frame.create_rectangle(x1, y1, x2, y2, fill="orange")
                label_text = f"Seat {row * columns + seat_number}"
                label_x = x1 + seat_width / 2
                label_y = y1 + seat_height / 2

                #dividing by 2 help in finding the midpoint of the width and height of the seat rectangle

                self.seat_layout_frame.create_text(label_x, label_y, text=label_text, fill="white")

        # Ticket Module Widgets
        self.ic_number_label = ttk.Label(ticket_tab, text="IC Number:")
        self.ic_number_entry = ttk.Entry(ticket_tab)
        self.ic_number_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ic_number_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.selected_movie_label = ttk.Label(ticket_tab, text="Selected Movie:")
        self.selected_movie_entry = ttk.Entry(ticket_tab, state='readonly', textvariable=self.selected_movie)
        self.selected_movie_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.selected_movie_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.date_label = ttk.Label(ticket_tab, text="Date (YY/MM/DD):")
        self.date_entry = ttk.Entry(ticket_tab)
        self.date_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.date_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.seat_number_label = ttk.Label(ticket_tab, text="Seat Number:")
        self.seat_number_combobox = ttk.Combobox(ticket_tab, values=["Seat 1", "Seat 2", "Seat 3", "Seat 4", "Seat 5", "Seat 6", "Seat 7", "Seat 8", "Seat 9", "Seat 10"])
        self.seat_number_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.seat_number_combobox.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.pax_label = ttk.Label(ticket_tab, text="Pax:")
        self.pax_entry = ttk.Entry(ticket_tab)
        self.pax_label.grid(row=5,column=0, padx=5, pady=5, sticky="w")
        self.pax_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        submit_button = ttk.Button(ticket_tab, text="Submit", command=self.submit_ticket)
        submit_button.grid(row=6, columnspan=2, pady=10)

        update_button = ttk.Button(ticket_tab, text="Update", command=self.update_ticket)
        delete_button = ttk.Button(ticket_tab, text="Delete", command=self.delete_ticket)
        update_button.grid(row=7, column=0, pady=5)
        delete_button.grid(row=7, column=1, pady=5)

        # Output Label & result
        label = tk.Label(ticket_tab, text='RECEIPT', font=("Impact",13))
        output_label = tk.Label(ticket_tab, text="")
        label.grid(row=8, columnspan=2, pady=10)
        output_label.grid()

        # Add a label to display success message
        self.success_label = ttk.Label(ticket_tab, text="")
        self.success_label.grid(row=9, column=0, columnspan=5, pady=5)

        ticket_tab.grid()

    def update_ticket(self):
        # Retrieve the entered data from membership module
        ic_number = self.ic_number_entry.get()
        selected_movie = self.selected_movie_entry.get()
        date = self.date_entry.get()
        seat_number = self.seat_number_combobox.get()
        pax = int(self.pax_entry.get())

        # The price below is to defined the value from your selections
        prices = {
            "Trolls": 15,
            "Wish": 16,
            "The Marvels": 17,
            }

        # Calculate the total price. This will be derived from your selection (Package, Pack).
        total_price = (prices[selected_movie] * pax)


        # Update the collected data in the instance variable
        self.ticket_data = {
        "IC_Number": ic_number,
        "Selected_Movie": selected_movie,
        "Date": date,
        "Seat_Number": seat_number,
        "Pax": pax,
        "Price": total_price,
        }

        # Update the record in the database
        sql = "UPDATE ticket SET Selected_Movie=%s, Date=%s, Seat_Number=%s, Pax=%s, Price=%s WHERE IC_Number=%s"
        val = (selected_movie, date, seat_number, pax, total_price, ic_number)
        mycursor.execute(sql, val)
        mydb.commit()

        # Display a message indicating the update has been performed
        messagebox.showinfo("Update", "Ticket information updated successfully")
    
    def clear_ticket_tab(self):
        # Clear the entry fields in the ticket tab
        self.ic_number_entry.delete(0, tk.END)
        self.selected_movie.set("")  # Clear the selected movie
        self.date_entry.delete(0, tk.END)
        self.seat_number_combobox.delete(0, tk.END)
        self.pax_entry.delete(0, tk.END)

    def delete_ticket(self):
        # Retrieve the entered data from ticket module
        ic_number = self.ic_number_entry.get()

        # Delete the record from the database
        sql = "DELETE FROM ticket WHERE IC_Number=%s"
        val = (ic_number,)
        mycursor.execute(sql, val)
        mydb.commit()

        # Display a message indicating the deletion has been performed
        messagebox.showinfo("Delete", "Ticket information deleted successfully")

        # Clear the entry fields after deletion
        self.clear_ticket_tab()

    def submit_ticket(self):
        while True:
            # Retrieve the entered data from ticket module
            ic_number = self.ic_number_entry.get()
            selected_movie = self.selected_movie.get()
            date = self.date_entry.get()
            seat_number = self.seat_number_combobox.get()
            pax= int(self.pax_entry.get())

            # Store the collected data in the instance variable
            self.ticket_data = {
                "IC": ic_number,
                "Selected Movie": selected_movie,
                "Date": date,
                "Seat Number": seat_number,
                "Pax": pax
            }   

            # The price below is to defined the value from your selections
            prices = {
                "Trolls": 15,
                "Wish": 16,
                "The Marvels": 17,
                }

            # Calculate the total price
            total_price = (prices[selected_movie] * pax)
            
            booking_id = random.randint(100, 999)

            sql = "INSERT INTO ticket (IC_Number, Selected_Movie, Date, Seat_Number, Pax, Price, Booking_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (ic_number, selected_movie, date, seat_number, pax, total_price, booking_id)
            mycursor.execute(sql, val)
            mydb.commit()
    
            self.success_label.config(text=f"IC Number: {ic_number}\n"
            f"Selected Movie: {selected_movie}\n"
            f"Date: {date}\n"
            f"Seat Number: {seat_number}\n"
            f"Pax: {pax}\n"
            f"Price: RM{total_price}\n" 
            f"Booking ID: {booking_id}\n\n"
            f"THANK YOU!")

            messagebox.showinfo("Booking ID", f"Your Booking ID: {booking_id}")

            break   
    
if __name__ == "__main__":
    root = tk.Tk()
    app = CinemaSystemApp(root)
    root.mainloop() 