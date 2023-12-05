import customtkinter
from new import Colors
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("700x400")
entryString = customtkinter.StringVar(root)
entryString2 = customtkinter.StringVar(root)

class User:
    def __init__(self,name,passers):
        self.name = name
        self.passers = passers

def login():
    state = entry1.cget("state")
    state = entry2.cget("state")
    user1 = entryString.get()
    password=entryString2.get()
    print(password)
    if(user1 ==""):
        print("UserName not found")
    else:
        p1 = User(user1,password)
        print(p1.name,p1.passers)
    # if(user == "koyejo"):
    #     print("Good Boy")
    # else:
    #     print("Get Out of here Before I call the police")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady= 20, padx=60, fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Login System", text_color=Colors.alarm, fg_color="transparent")
label.pack(pady= 12, padx= 10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username", textvariable=entryString)
entry1.pack(pady=12, padx =10)
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password",textvariable=entryString2)
entry2.pack(pady=12, padx =10)
button = customtkinter.CTkButton(master=frame, text="Login", command=login, fg_color=Colors.alarm, )
button.pack(pady=12, padx=10)
entry3 = customtkinter.CTkRadioButton(master=frame, text = "MALE",  )
entry3.pack(pady=15, padx=5)
def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(master=frame, values=["option 1", "option 2"],
                                     command=combobox_callback)
combobox.set("option 2")
entry3 = customtkinter.CTkRadioButton(master=frame, text = "FEMALE",  )
entry3.pack( pady=15,)
root.mainloop()






















