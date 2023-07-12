from fpdf import FPDF


class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house +
                                       flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return round(to_pay, 2)


class PdfReport:

    def __init__(self, file_name):
        self.file_name = file_name

    #   flatmate1, flatmate2, bill

    def generate(self, flatmate1, flatmate2, bill):
        self.pdf = FPDF(orientation="P", unit="pt", format="A4")
        self.pdf.add_page()

        # Add icon
        self.pdf.image("house.png", w=30, h=30)

        # Insert title
        self.pdf.set_font(family="Times", size=25, style="B")
        self.pdf.cell(w=0, h=30, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Insert period label and value
        self.pdf.set_font(family="Times", size=14, style="B")
        self.pdf.cell(w=100, h=40, txt="Period:", border=1)
        self.pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and amount due from 1st flatmate
        self.pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        self.pdf.cell(w=100,
                      h=40,
                      txt=str(flatmate1.pays(bill, flatmate2)),
                      border=1,
                      ln=1)

        # Insert name and amount due from 2nd flatmate
        self.pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        self.pdf.cell(w=100,
                      h=40,
                      txt=str(flatmate2.pays(bill, flatmate1)),
                      border=1,
                      ln=1)

        self.pdf.output("{}.pdf".format(self.file_name))


