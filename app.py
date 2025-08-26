from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded credentials for testing
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "secret"

# Simple login page
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    <p>{{ message }}</p>
</body>
</html>
"""

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            message = "Welcome, admin!"
        else:
            message = "Invalid credentials"
    return render_template_string(login_page, message=message)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
