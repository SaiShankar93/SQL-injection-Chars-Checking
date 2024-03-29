from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def is_sanitized(input_string):
    sql_injection_chars = [';', '--', "'", '"', '/*', '*/', 'xp_', 'exec']
    for char in sql_injection_chars:
        if char in input_string:
            return False
    return True

@app.route('/')
def index():
    return '<h1>Go to the <a href="/v1/sanitized/input/">/v1/sanitized/input/</a> to view SQL injection characters check.</h1>'

@app.route('/v1/sanitized/input/', methods=['POST', 'GET'])
def sanitized_input():
    if request.method == 'POST':
        # print(request.form)
        input_string = request.form.get('text', '')
        # print("Received input:",input_string)
        if input_string == "":
            return jsonify({"result": "empty"})
        if is_sanitized(input_string):
            result = "sanitized"
        else:
            result = "unsanitized"
        return jsonify({"result": result})
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)