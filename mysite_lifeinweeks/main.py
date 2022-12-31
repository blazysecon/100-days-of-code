from datetime import datetime, timedelta

import flask

app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index() -> str:

    death_age = 90
    message = ""
    if flask.request.method == "POST":
        try:
            date_birth = datetime.strptime(
                flask.request.form["birthdate-input"], "%Y-%m-%d"
            ).date()

            current_date = datetime.now().date()
            school_date = datetime((date_birth + timedelta(weeks=7 * 52.179)).year, 9, 1).date()
            workdate = date_birth + timedelta(weeks=23 * 52.179)
            death_date = date_birth + timedelta(weeks=death_age * 52.1795)

            message = "<pre>"
            for age in range(death_age + 2):
                year_start_at_age = datetime(date_birth.year + age, 1, 1).date()
                for week in range(52):
                    week_date = year_start_at_age + timedelta(weeks=week)
                    if week_date < date_birth:
                        message += "  "
                    elif (
                        week_date <= school_date
                        and date_birth < current_date
                        and week_date <= current_date
                    ):
                        message += "\u25A7 "
                    elif (
                        week_date <= workdate
                        and school_date < current_date
                        and week_date <= current_date
                    ):
                        message += "\u25A4 "
                    elif (
                        week_date <= current_date
                        and workdate < current_date
                        and week_date <= current_date
                    ):
                        message += "\u25A3 "
                    elif week_date <= death_date and current_date < death_date:
                        message += "\u25A1 "
                    else:
                        message += "  "
                message += "\n"
        except:
            message = f'Incorrect date: {flask.request.form["birthdate-input"]}'
    return flask.render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()
