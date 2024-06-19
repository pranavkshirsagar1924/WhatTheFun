from flask import Flask,render_template,jsonify,request
import applox as ap
app = Flask(__name__)

@app.route('/')
def template():
    return render_template("index.html")

@app.route('/comment',methods=['GET'])
def make_comment():
    args = request.args.get('data')
    return jsonify({'stat':ap.predict_nsfw(args)})

