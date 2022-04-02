from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    return ' \
        <div class="header"> \
        <h1 style="background-color:#007700">My Favourite Pet</h1> \
        </div> \
        <div> \
        <meta http-equiv="refresh" content="2"></meta> \
        <img src="https://media.istockphoto.com/photos/puppy-sleeping-by-the-fireplace-picture-id184928484"></img> \
        </div>'

if __name__ == "__main__":
    app.run()

