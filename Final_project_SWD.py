import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import sqlite3
from datetime import date

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS service (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            material REAL,
            labour REAL,
            services TEXT,
            services_count REAL,
            date TEXT,
            contractor TEXT,
            orders TEXT
             
        )
    ''')
conn.commit()



# All details about interfaces are write here
global excavationpool, plumbing, elecric, spashell, coping, tile, plaster
excavationpool = """digging and shaping the ground to create a hole or trench for the construction of a swimming pool. This involves removing soil, rocks, and other materials from the designated area to form the desired pool shape and depth. The excavation process is a crucial step in the overall construction of a swimming pool, setting the foundation for the pool's structure. It requires precision to achieve the correct dimensions and contours outlined in the pool design."""
plumbing = """Pool plumbing involves the installation of a network of pipes and fittings that facilitate the circulation and filtration of water within a swimming pool system."""
electric = """A pool's electrical system is essential for powering and controlling various components within the swimming pool setup. This includes the circulation pump, lighting, heaters, and other electrical devices. The electrical system enables the automation of pool functions, such as filtration and temperature regulation, through the use of timers and control panels."""
spashell = """Pool shell installation involves the placement and securing of the structural framework that forms the foundation and shape of a swimming pool. This process includes setting up the reinforcing steel, often in the form of rebar, and constructing the framework for the pool walls and floor. Once the framework is in place, concrete or another suitable material is applied to create the pool shell. This material is then shaped and finished according to the design specifications. The pool shell serves as the structural core of the pool, providing stability and shape for the overall construction."""
coping = """Pool coping serves both functional and aesthetic purposes in swimming pool construction. Functionally, it provides a protective cap or edging around the pool's edge, acting as a barrier between the pool structure and the surrounding deck or landscape. This helps prevent water from seeping into the pool's foundation and minimizes potential damage from exposure to the elements. Aesthetically, pool coping enhances the visual appeal of the pool area by creating a finished and polished edge. It also provides a comfortable and safe transition from the pool to the surrounding deck, offering a smooth surface for swimmers and creating a defined border for the pool structure. Additionally, pool coping can serve as a design element, contributing to the overall look and style of the pool environment."""
tile = """Pool tiles serve multiple purposes in swimming pool construction. Primarily, they provide a waterproof and durable surface that enhances the pool's structural integrity by preventing water from penetrating the pool walls and floor. This helps in maintaining the pool's overall longevity and stability. Aesthetically, pool tiles contribute to the visual appeal of the pool by adding color, texture, and design. They create a smooth and easy-to-clean surface, and their reflective properties can enhance the brightness and clarity of the water. Additionally, pool tiles are often used to mark waterlines and accentuate specific features within the pool, adding a decorative element to the overall design."""
plaster = """Pool plaster is a material applied to the interior surface of swimming pools to create a smooth, watertight finish. It serves as a protective layer over the pool shell, preventing water absorption and enhancing the structural integrity of the pool. Pool plaster contributes to the overall aesthetics by providing a clean, attractive surface. It comes in various colors and textures, allowing for customization of the pool's appearance. Additionally, pool plaster improves the comfort of swimmers, as it creates a smooth surface that is gentle on the skin. Regular maintenance and proper care of the pool plaster are essential for preserving its durability and appearance over time."""


class PoolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Imperial Pools and Spas")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Main Menu
        main_menu = ttk.Notebook(self.root)

        # Home Interface
        home_frame = ttk.Frame(main_menu)
        self.create_home_interface(home_frame)
        main_menu.add(home_frame, text="Home")

        # Cost Estimator
        cost_frame = ttk.Frame(main_menu)
        self.create_cost_estimator(cost_frame)
        main_menu.add(cost_frame, text="Cost Estimator")

        # Appointment Scheduling System
        appointment_frame = ttk.Frame(main_menu)
        self.create_appointment_scheduling(appointment_frame)
        main_menu.add(appointment_frame, text="Appointment Scheduling")

        # Contact Information
        contact_frame = ttk.Frame(main_menu)
        self.create_contact_information(contact_frame)
        main_menu.add(contact_frame, text="Contact Information")

        main_menu.pack(expand=1, fill="both")

    def create_home_interface(self, frame):
        # Load the image
        self.pool_image = PhotoImage(file="images/poolexcavation.png")

        # Create a Label widget with the image as background
        background_label = tk.Label(frame, image=self.pool_image)
        background_label.place(relwidth=1, relheight=1)

         # Create a Text widget for displaying information
        self.info_text = Text(frame, height=20, width=70)
        self.info_text.insert(tk.END, excavationpool)
        self.info_text.place(relx=0.6, rely=0.7, anchor="center")
        self.info_text.config(state="disabled")

        
        #Setting all home interface buttons
        
        # Excavation function with button
        def excavation_func():
            global excavationpool
            # Load the image
            self.pool_image = PhotoImage(file="images/poolexcavation.png")

            # changing background image
            background_label.configure(image=self.pool_image)

            # Change the information text
            self.info_text.config(state="normal")
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, excavationpool)
            self.info_text.config(state="disabled")

        excavation_button = Button(frame, text="Excavation", bg="SteelBlue2",fg='white', width=30,command=excavation_func)
        excavation_button.grid(row=1, column=0, pady=5)


        # Plumbing
        def plumbing_func():
            # Load the image
            self.pool_image = PhotoImage(file="images/plumbing.png")

            # changing background image
            background_label.configure(image=self.pool_image)

            # Change the information text
            self.info_text.config(state="normal")
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, plumbing)
            self.info_text.config(state="disabled")
            
        plumbing_button = Button(frame, text="Plumbing", bg="SteelBlue2",fg='white', width=30,command=plumbing_func)
        plumbing_button.grid(row=2, column=0, pady=5)

        # Electrical
        def electric_func():
            # Load the image
            self.pool_image = PhotoImage(file="images/poolelectric.png")

            # changing background image
            background_label.configure(image=self.pool_image)

            # Change the information text
            self.info_text.config(state="normal")
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, electric)
            self.info_text.config(state="disabled")
            
        electric_button = Button(frame, text="Electrical", bg="SteelBlue2",fg='white', width=30,command=electric_func)
        electric_button.grid(row=3, column=0, pady=5)

        # Pool/spa Shell
        def spashell_func():
            # Load the image
            self.pool_image = PhotoImage(file="images/poolspa.png")

            # changing background image
            background_label.configure(image=self.pool_image)

            # Change the information text
            self.info_text.config(state="normal")
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, spashell)
            self.info_text.config(state="disabled")
            
        poolshell_button = Button(frame, text="Pool/Spa Shell", bg="SteelBlue2",fg='white', width=30,command=spashell_func)
        poolshell_button.grid(row=4, column=0, pady=5)

        # Pool Coping
        def coping_func():
            # Load the image
            self.pool_image = PhotoImage(file="images/poolcoping.png")

            # changing background image
            background_label.configure(image=self.pool_image)

            # Change the information text
            self.info_text.config(state="normal")
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, coping)
            self.info_text.config(state="disabled")
            
        poolcoping_button = Button(frame, text="Pool Coping", bg="SteelBlue2",fg='white', width=30,command=coping_func)
        poolcoping_button.grid(row=5, column=0, pady=5)

        # Tile
        def tile_func():
            # Load the image
            self.pool_image = PhotoImage(file="images/tile.png")

            # changing background image
            background_label.configure(image=self.pool_image)

            # Change the information text
            self.info_text.config(state="normal")
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, tile)
            self.info_text.config(state="disabled")
            
        tile_button = Button(frame, text="Tile", bg="SteelBlue2",fg='white', width=30,command=tile_func)
        tile_button.grid(row=6, column=0, pady=5)

        # Plaster
        def plaster_func():
            # Load the image
            self.pool_image = PhotoImage(file="images/poolpluster.png")

            # changing background image
            background_label.configure(image=self.pool_image)

            # Change the information text
            self.info_text.config(state="normal")
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, plaster)
            self.info_text.config(state="disabled")
            
        plaster_button = Button(frame, text="Plaster", bg="SteelBlue2",fg='white', width=30,command=plaster_func)
        plaster_button.grid(row=7, column=0, pady=5)

        # Apply blue color style
        self.root.style = ttk.Style()
        self.root.style.configure("Blue.TButton", foreground="white", background="blue", padding=(5, 5), font=('Helvetica', 10, 'bold'))

        conn.commit()



    def create_cost_estimator(self, frame):

        def calculate_cost():
            try:
                # Retrieve material and labor costs from the entry widgets
                material_cost = float(material_entry.get())
                labour_cost = float(labour_entry.get())

                selected_checkboxes = [text for text, var in zip(checkbox_texts, checkbox_vars) if var.get() == 1]

                if selected_checkboxes:
                    # Combine material and labor costs with selected services
                    total_costs = {service: (material_cost + labour_cost) + ((material_cost + labour_cost) * 0.25) for service in selected_checkboxes}
                    
                    # Establish a new connection and cursor (ensure these are in the correct scope)
                    with sqlite3.connect('database.db') as conn:
                        cursor = conn.cursor()
                        today = date.today()
                        # Insert combined data into the database
                        for service, cost in total_costs.items():
                            cursor.execute("INSERT INTO service (services, material, labour, date) VALUES('{}',{},{},'{}');".format(service,material_cost,labour_cost,today))
                        
                        # Commit changes to the database
                        conn.commit()

                        cursor.execute('SELECT * FROM service')
                        data = cursor.fetchall()
                        print(data)

                        # Display messagebox with the results
                        message = "\n".join([f"Your Total cost for '{service}' is {cost}" for service, cost in total_costs.items()])
                        messagebox.showinfo("Cost Estimate", message)

            except ValueError:
                # Handle the case where the user entered non-numeric values
                messagebox.showerror("Error", "Please enter valid numeric values for Material and Labour costs.")
            except sqlite3.Error as e:
                # Handle database errors
                messagebox.showerror("Error", f"Database error: {e}")




                    

                 
                    

                # Continue with the rest of your code for calculating the cost
                material_cost = float(material_entry.get())
                labour_cost = float(labour_entry.get())
               
                cursor.execute("INSERT INTO service (material) VALUES (?)", (material_cost,))
                cursor.execute("INSERT INTO service (labour) VALUES (?)", (labour_cost,))



               # Calculate total cost for each selected service
                total_costs = {service: (material_cost + labour_cost) + ((material_cost+labour_cost) * 0.25) for service in selected_checkboxes}

                


                # Display messagebox with the results
                message = "\n".join([f"Your Total cost for '{service}' is {cost}" for service, cost in total_costs.items()])
                messagebox.showinfo("Cost Estimate", message)
            except ValueError:
                # Handle the case where the user entered non-numeric values
                messagebox.showerror("Error", "Please enter valid numeric values for Material and Labour costs.")

            conn.commit()
    

                




        services_label = tk.Label(frame, text="Services:", font=("Helvetica", 13, 'bold'), fg="black" )
        services_label.place(x=10, y=50)


        # Create a variable to store the state of the checkbox
        checkbox_var_excavation = tk.IntVar()
        checkbox_var_plumbing = tk.IntVar()
        checkbox_var_electrical = tk.IntVar()
        checkbox_var_pool_shell = tk.IntVar()
        checkbox_var_pool_coping = tk.IntVar()
        checkbox_var_tile = tk.IntVar()
        checkbox_var_plaster = tk.IntVar()

        # Create checkboxes
        checkbox_texts = ["Excavation", "Plumbing", "Electrical", "Pool/spa shell", "Pool coping", "Tile", "Plaster"]
        checkbox_vars = [checkbox_var_excavation, checkbox_var_plumbing, checkbox_var_electrical,
                         checkbox_var_pool_shell, checkbox_var_pool_coping, checkbox_var_tile, checkbox_var_plaster]

        # Create a checkbox (Checkbutton)
        checkbox = tk.Checkbutton(frame, text="Excavation", variable=checkbox_var_excavation)
        checkbox.place(x=100,y=80)
        checkbox = tk.Checkbutton(frame, text="Plumbing", variable=checkbox_var_plumbing)
        checkbox.place(x=100,y=120)
        checkbox = tk.Checkbutton(frame, text="Electrical", variable=checkbox_var_electrical)
        checkbox.place(x=100,y=160)
        checkbox = tk.Checkbutton(frame, text="Pool/spa shell", variable=checkbox_var_pool_shell)
        checkbox.place(x=200,y=80)
        checkbox = tk.Checkbutton(frame, text="Pool coping", variable=checkbox_var_pool_coping)
        checkbox.place(x=200,y=120)
        checkbox = tk.Checkbutton(frame, text="Tile", variable=checkbox_var_tile)
        checkbox.place(x=200,y=160)
        checkbox = tk.Checkbutton(frame, text="Plaster", variable=checkbox_var_plaster)
        checkbox.place(x=300,y=80)

        Material_label = tk.Label(frame, text="Material:", font=("Helvetica", 13), fg="black")
        Material_label.place(x=10, y=200)
        material_entry = tk.Entry(frame, width=20, font=("Monsterret"))
        material_entry.place(x=100, y=203)

        Labour_label = tk.Label(frame, text="Labour:", font=("Helvetica", 13), fg="black")
        Labour_label.place(x=10, y=230)
        labour_entry = tk.Entry(frame, width=20, font=("Monsterret"))
        labour_entry.place(x=100, y=233)

       

            
        Estimate_button = Button(frame, text="Cost Estimate", bg="SteelBlue2",fg='white', width=30, command=calculate_cost)
        Estimate_button.place(x=300,y=300)


        
        






        

        

    def create_appointment_scheduling(self, frame):


        selected_option_var = tk.StringVar()
        
        
        
          # Calendar

        def get_selected_date():
            selected_date = cal.get_date()
            selected_date_label.config(text=f"Selected Date: {selected_date}")
            
            # Assuming 'cursor' is a global variable or defined in an outer scope
            # Assuming 'cursor' is a global variable or defined in an outer scope
            cursor.execute("""SELECT services FROM service where date='{}'""".format(selected_date))
            print('yes')
            services_show = cursor.fetchall()
            print(services_show)
            if services_show:
                # Assuming 'services' is the first column in the result
                services_label.config(text=f"Services interested in: {services_show}")
            else:
                services_label.config(text="No data found")

            conn.commit()

    



        cal = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=12, day=4)
        cal.place(x=100,y=50)    


        get_date_button = tk.Button(frame, text="Get Selected Date", command=get_selected_date)
        get_date_button.place(x=200,y=47)

        # Label to display selected date
        selected_date_label = tk.Label(frame, text="Selected Date: ")
        selected_date_label.place(x=100,y=100)

        services_label = tk.Label(frame, text="Services interested in: ")
        services_label.place(x=50,y=150)

        contractors_label = tk.Label(frame, text="List of Contractors: ")
        contractors_label.place(x=50,y=200)

        # Dropdown menu options
        options = [
            "Efrain Preciado",
            "Bryan Preciado",
        ]

        # Create a StringVar to store the selected option
        selected_option = tk.StringVar(frame)
        selected_option.set(options[0])  # Set the default option
        

        # Create the dropdown menu
        dropdown_menu = ttk.OptionMenu(frame, selected_option, *options)
        dropdown_menu.place(x=200,y=200)

        comments_label = tk.Label(frame, text="Comments Box: ")
        comments_label.place(x=50,y=300)


        

        # Create a Text widget for entering new comments
        comment_entry = tk.Text(frame, wrap=tk.WORD, width=40, height=5)
        comment_entry.place(x=200,y=300)

        


        def confirm():
            # Get selected date
            selected_date = cal.get_date()

            # Get selected contractor name
            selected_contractor = selected_option.get()

            # Get comment from the Text widget
            comment = comment_entry.get("1.0", tk.END).strip()

            if selected_date and selected_contractor:  # Check if date and contractor are selected
                # Insert data into the orders table
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                query = "INSERT INTO service (date, contractor, orders) VALUES (?, ?, ?)"
                cursor.execute(query, (selected_date, selected_contractor, comment))
                conn.commit()


                # Show a message box
                messagebox.showinfo("Order Placed", "Your order has been placed!")

                # Display the saved data in a new window
                display_saved_data(selected_date, selected_contractor, comment)
            else:
                messagebox.showerror("Error", "Please select date and contractor!")


                

        def display_saved_data(selected_date, selected_contractor, comment):
            # Create a new window
            saved_data_window = tk.Toplevel()
            saved_data_window.geometry('200x200')

            # Display the saved data in the new window
            tk.Label(saved_data_window, text="Your Order Details:",font =('Helvetica',10,'bold') ).pack()
            tk.Label(saved_data_window, text=f"Date: {selected_date}",font = ('Helvetica',10,'bold')).pack()
            tk.Label(saved_data_window, text=f"Contractor: {selected_contractor}",font = ('Helvetica',10,'bold')).pack()
            tk.Label(saved_data_window, text=f"Comment: {comment}",font = ('Helvetica',10,'bold')).pack()

            saved_data_window.mainloop()



        confirm_button = Button(frame, text="Confirm", bg="SteelBlue2",fg='white', width=30, command = confirm)
        confirm_button.place(x=300,y=450)     

            
   


        

    

        


    def create_contact_information(self, frame):
        # List of Contractors
        contractor_label = ttk.Label(frame, text="List of Contractors", font=('Helvetica', 16, 'bold'))
        contractor_label.grid(row=0, column=0, pady=10, columnspan=2)

        efrain_label = ttk.Label(frame, text="i. Efrain Preciado")
        efrain_label.grid(row=1, column=0, sticky="w", pady=5)

        efrain_phone_label = ttk.Label(frame, text="1(818) 321-1111")
        efrain_phone_label.grid(row=2, column=0, sticky="w", pady=2)

        efrain_email_label = ttk.Label(frame, text="Fake_email@gmail.com")
        efrain_email_label.grid(row=3, column=0, sticky="w", pady=2)

        bryan_label = ttk.Label(frame, text="ii. Bryan Preciado")
        bryan_label.grid(row=4, column=0, sticky="w", pady=5)

        bryan_phone_label = ttk.Label(frame, text="1 (818) 471-1111")
        bryan_phone_label.grid(row=5, column=0, sticky="w", pady=2)

        bryan_email_label = ttk.Label(frame, text="Fake_email_2@gmail.com")
        bryan_email_label.grid(row=6, column=0, sticky="w", pady=2)

        # Office
        office_label = ttk.Label(frame, text="Office", font=('Helvetica', 16, 'bold'))
        office_label.grid(row=7, column=0, pady=2, columnspan=2)

        office_phone_label = ttk.Label(frame, text="i. 1 (818) 825-1111")
        office_phone_label.grid(row=8, column=0, sticky="w", pady=2)

        office_email_label = ttk.Label(frame, text="ii. Fake_email_3@gmail.com")
        office_email_label.grid(row=9, column=0, sticky="w", pady=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = PoolApp(root)
    root.mainloop()
