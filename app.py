from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_data = request.form['input_data']

    # Use the input_data in your Python code
    # For example, print it to the console
    print(f"Received input: {input_data}")

    # You can also pass the input_data to another function or process it as needed

    return f"Input received: {input_data}"
wantedVar = process()
if __name__ == '__main__':
    app.run(debug=True)