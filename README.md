
# Flask Web Development & IoT Integration
## Table of Contents

- [About the Project](#Appendix)
- [Built With](#Documentation)
- [Installation](#Installation)
- [Usage/Examples](#Usage/Examples)
- [Functionality](#Screenshots)
- [Demonstration](#Demo)
- [References](#Acknowledgments)


    
## About the Project

The objective of this project was to develop a small Flask web application that integrates an IoT device simulated by an IoT platform (Blynk was used). 

The web app serves as a control server to the theoretical device, meaning in the 'Streaming' Page, the user has access to the eletronic device that intends to simulate a robot, in this case, a LED was used that would get the commands from both the web app server as well as the Blynk server to connect to the device by Wi-Fi and be able to turn the light ON and OFF through the computer.



## Built With

* [SQLite](https://sqlite.org/index.html)

* [Flask](https://flask.palletsprojects.com/en/2.3.x/)

* [Python](https://www.python.org/)

* JavaScript

* CSS

* HTML


## Installation

In order to run this project, you need to: 

* Install the lattest version of Python in (https://www.python.org/downloads/)

* Create  a virtual environment: 
```bash
  python -m venv venv
```
* Download the Source code and run OR go to GitHub Repository, get the URL and input: 
```bash
  git clone <(https://github.com/laryssacoe/Flask-web-app-with-IoT-integration.git)>
```

### Libraries needed 

* Flask

```bash
  pip install flask
```

* SQLite3 (Note that this library is part of the Python Standard, however, to ensure that you have the correct version, install)

```bash
  pip install pysqlite3
```
     
## Usage/Examples

Demonstration of code snippets and their purpose. 

* Sign Up functionality: 
Defines the route to sign up page that will request the user to create an username and password and will save the the values in a tuple in the table that will be used to match the credentials to the user in the redirecting of login page. 

```python
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
```


* Streaming Commands: 
Defines the commands that will send information to the Blynk server to turn the light ON and OFF and creates a function that will update the status in the streaming page by getting this information from the Blynk server.

```JavaScrpit
	// defines the function that turns the light on in IoT integration
	function turnLightOn() {
		// uses XML Http and the GET request to update data from the blink server API and make value of light = 1
		var xhttp = new XMLHttpRequest();
		xhttp.open("GET", "https://blynk.cloud/external/api/update?token=9htotNtrt1lrBSfxk8gwZNA5S8iMlMkY&v0=1", true);
		// sends new value
		xhttp.send();
		// calls the update light status function to automatically change the status to 1 or 'on'
		updateLightStatus();
	}

    // defines the function that turns light off in IoT integration
	function turnLightOff() {
		var xhttp = new XMLHttpRequest();
		// uses XML Http and the GET request to update data from the blynk server API and make value of light = 0
		xhttp.open("GET", "https://blynk.cloud/external/api/update?token=9htotNtrt1lrBSfxk8gwZNA5S8iMlMkY&v0=0", true);
		// sends the new value
			xhttp.send();
		// calls the update light status function to automatically change the status to 0 or 'off'
		updateLightStatus();
	}

	// defines the function that will update constantly and display the status of the light
		function updateLightStatus() {

	// uses XML Http to get the new request of data from the Blynk API server to update light status
    var xhttp = new XMLHttpRequest();

    // defines a function that will only be called by the change of light state in the XMLHttp request and display its status
    xhttp.onreadystatechange = function() { // calls the function upon change using "xhttp.onreadystate" property of XML HTTP

        // checks if the "readystate" xmlhttp property is done (4) and the request of data was successful (200)
        if (this.readyState == 4 && this.status == 200) {

            // if so, assigns the variable response to a response text that will be used to display status
            var responseText = this.responseText;

            // checks the status of the light by the response text, if the response is '1', attatches the value "on" to the string lightStatus
            // if not, assigns the value "off" to be displayed
            var lightStatus = responseText == "1" ? "on" : "off";

            // attributes an identifier to the HTML element light-status that will return the content setup
            // in this case, the content is the status of the light in string plus the actual value define in variable "lightStatus"
            document.getElementById("light-status").innerHTML = "The status of the light is currently " + lightStatus + "!";

			// checks the status of the light to assign icon id to the specific png link
            if (lightStatus == "on") {
                document.getElementById("light-icon").src = "https://toppng.com/uploads/preview/light-bulb-on-off-png-11553940319kdxsp3rf0i.png";
            } else {
                document.getElementById("light-icon").src = "https://toppng.com/uploads/preview/light-bulb-on-off-png-11553939967conkckniqn.png";
            }
        }
    };

    // initializes a new GET request of data to the Blynk server and sends the request to get the new value of the light
    xhttp.open("GET", "https://blynk.cloud/external/api/get?token=9htotNtrt1lrBSfxk8gwZNA5S8iMlMkY&v0", true);
    xhttp.send();
}
```


## Functionality

The user (computer) is connected to the Flask server to receive and submit information, this way, when the user send the command for the light to turn ON in the streaming page, the Flask serve sends this information to the Blynk server, which is connected by the ID Token.

After that, the Bynk server will connect to the button (pin v0), changing the status of the light and sending this information back to the user. The Blynk app simulates and IoT physical device that can be connected through Wi-Fi if there was a need for the physical components.

![Imgur](https://i.imgur.com/0nWDGnp.png)

This image exemplifies how the Flask web app connects to the IoT platform. 



## Demonstration

In this video, I showcase the syncronized functionality of the web server connected with the platform IoT, which could be connected to a physical device, but, in this case, it simulates one.

Link to video: https://youtu.be/Vu9XOczp5yk


## References

 - [Blynk Documentation](https://docs.blynk.io/en/blynk.cloud/get-datastream-value)
 - [CSS Resources](https://freefrontend.com/css-code-examples/)
- [Flask Database Tutorial](http://turing.com.br/material/flask/tutorial/setup.html#tutorial-setup)
 - [Login Template](https://bbbootstrap.com/snippets/bootstrap-5-login-form-using-neomorphism-89456141)
 - [Professional README Guide](https://coding-boot-camp.github.io/full-stack/github/professional-readme-guide)
