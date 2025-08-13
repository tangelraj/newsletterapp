from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = "secret123"  # Needed for forms and flash messages

class SubscriptionForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(message="Name is required")])
    email = StringField("Email", validators=[DataRequired(), Email(message="Invalid email address")])
    frequency = SelectField(
        "Frequency",
        choices=[("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly")],
        validators=[DataRequired()]
    )
    submit = SubmitField("Subscribe")

@app.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    form = SubscriptionForm()
    if form.validate_on_submit():
        flash("Subscribed successfully!", "success")
        return redirect(url_for("subscribe"))
    return render_template("subscribe.html", form=form)

if __name__ == "__main__":
    app.run(debug=False)
