from flask import Flask
from flask import render_template
import glob
import os
from datetime import datetime

app = Flask("Namie")

@app.route("/")
def root():
  ds = glob.glob("articles/*")
  result = []
  for d in ds:
    fs = glob.glob(d + "/*.txt")
    t = (d.split("/")[-1] , len(fs))
    result.append(t)
  return render_template("index.html" , d=result)


@app.route("/category/<c>")
def category(c):
  fs = glob.glob("articles/" + c  + "/*.txt")
  result = []
  for i,d in enumerate(fs):
    a = open(d)
    article = a.read()
    a.close()
    dsplit = d.split("/")[-1].replace(".txt" , "")
    m = os.path.getmtime(d)
    z = str(datetime.utcfromtimestamp(m))
    t = (i, dsplit , z, article)
    result.append(t)
  return render_template("category.html" , d = result)

@app.route("/article/<e>")
def article(e):
  articles = glob.glob("articles/" + e  + "/*.txt")
  result = []
  for d in articles:
    artsplit = d.split("/")[-1].replace(".txt" , "")
    result.append(artsplit)
  return render_template("article.html" , d = result)
if __name__ == "__main__":
  app.run(debug=True , port = '3000' , host = '0.0.0.0')

