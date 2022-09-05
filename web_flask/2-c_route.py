#!/usr/bin/python3
""" route """


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        """root folder route"""
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb_route():
        """/hbnb/ folder route"""
        return "HBNB"

    @app.route('/c/<text>', strict_slashes=False)
    def replace_text(text):
        """some text in uotput depending on url after /c/"""
        return "C " + text.replace('_', ' ')

    app.run(host='0.0.0.0')