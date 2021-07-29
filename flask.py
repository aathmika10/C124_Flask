from flask import Flask,jsonify,request

app = Flask(__name__)
tasks=[
    {
        "id":1,
        "title":u"Buy groceries",
        "description":u"Milk , fruits",
        "done":False,
    },
    {
        "id":2,
        "title":u"Buy stationaries",
        "description":u"Pen , Notebook",
        "done":False,
    }
]
@app.route("/")

def helloWorld():
    return "Hello World"

@app.route("/addData",methods=["POST"])

def addTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide data"
        },400)
    task={
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False,
    }
    tasks.append(task)
    return jsonify({
            "status":"success",
            "message":"Task added successfully"
        })

@app.route("/getData")

def getTask():
    return jsonify({
        "data":tasks
    })

if(__name__=="__main__"):
    app.run(debug=True)
