from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill.flat_classes import Flatmate, Bill
app = Flask(__name__)
class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform=bill_form)


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)
        amount = float(billform.amount.data)
        period = billform.period.data

        name1 = billform.name1.data
        days1 = float(billform.days_in_house1.data)
        flatmate1 = Flatmate(name1, days1)

        name2 = billform.name2.data
        days2 = float(billform.days_in_house2.data)
        flatmate2 = Flatmate(name2, days2)

        the_bill = Bill(amount, period)

        pays1 = flatmate1.pays(the_bill, flatmate2)
        pays2 = flatmate2.pays(the_bill, flatmate1)

        return render_template('results.html',
                               name1=name1, amount1=pays1,
                               name2=name2, amount2=pays2)




class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")

    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the house: ")

    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the house: ")

    button = SubmitField("Calculate")


app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.run()
