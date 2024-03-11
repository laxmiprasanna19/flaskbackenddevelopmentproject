from flask import Flask, render_template, request
import re

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def index():
    test_string = ""
    regex_pattern = ""
    matches = []
    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")
        try:
            matches = re.findall(regex_pattern, test_string)
        except re.error:
            error_message = "Invalid regex pattern."
            return render_template("index.html", test_string=test_string, regex_pattern=regex_pattern, matches=matches, error_message=error_message)
    return render_template("index.html", test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route("/validate-email", methods=["POST"])
def validate_email():
    email = request.form.get("email")
    is_valid_email = re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email)
    if is_valid_email:
        result_message = f"{email} is a valid email address."
    else:
        result_message = f"{email} is not a valid email address."
    return render_template("index.html", result_message=result_message)

if _name_ == "_main_":
    app.run(debug=True)