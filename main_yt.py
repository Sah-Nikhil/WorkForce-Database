from tkinter import *
from tkinter import ttk
import uuid
import json

global my_data_list
global currentRowIndex

my_data_list = {}

root = Tk()
root.title('Workforce Database Setup')
root.geometry("831x530")
root.configure(bg='#F9F7FB')
root.resizable(False ,False)


input_frame = LabelFrame(root, text='Info', bg="lightgray", font=('Consolas', 14))
input_frame.grid(row=0, column=0, rowspan=5, columnspan=4)


l1 = Label(input_frame, anchor="w", width=24,
           height=1, relief="ridge", text="ID",
           font=('Consolas', 14)).grid(row=1, column=0)


l2 = Label(input_frame, anchor="w", width=24,
           height=1, relief="ridge", text="First Name",
           font=('Consolas', 14)).grid(row=2, column=0)


l3 = Label(input_frame, anchor="w", width=24,
           height=1, relief="ridge", text="Last Name",
           font=('Consolas', 14)).grid(row=3, column=0)


l4 = Label(input_frame, anchor="w", width=24,
           height=1, relief="ridge", text="Cell Phone",
           font=('Consolas', 14)).grid(row=4, column=0)


l5 = Label(input_frame, anchor="w", width=24,
           height=1, relief="ridge", text="Custom ID",
           font=('Consolas', 14)).grid(row=5, column=0)



#userinput setup
id_value = StringVar()
id_value.set(uuid.uuid4())

crm_id = Label(input_frame, anchor="w", height=1, relief="ridge", textvariable=id_value, font=('Consolas', 14))
crm_id.grid(row=1, column=1)

crm_fn = Entry(input_frame, width=30, borderwidth=2, fg="black", font=('Consolas', 14))
crm_fn.grid(row=2, column=1, columnspan=2)

crm_ln = Entry(input_frame, width=30, borderwidth=2, fg="black", font=('Consolas', 14))
crm_ln.grid(row=3, column=1, columnspan=2)

crm_cellphone = Entry(input_frame, width=30, borderwidth=2, fg="black", font=('Consolas', 14))
crm_cellphone.grid(row=4, column=1, columnspan=2)

crm_csid = Entry(input_frame, width=30, borderwidth=2, fg="black", font=('Consolas', 14))
crm_csid.grid(row=5, column=1, columnspan=2)


#visual output of userinput in form of table
trv = ttk.Treeview(root, columns=(1, 2, 3, 4, 5), show="headings", height="16")
trv.grid(row=11, column=0, rowspan=16, columnspan=4)

trv.heading(1, text="ID", anchor="center")
trv.heading(2, text="First Name", anchor="center")
trv.heading(3, text="Last Name", anchor="center")
trv.heading(4, text="Cell Phone", anchor="center")
trv.heading(5, text="Custom ID", anchor="center")

trv.column("#1", anchor="w", width=270, stretch=True)
trv.column("#2", anchor="w", width=140, stretch=False)
trv.column("#3", anchor="w", width=140, stretch=False)
trv.column("#4", anchor="w", width=140, stretch=False)
trv.column("#5", anchor="w", width=140, stretch=False)


# opening json file
def load_json_from_file():
    global my_data_list
    with open("d:\\Python Project\\app to register househelp\\dada1.json", "r") as file_handler:
        my_data_list = json.load(file_handler)
    file_handler.close()
    print('file has been opened to register househelp')


# saving json file
def save_json_to_file():
    global my_data_list
    with open("d:\\Python Project\\app to register househelp\\dada1.json", "w") as file_handler:
        json.dump(my_data_list, file_handler, indent=4)
    file_handler.close()
    print('file has been written to and saved')


# deleting data from table
def remove_all_data_from_trv():
    for item in trv.get_children():
        trv.delete(item)


# loading datatable as json
def load_trv_with_json():
    global my_data_list

    remove_all_data_from_trv()

    rowIndex = 1

    for key in my_data_list.keys():
        guid_value = my_data_list[key]["id"]
        first_name = my_data_list[key]["first_name"]
        last_name = my_data_list[key]["last_name"]
        cell_phone = my_data_list[key]["cell_phone"]
        custom_id = my_data_list[key]["custom_id"]
        trv.insert('', index='end', iid=rowIndex, text="", values=(guid_value, first_name, last_name, cell_phone, custom_id))
        rowIndex = rowIndex + 1


# --review=Y
def clear_all_fields():
    crm_fn.delete(0, END)
    crm_ln.delete(0, END)
    crm_cellphone.delete(0, END)
    crm_csid.delete(0, END)
    crm_id.configure(text="")
    crm_fn.focus_set()
    id_value.set(uuid.uuid4())
    change_background_color("#FFFFFF")


# --review=Y
def find_row_in_my_data_list(guid_value):
    global my_data_list
    row = 0

    for rec in my_data_list.keys():
        if my_data_list[rec]["id"] == guid_value:
            return row
        row += 1



