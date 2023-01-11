from flask import Flask,render_template
import requests
from flask import request as req

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
   return render_template("index.html")

@app.route("/Summarise",methods=["GET","POST"])
def Summarise():
    if req.method=="POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

        textInput=req.form["data"]

        def query(payload):
            
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        maxL=int(req.form["maxL"])
        minL=maxL//4
        output = query({
            "inputs": textInput,
            "parameters": {"min_length":minL,"max_length":maxL},
        })[0]
        return render_template("index.html",result=output["summary_text"])
    else:
        return render_template("index.html")
if __name__=='__main__':
    app.run()