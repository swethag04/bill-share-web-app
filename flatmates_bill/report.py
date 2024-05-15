import webbrowser
import os
from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that contains name of flatmate, period of bill 
    and their share
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_share = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_share = str(round(flatmate2.pays(bill, flatmate1),2))
        
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        
        #add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt = 'Flatmates Bill', border=0, align ='C', ln=1)

        #Insert period
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=100, h=40, txt = 'Period:', border=0)
        pdf.cell(w=150, h=40, txt = bill.period, border=0, ln=1)

        #Insert name
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt = flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt = flatmate1_share, border=0, ln=1)
        pdf.cell(w=100, h=25, txt = flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt = flatmate2_share, border=0, ln=1)

        # change dir to files, generate and open pdf
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open('file://'+os.path.realpath(self.filename))