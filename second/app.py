# app.py
from flask import Flask, request, render_template_string
import traceback

app = Flask(__name__)

# HTML template with a form to submit Python code
html_template = """
<!doctype html>
<title>Python Executor</title>
<h1>Execute Python Code</h1>
<form method="post">
  <textarea name="code" rows="10" cols="30" placeholder="Enter Python code here..."></textarea><br>
  <input type="submit" value="Execute">
</form>
<h2>Output:</h2>
<pre>{{ output }}</pre>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        code = request.form["code"]
        try:
            # Execute the code and capture the output
            local_vars = {}
            exec(code, {}, local_vars)
            output = str(local_vars)
        except Exception as e:
            # Capture any exception that occurs
            output = f"Error: {str(e)}\n{traceback.format_exc()}"
    return render_template_string(html_template, output=output)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
