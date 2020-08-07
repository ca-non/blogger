from Flaskblog import create_app

app = create_app() # using config class as default

if __name__ == '__main__':
	app.run(debug=True)

