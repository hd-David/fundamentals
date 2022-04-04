from flask import Flask, render_template, redirect
from enter import Createform

app = Flask(__name__)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = Createform()
    if form.validate_on_submit():
        flash('successful')
    return render_template('base.html', form=form)

