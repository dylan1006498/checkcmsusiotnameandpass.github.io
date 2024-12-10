from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Username and password data
USER_DATA = {
    "Computerbetas847": {"password": "ComputerBetas847", "message": "Welcome, Computerbetas847!"},
    "tahar": {"password": "Uhc2008)", "message": "Hello Tahar, nice to see you!"},
    "scarsdale": {"password": "ChickenNuggets", "message": "Scarsdale, enjoy your stay!"},
    "Discoders": {"password": "Aryan@Raja", "message": "Welcome, Discoder!"},
    "BinaryTree": {"password": "GovindaGovinda", "message": "Hello BinaryTree, explore wisely!"},
    "Itachi_SU": {"password": "separateunion69420", "message": "Itachi_SU, sharingan activated!"},
    "shirokosimps": {"password": "abydosBankRobbers", "message": "ShirokoSimps, ready for action!"},
    "init to win it": {"password": "wVV,g0767LPB", "message": "Welcome, Init to Win It!"},
    "tigORZ": {"password": "trinityFTW", "message": "TigORZ, conquer the day!"},
    "trinityteam": {"password": "GoT!ger$1711", "message": "Trinity Team, you're the best!"},
    "Trinity 2028": {"password": "TrinityTigers2028", "message": "Hello Trinity 2028, stay awesome!"},
    "team_rhs": {"password": "#Password1", "message": "Team RHS, good luck!"},
    "DrJdaBest": {"password": "qadzum-myjwof-7pupVa", "message": "DrJdaBest, you rock!"},
    "panini": {"password": "1234", "message": "Hello Panini, enjoy your time here!"}
}

# HTML template for login and messages
LOGIN_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form action="/login" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
    {% if error %}
    <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

MESSAGE_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
</head>
<body>
    <h1>{{ message }}</h1>
    <a href="/">Logout</a>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(LOGIN_PAGE)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = USER_DATA.get(username)

    if user and user["password"] == password:
        return render_template_string(MESSAGE_PAGE, message=user["message"])
    else:
        return render_template_string(LOGIN_PAGE, error="Invalid username or password!")

if __name__ == "__main__":
    app.run(debug=True)
