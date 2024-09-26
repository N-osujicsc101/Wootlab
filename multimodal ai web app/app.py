import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import google.generativeai as genai
import time

genai.configure(api_key="apikey")


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # Limit to 40MB
app.config["SECRET_KEY"] = "secretkey"


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "mp4", "mpeg", "pdf", "csv"}



def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/", methods=["GET", "POST"])
def index():
    result_text = None  
    uploaded_media_url = None  

    if request.method == "POST":
        
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files["file"]

      
        prompt = request.form.get("prompt", "")
        if not prompt:
            flash("No prompt provided")
            return redirect(request.url)

        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            # Set the uploaded media URL for displaying
            uploaded_media_url = url_for("static", filename=f"uploads/{filename}")

            # Use genai package to upload the file and interact with the model
            try:
                myfile = genai.upload_file(file_path)
                model = genai.GenerativeModel("gemini-1.5-pro")

                # Check whether the file is ready to be used.
                while myfile.state.name == "PROCESSING":
                    print(".", end="")
                    time.sleep(120)
                    myfile = genai.get_file(myfile.name)
                    print(f"Raw response: {myfile}")

                if myfile.state.name == "FAILED":
                    raise ValueError(f"File processing failed: {myfile.state.name}")

                # Generate content based on the file and the provided prompt
                result = model.generate_content(
                    [myfile, prompt], request_options={"timeout": 600}
                )

                # Debugging: print the raw result to inspect it
                print(f"Raw response: {result}")

                # Extracting the response text safely
                result_text = (
                    result.text
                    if hasattr(result, "text")
                    else "Unable to generate response at the moment. Try again later"
                )
            except Exception as e:
                flash(f"An error occurred: {e}")
                return redirect(request.url)

   
    return render_template(
        "index.html", result_text=result_text, uploaded_media_url=uploaded_media_url
    )


if __name__ == "__main__":
  
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    app.run(debug=True)
