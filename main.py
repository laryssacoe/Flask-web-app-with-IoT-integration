from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = '7p68Nvqik7R$' # sets up a secret key that protects information to the Flask app only

conn = sqlite3.connect('users.db') # connects to a SQL database named users
c = conn.cursor() # creates a temporary cursor object (space in SQL database memory)

# drops the table if another named users exists (works for iterative changes in code)
c.execute("DROP TABLE IF EXISTS users")

# creates the table containing three values: username, password and id that will assign a unique value to each user on the table)
c.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              password TEXT NOT NULL)''')
conn.commit()
conn.close()

# login page, asks for credentials and offers sign up
# defines the route to the login page using request methods GET and POST to receive and submit information
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST': # checks if submission was made
        # if so, stores the submission of username and password into variables
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # searches the columns and select the row in which the username matches the one typed as well as the password
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

        # returns the user found with match password and username, and if none found, returns "None"
        user = c.fetchone()
        conn.close()

        # checks if user exists and is logged in
        if user:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password'

    return render_template('login.html', error=error)

# sign up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # asks for the insertion of username and password values as a tuple stored in users
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

        conn.commit()
        conn.close()

        # after sign up, redirects the user to do their login
        return redirect(url_for('login'))

    return render_template('signup.html')

# dashboard page
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    # if user is already logged in, leads them to their dashboard, using their username to get their personalized page
    username = session['username']
    return render_template('dashboard.html', username=username)

# streaming page
@app.route('/streaming')
def streaming():
    return render_template('streaming.html')

# logout functionality
@app.route('/logout')
def logout():
    # removes the username from the session dictionary, logging them out
    session.pop('username', None)
    return redirect(url_for('login'))

# runs the application
if __name__ == '__main__':
    app.run(debug=True)