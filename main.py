from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)
    
    def post(self):
        billform = BillForm(request.form)

        the_bill = flat.Bill(float(billform.amount.data),  billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))
        return render_template('bill_form_page.html', 
                               billform=billform,
                               result=True,
                               name1=flatmate1.name,
                               amount1 = flatmate1.pays(the_bill, flatmate2),
                               name2 = flatmate2.name,
                               amount2 = flatmate2.pays(the_bill, flatmate1)
                               )
    

class ResultsPage(MethodView):
        
    def post(self):
        billform = BillForm(request.form)

        the_bill = flat.Bill(float(billform.amount.data),  billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))
        return render_template('results.html', 
                               name1=flatmate1.name,
                               amount1 = flatmate1.pays(the_bill, flatmate2),
                               name2 = flatmate2.name,
                               amount2 = flatmate2.pays(the_bill, flatmate1)
                               )
    
class BillForm(Form):
    test = 101
    amount = StringField(label='Bill Amount: ', default="100")
    period = StringField(label='Bill Period: ', default = "March 2024")
    name1 =  StringField(label='Name: ', default="John")
    days_in_house1 = StringField(label='Days in the house', default ="20")

    name2 =  StringField(label='Name: ', default ="Mary")
    days_in_house2 = StringField(label='Days in the house', default="10")
    
    button = SubmitField("Calculate")

# routing
app.add_url_rule('/', view_func = HomePage.as_view('home_page'))
app.add_url_rule('/bill_form_page', view_func = BillFormPage.as_view('bill_form_page'))
#app.add_url_rule('/results', view_func = ResultsPage.as_view('results_page'))


app.run(debug=True)


