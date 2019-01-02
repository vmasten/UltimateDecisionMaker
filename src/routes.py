from . import app
from flask import render_template, request
# from .forms import ChoiceForm, C_Form, CompanyForm, LocationForm
import random


@app.route('/', methods=['POST', 'GET'])
def home():
    """
    """
    # grab data from user inputs in dynamic forms
    data = request.form
    keys = list(data.keys())
    values = list(data.values())

    # notice, to randomly select n out of m items:
    # random.shuffle(arr)
    # Take the first 2 elements of the now randomized array
    # print arr[0:2]

    # check if user has valid input
    if len(keys) > 1:
        decision = random.choice(values)
        return render_template('home.html', decision=decision)
        # return render_template('home.html', decision=decision, form=form, old_form=old_form)

    # if old_form.validate_on_submit():
    #     choice1 = old_form.data['choice1']
    #     choice2 = old_form.data['choice2']
    #     decision = random.choice([choice1, choice2])
    #     return render_template('home.html', decision=decision, form=form, old_form=old_form)

    # return render_template("edit.html", form=form)

    # return render_template('home.html', form=form, old_form=old_form)
    return render_template('home.html')


# @app.route('/history/<user_id>', methods=['POST', 'GET'])
# def hisotry():
