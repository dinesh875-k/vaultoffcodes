from tkinter import *
from tkinter import messagebox

class LoanCalculator:

    def __init__(self):
        self.window = Tk()
        self.window.title("Loan Calculator")
        self.window.config(bg="#f0f0f0")  # Light background

        # Frames for better design
        input_frame = Frame(self.window, bg="#f0f0f0", padx=20, pady=20)
        input_frame.grid(row=0, column=0, sticky=W)

        output_frame = Frame(self.window, bg="#f0f0f0", padx=20, pady=20)
        output_frame.grid(row=1, column=0, sticky=W)

        # Input Labels and Entry 
        Label(input_frame, text="Annual Interest Rate (%)", bg="#f0f0f0").grid(row=0, column=0, sticky=W, pady=5)
        Label(input_frame, text="Number of Years", bg="#f0f0f0").grid(row=1, column=0, sticky=W, pady=5)
        Label(input_frame, text="Loan Amount", bg="#f0f0f0").grid(row=2, column=0, sticky=W, pady=5)

        self.annualInterestRateVar = StringVar()
        self.numberOfYearsVar = StringVar()
        self.loanAmountVar = StringVar()
        
        Entry(input_frame, textvariable=self.annualInterestRateVar, justify=RIGHT, width=20).grid(row=0, column=1, pady=5)
        Entry(input_frame, textvariable=self.numberOfYearsVar, justify=RIGHT, width=20).grid(row=1, column=1, pady=5)
        Entry(input_frame, textvariable=self.loanAmountVar, justify=RIGHT, width=20).grid(row=2, column=1, pady=5)

        # Output Labels
        Label(output_frame, text="Monthly Payment", bg="#f0f0f0").grid(row=0, column=0, sticky=W, pady=5)
        Label(output_frame, text="Total Payment", bg="#f0f0f0").grid(row=1, column=0, sticky=W, pady=5)

        self.monthlyPaymentVar = StringVar()
        self.totalPaymentVar = StringVar()
        
        Label(output_frame, textvariable=self.monthlyPaymentVar, bg="#e0e0e0", width=20, anchor=E).grid(row=0, column=1, pady=5)
        Label(output_frame, textvariable=self.totalPaymentVar, bg="#e0e0e0", width=20, anchor=E).grid(row=1, column=1, pady=5)


        Button(self.window, text="Compute Payment", command=self.computePayment, bg="#4CAF50", fg="white", padx=10, pady=5).grid(row=2, column=0, pady=10, sticky=E)

        self.window.mainloop()

    def computePayment(self):
        try:
            loanAmount = float(self.loanAmountVar.get())
            annualInterestRate = float(self.annualInterestRateVar.get())
            years = int(self.numberOfYearsVar.get())

            monthlyInterestRate = annualInterestRate / 1200
            monthlyPayment = self.getMonthlyPayment(loanAmount, monthlyInterestRate, years)
            totalPayment = monthlyPayment * 12 * years

            self.monthlyPaymentVar.set(f"{monthlyPayment:,.2f}")
            self.totalPaymentVar.set(f"{totalPayment:,.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        return loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))


# Run the calculator
LoanCalculator()
