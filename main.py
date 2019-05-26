from flask import Flask
from cow import Cow

app = Flask(__name__)

@app.route("/")
def hello():
	myCow = Cow("fortunes.txt")
	return("""<xmp>"""+str(myCow.speak())+"""</xmp>""")



