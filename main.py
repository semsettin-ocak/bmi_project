from tkinter import *

screen = Tk()
screen.title("BMI Calculator")
screen.config(padx=60, pady=20)


def bmi_calculation():
    weight_input = weight_entry.get()
    height_input = height_entry.get()

    if weight_input == "" or height_input == "":
        result_label.config(text="It can not be empty!")
    else:
        try:
            bmi = float(weight_input) / (float(height_input) / 100) ** 2
            resulting_string = bmi_statements(bmi)
            result_label.config(text=resulting_string)
        except:
            result_label.config(text="Enter a valid number!")


weight_label = Label(text="Enter your weight (kg)")
weight_label.pack()

weight_entry = Entry(width=20)
weight_entry.pack()

height_label = Label(text="Enter your height (cm)")
height_label.pack()

height_entry = Entry(width=20)
height_entry.pack()

calculation_button = Button(text="Calculate", command=bmi_calculation)
calculation_button.pack()

result_label = Label()
result_label.pack()


def bmi_statements(bmi):
    result_string = f"Your bmi is: {(round(bmi,2))}. You are "
    if bmi < 18.5:
        result_string += "Underweight."
    elif 18.5 <= bmi < 25:
        result_string += "Normal."
    elif 25 <= bmi < 40:
        result_string += "Overweight."
    else:
        result_string += "Obese."
    return result_string


screen.mainloop()
