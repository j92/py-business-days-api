from flask import Flask
from flask import request
from calc.days_diff import DaysDiff
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/diff", methods=['GET'])
def days_diff():
    if not request.args.get('start', 0):
        return 'Missing start parameter'

    if not request.args.get('end', 0):
        return 'Missing end parameter'

    try:
        # day-month-year format
        start = datetime.strptime(request.args.get('start'), '%d-%m-%Y')
        end = datetime.strptime(request.args.get('end'), '%d-%m-%Y')
    except ValueError:
        return 'Invalid date strings. Format must be day-month-year.'

    return str(DaysDiff().diff(start, end))

if __name__ == "__main__":
    app.run()