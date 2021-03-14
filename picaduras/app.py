import web
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from flask import Flask, render_template



urls = ('/upload', 'Upload')

class Upload ():
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html>
        <html><head><meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<title>What stung me?</title>
	<!-- CSS only -->
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
     crossorigin="anonymous"></head><body><div class="container bg-light ">
     <center>
		<div class="row justify-content-center mt-4 pt-4">
			<div class="col-md-10 ">
            <a href="https://ibb.co/27Dn5xh"><img src="https://i.ibb.co/27Dn5xh/logo.png" alt="logo" border="0" ></a>
            <br>
            <br>
            <br>
             <label class="h1">What stung me?</label> <br>
             <br><br>
                 <form method="POST" enctype="multipart/form-data" action="">
                 <input type="file" name="myfile" />
                <br/><br/>
                <button  class="btn btn-secondary input type="submit"> Subir </button> <br> <br> 
                  </form>
        </center>
        </body>
        </div></<div>
        </html>



</html>"""

    def POST(self):
        x = web.input(myfile={})
        filedir = '/workspace/Picaduras/picaduras/static' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
     
        np.set_printoptions(suppress=True)
        # Disable scientific notation for clarity


            # Load the model
        model = tensorflow.keras.models.load_model('/workspace/Picaduras/picaduras/static/keras_model.h5')
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
        image = Image.open('/workspace/Picaduras/picaduras/static/'+filename)

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
        image_array = np.asarray(image)

# display the resized image
        image.show()

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

# run the inference
        prediction = model.predict(data)

        for i in prediction:
            if i[0] > 0.7: #araña
               return """<html>
                        <center>
                        <body>
                        <a href="https://ibb.co/myncGCD"><img src="https://i.ibb.co/NN0ys6V/ara-a-plantilla.jpg" alt="ara-a-plantilla" border="0"></a>
                        <center><input type="button" value="REGRESAR" onClick="history.go(-1);"></center>
                        </body>
                        </center>
                        </html>"""
            elif i[1] > 0.7: #abeja
               return """<html>
                        <center>
                        <body>
                        <a href="https://ibb.co/D7pMpjg"><img src="https://i.ibb.co/tbX2X1P/abeja-plantilla.jpg" alt="abeja-plantilla" border="0"></a>
                        <center><input type="button" value="REGRESAR" onClick="history.go(-1);"></center>
                        </body>
                        </center>
                        </html>"""
            elif i[2] > 0.7: #hormiga
                return """<html>
                        <center>
                        <body>
                        <a href="https://ibb.co/BjKNq8B"><img src="https://i.ibb.co/mtF86Q4/plantilla-hormiga.jpg" alt="plantilla-hormiga" border="0"></a>
                        <center><input type="button" value="REGRESAR" onClick="history.go(-1);"></center>
                        </body>
                        </center>
                        </html>"""
            elif i[3] > 0.7: #garrapata
                return """<html>
                        <center>
                        <body>
                        <a href="https://ibb.co/4TFRdpG"><img src="https://i.ibb.co/swg9HqG/plantilla-garrapata.jpg" alt="plantilla-garrapata" border="0"></a>
                        <center><input type="button" value="REGRESAR" onClick="history.go(-1);"></center>
                        </body>
                        </center>
                        </html>"""
            elif i[4] > 0.7: #mosquito
              return """<html>
                        <center>
                        <body>
                        <a href="https://ibb.co/rm8tdVn"><img src="https://i.ibb.co/xD9sFNV/mosquito-plantilla.jpg" alt="mosquito-plantilla" border="0"></a>
                        <center><input type="button" value="REGRESAR" onClick="history.go(-1);"></center>
                        </body>
                        </center>
                        </html>"""
            elif i[5] > 0.7: #pulga
                return """<html>
                        <center>
                        <body>
                        <a href="https://ibb.co/sCyGPwP"><img src="https://i.ibb.co/r34St6t/plantilla-pulga.jpg" alt="plantilla-pulga" border="0"></a>
                        <center><input type="button" value="REGRESAR" onClick="history.go(-1);"></center>
                        </body>
                        </center>
                        </html>"""
               
            elif i[6] > 0.7: #chinche
               return """<html>
                        <center>
                        <body>
                        <a href="https://ibb.co/CB1PK92"><img src="https://i.ibb.co/b1Wb5vJ/plantilla-chinche.jpg" alt="plantilla-chinche" border="0"></a>
                        <center><input type="button" value="REGRESAR" onClick="history.go(-1);"></center>
                        </body>
                        </center>
                        </html>"""
            else:
                return """<html>
                        <center>
                        <body>
                        <a href="https://ibb.co/pX7xTsT"><img src="https://i.ibb.co/gg238X8/plantilla-error.jpg" alt="plantilla-error" border="0"></a>
                        <center><input type="button" value="REGRESAR" onClick="history.go(-1);"></center>
                        </body>
                        </center>
                        </html>"""


if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()