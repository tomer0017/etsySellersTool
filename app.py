from flask import Flask ,render_template,url_for,request
from bs4 import BeautifulSoup
import tomer_etsy_tool as tet
# import tomer_etsy_tool
import requests
import sys
app= Flask(__name__)

@app.errorhandler(404)
def not_found(e):

  return "<h1> 404 - Page Not Found </br> usage: </br> /roomName - for send a message </br> /chat/roomName - for messages history </h1>  "



@app.route("/")

def home():
    # print1()
    return render_template('index.html')


@app.route("/<room>",methods=["POST","GET"])
def room(room):

    if request.method == "POST":

        search_val=request.form["search_val"]

    # return render_template('index.html')

        # return (tet.user_search(search_val))
        return render_template('index.html',res=tet.user_search(search_val))
    return (room)



if __name__=="__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)            