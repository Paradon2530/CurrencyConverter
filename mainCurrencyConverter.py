from datetime import date
from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from tkinter import messagebox

# creating the main window
window = Tk()

# this gives the window the width(310), height(320) and the position(center)
window.geometry('310x340+500+200')
# this is the title for the window
window.title('Currency Converter')
# this will make the window not resizable, since height and width is FALSE
window.resizable(height=FALSE, width=FALSE)

currency_rates = CurrencyRates()
currency_code = CurrencyCodes()


def main_process():
    component = components_class()
    currency_income = component.from_currency_combox.get().upper()
    currency_convert = component.to_currency_combox.get().upper()
    value = int(component.amount_entry.get())

    today = date.today()
    datetime = today.strftime("%B %d, %Y")

    result_value = currency_rates.convert(currency_income, currency_convert, value, today)

    component.result_label.config(text=result_value)
    component.time_label.config(text=datetime)


def check_text_value() :
    component = components_class()
    return (component.from_currency_combox.get().upper() != ""
             and component.to_currency_combox.get().upper() != ""
             and component.amount_entry.get() != "")

class colorvariable():
    primary = '#E5A310'
    secondary = '#0083FF'
    white = '#FFFFFF'


class currencyvariable():
    currency_type = "THB"
    currenycode_list = ["THB", "INR", "USD", "CAD", "CNY", "DKK", "EUR"]


colors = colorvariable()
currency = currencyvariable()


# the top frame
top_frame = Frame(window, bg=colors.primary, width=300, height=80)
top_frame.grid(row=0, column=0)
# label for the text Currency Converter
name_label = Label(top_frame, text='Currency Converter', bg=colors.primary, fg=colors.white, pady=30, padx=24,
                   justify=CENTER, font=('Poppins 20 bold'))
name_label.grid(row=0, column=0)

# the top frame
top_frame = Frame(window, bg=colors.primary, width=300, height=80)
top_frame.grid(row=0, column=0)
# label for the text Currency Converter
name_label = Label(top_frame, text='Currency Converter', bg=colors.primary, fg=colors.white, pady=30, padx=24,
                   justify=CENTER, font=('Poppins 20 bold'))
name_label.grid(row=0, column=0)
# the bottom frame

bottom_frame = Frame(window, width=300, height=250)
bottom_frame.grid(row=1, column=0)


class components_class:
    from_currency_combox = ttk.Combobox(bottom_frame, width=14, font=('Poppins 10 bold'))
    to_currency_combox = ttk.Combobox(bottom_frame, width=14, font=('Poppins 10 bold'))

    amount_label = Label(bottom_frame, text='AMOUNT:', font=('Poppins 10 bold'))
    amount_label.place(x=6, y=80)

    # amount_text = Text(bottom_frame,)
    amount_entry = Entry(bottom_frame, width=25, font=('Poppins 10 bold'))
    amount_entry.place(x=5, y=105)

    result_label = Label(bottom_frame,  font=('Poppins 10 bold'))
    result_label.place(x=5, y=135)

    time_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
    time_label.place(x=5, y=155)

    def combobox_from(self):
        from_currency_label = Label(bottom_frame, text='FROM:', font=('Poppins 8 bold'), justify=LEFT)
        from_currency_label.place(x=5, y=10)

        self.from_currency_combox['values'] = currency.currenycode_list
        self.from_currency_combox.place(x=5, y=30)
        self.from_currency_combox.bind('<<ComboboxSelected>>', combobox_form_changed)

    def combobox_to(self):
        to_currency_label = Label(bottom_frame, text='TO:', font=('Poppins 8 bold'), justify=RIGHT)
        to_currency_label.place(x=160, y=10)

        self.to_currency_combox.bind('<<ComboboxSelected>>', combobox_to_changed)
        self.to_currency_combox['values'] = currency.currenycode_list
        self.to_currency_combox.place(x=160, y=30)


    def button_amount(self):
        convert_button = Button(bottom_frame, text="CONVERT",command=convert_currency,  bg=colors.primary, fg=colors.white,
                                font=('Poppins 10 bold'))
        convert_button.place(x=5, y=180)


def combobox_form_changed(event):
    result_code = currency_code.get_currency_name(component.from_currency_combox.get())
    messagebox.showinfo(
        title='Result',
        message=f'You currency {result_code}!'
    )

def combobox_to_changed(event):
    result_code = currency_code.get_currency_name(component.to_currency_combox.get())
    messagebox.showinfo(
        title='Result',
        message=f'Your currency {result_code}!'
    )

def show_message():
    messagebox.showinfo(
        title='Result',
        message=f'Your text value can not null !'
    )

def convert_currency():
    if check_text_value():
        main_process()
    else:
        show_message()


component = components_class()
component.combobox_from()
component.combobox_to()
component.button_amount()

window.mainloop()



