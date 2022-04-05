from msilib.schema import File
from stringprep import map_table_b3
from flask import Flask, render_template, request, url_for, redirect, send_file, session
from numpy import tile
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            return render_template("error.html") 
        return render_template("download.html", url = url)
    return render_template("home.html")

@app.route("/download", methods = ["GET", "POST"])
def download_video():
    if request.method == "POST":
        
        buffer = BytesIO()
        url = YouTube(session['link'])
        itag = request.form.get("itag")
        video = url.streams.get_by_itag(itag)  
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=url.title +".mp4", mimetype="videos/mp4")
    return redirect(url_for("home"))



@app.route("/downloada", methods = ["GET", "POST"])
def download_song():
    if request.method == "POST":
        
        buffer = BytesIO()
        url = YouTube(session['link'])
        itag = request.form.get("itag")
        video = url.streams.get_by_itag(itag)  
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=url.title +".mp3", mimetype="videos/mp4")
    return redirect(url_for("songa"))



if __name__ == '__main__':
    app.run(debug=True)