# set error bg (if error occurs, naturally)
def change_background_color(new_color):
    crm_fn.config(bg=new_color)
    crm_ln.config(bg=new_color)
    crm_cellphone.config(bg=new_color)
    crm_csid.config(bg=new_color)


# button function in certain cases
def change_enabled_state(state):
    if state == 'Edit':
        btnUpdate["state"] = "normal"
        btnDelete["state"] = "normal"
        btnAdd["state"] = "disabled"
    elif state == 'Cancel':
        btnUpdate["state"] = "disabled"
        btnDelete["state"] = "disabled"
        btnAdd["state"] = "disabled"
    else:
        btnUpdate["state"] = "disabled"
        btnDelete["state"] = "disabled"
        btnAdd["state"] = "normal"


# --review=Y
def load_edit_field_with_row_data(_tuple):
    if len(_tuple) == 0:
        return;
    id_value.set(_tuple[0]);
    crm_fn.delete(0, END)
    crm_fn.insert(0, _tuple[1])
    crm_ln.delete(0, END)
    crm_ln.insert(0, _tuple[2])
    crm_cellphone.delete(0, END)
    crm_cellphone.insert(0, _tuple[3])
    crm_csid.delete(0, END)
    crm_csid.insert(0, _tuple[4])


# resetting the (current) entry set to take in entries
def cancel():
    clear_all_fields()
    change_enabled_state('New')


# button press triggers printing entries to console
def print_all_entries():
    global my_data_list
    for rec in my_data_list:
        print(my_data_list[rec])

    crm_fn.focus_set();


# button press adds entries if filled or displays visual error if empty/error
def add_entry():
    guid_value = id_value.get()
    first_name = crm_fn.get()
    last_name = crm_ln.get()
    cell_phone = crm_cellphone.get()
    custom_id = crm_csid.get()

    if len(first_name) == 0:
        change_background_color("#FFB2AE")
        return

    process_request('_INSERT_', guid_value, first_name, last_name, cell_phone, custom_id)


# button press updates entries if edited or displays visual error if empty/error
def update_entry():
    guid_value = id_value.get()
    first_name = crm_fn.get()
    last_name = crm_ln.get()
    cell_phone = crm_cellphone.get()
    custom_id = crm_csid.get()

    if len(first_name) == 0:
        change_background_color("#FFB2AE")
        return

    process_request('_UPDATE_', guid_value, first_name, last_name, cell_phone, custom_id)


# button press deletes selected entries or doesnt work if there are no entries present/selected
def delete_entry():
    guid_value = id_value.get()
    process_request('_DELETE_', guid_value, None, None, None, None)


# defining process request which will help interact with various buttons in the software
def process_request(command_type, guid_value, first_name, last_name, cell_phone, custom_id):
    global my_data_list

    if command_type == "_UPDATE_":
        row = find_row_in_my_data_list(guid_value)
        if row >= 0:
            dict = {"id": guid_value, "first_name": first_name,
                    "last_name": last_name, "cell_phone": cell_phone, "custom_id": custom_id}
            my_data_list[dict["id"]] = dict

    elif command_type == "_INSERT_":
        dict = {"id": guid_value, "first_name": first_name,
                "last_name": last_name, "cell_phone": cell_phone, "custom_id": custom_id}
        my_data_list[dict["id"]] = dict

    elif command_type == "_DELETE_":
        row = find_row_in_my_data_list(guid_value)
        if row >= 0:
            del my_data_list[guid_value];

    save_json_to_file();
    load_trv_with_json();
    clear_all_fields();


# defining use of mouseclick_release
def MouseButtonUpCallBack(event):
    currentRowIndex = trv.selection()[0]
    lastTuple = (trv.item(currentRowIndex, 'values'))
    load_edit_field_with_row_data(lastTuple)
    change_enabled_state('Edit')


# binding mouseclick_release
trv.bind("<ButtonRelease>", MouseButtonUpCallBack)

# creating buttons
ButtonFrame = LabelFrame(root, text='', bg="lightgray", font=('Consolas', 14))
ButtonFrame.grid(row=5, column=0, columnspan=6)

##save=Button(root,text="Save",padx=20,pady=10,command=Save)
btnShow = Button(ButtonFrame, text="Print", padx=20, pady=10, command=print_all_entries)
btnShow.pack(side=LEFT)

btnAdd = Button(ButtonFrame, text="Add", padx=20, pady=10, command=add_entry)
btnAdd.pack(side=LEFT)

btnUpdate = Button(ButtonFrame, text="Update", padx=20, pady=10, command=update_entry)
btnUpdate.pack(side=LEFT)

btnDelete = Button(ButtonFrame, text="Delete", padx=20, pady=10, command=delete_entry)
btnDelete.pack(side=LEFT)

btnClear = Button(ButtonFrame, text="Reset", padx=18, pady=10, command=cancel)
btnClear.pack(side=LEFT)

btnExit = Button(ButtonFrame, text="Exit", padx=20, pady=10, command=root.quit)
btnExit.pack(side=LEFT)

# --review=Y
load_json_from_file()
load_trv_with_json()

crm_fn.focus_set();
root.mainloop()