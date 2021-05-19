# College Enquiry Chatbot
## Group members
- Sanjana T. Aniwar (Roll No. 2)
- Veena R. Badgujar (Roll No. 3)
- Shivani R. Dugade (Roll No. 59)
---
## Project Guide
- Prof. V. M. Kharche
---
## Content
### Main Directory
```
College-Enquiry-Chatbot
└───Chatbot
└───Documents
└───Screenshots
```
### 1. Chatbot Folder
Contains flask files, templates, static, virtual environment folder of the website
```
Chatbot
└───data
└───static
└───templates
└───venv
|   bot.py
|   std-startup.xml
```
- #### data Folder
> AIML, or Artificial Intelligence Markup Language, is an XML dialect for creating natural language software agents.\
> Contains all the aiml files of the project.\
> data directory
```
data
|   std-profile.aiml
|   bot-profile.aiml
|   bye.aiml
|   ...
```
following code is taken from [std-profile.aiml](https://github.com/shivanidugade/College-Enquiry-Chatbot/blob/master/Chatbot/data/std-profile.aiml)
```xml
<category>
<pattern>_</pattern>
<that>* WHAT CAN I CALL YOU</that>
<template>
<think><set name="personality">average</set><set name="name"><formal><star/></formal></set></think>
Nice to meet you <get name="name"/>.
</template>
</category>

<category>
<pattern>_</pattern>
<that>* WHAT COLOR ARE YOUR EYES</that>
<template>
<set name="eyecolor"><star/></set> eyes are nice.
</template>
</category>
```
- #### static Folder
> A web application often requires a static file such as a javascript file or a CSS file supporting the display of a web page. Usually, the web server is configured to serve them for you, but during the development, these files are served from static folder in your package or next to your module and it will be available at /static on the application.\
> static Directory
```
static
└───css
└───js
└───media
```
> Ajax of chatbot\
following code is taken from app.js
```javascript
var $ = new BaseJS();
$.ready(function() {
	var result = $.select("#result");
	var message = $.select("#message");
	function reply() {
		$.http("/" + message[0].value).get().ready(function(res) {
				if (res.readyState === 4 && res.status == 200) {
					txt = res.responseText;
					if (txt.trim() === "") {
						txt = "?";
					}
					result.append("<div class='bot'><img class='mr-2' src='/static/media/kgce1.png' style='width: 30px; height: 30px'><span>" + txt + "</span></div>");
					result[0].scrollTop = result[0].scrollHeight;
				}
			});
			result.append("<div class='you'><span class=' bg-primary text-white'>" + message[0].value + "</span></div>");
			message[0].value = "";
			result[0].scrollTop = result[0].scrollHeight;
	}
	$.select("#message").on("keyup").call(function(e) {
		if(e.keyCode == 13 && message[0].value.trim() !== "") {
			reply();
		}
	});
	$.select("#send").on("click").call(function() {
		if(message[0].value.trim() !="") {
			reply();
		}
	});
});
```
- #### templates Folder
> Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document.\
> templates Directory
```
templates
|   index.html
```
- #### venv
>A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.\
- #### bot.py
> which is an instance of the Flask object. It'll act as the central configuration object for the entire application. It's used to set up pieces of the application required for extended functionality, e.g., a database connection and help with authentication.\
following code is taken from [bot.py](https://github.com/shivanidugade/College-Enquiry-Chatbot/blob/master/Chatbot/bot.py)
```python
kernel = aiml.Kernel()
kernel.learn('std-startup.xml')
kernel.respond('load aiml b')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<query>')
def api(query):
	response = kernel.respond(query)
	if response[:4] == 'http':
		return "<a href='" + response + "' target='_blank'>Click here for more info</a>"
	else:
		return kernel.respond(query)

if __name__ == '__main__':
	app.run(debug=True)
```
- #### std-startup.xml
> load the contents of an AIML file into the Kernel.
```xml
<aiml version = "1.0.1" encoding = "UTF-8">
<!-- This category works with the Standard AIML Set -->
<category>
<pattern>LOAD AIML B</pattern>
<template>
<!-- Load standard AIML set -->
<learn>data/*.aiml</learn>
</template>
</category>
</aiml>
```
