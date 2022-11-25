from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/",methods=['GET'])
def root():
    return "<h1>Ответ на запрос GET</h1>"


@app.route ("/user", methods=['GET'])
def user():
     name = "Алина"
     group = "ИБМ7-31Б"
     marks = [5,4,3,4,5,5]
     return render_template('user.html',name = name, group = group, marks = marks)

@app.route ("/student", methods=['GET'])
def summ():
    name = str(request.args.get("name"))
    group = str(request.args.get("group"))
    marks = request.args.get("marks")

    return render_template('user.html',name = name, group = group, marks = marks)


if __name__ == "__main__":
    app.run(debug=True)


