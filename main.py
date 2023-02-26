from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


df = pd.read_csv("dictionary.csv")


@app.route('/api/v1/<word>')
def test(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    if type(definition) is not str:
        return {"error": f"{word} is not in our dictionary"}
    return {"word": word,
            "definition": definition}


if __name__ == '__main__':
    app.run(debug=True)
