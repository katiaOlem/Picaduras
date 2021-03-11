import web, shutil
from web import form
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np



urls = ('/upload', 'Upload')

class Upload():
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        filedir = '/workspace/Picaduras/picaduras/static' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        raise web.seeother('/upload')
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
        inicio = "<html lang='es'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'><title>Qué me pico? </title><!-- CSS only -->	<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1' crossorigin='anonymous'><link rel='icon' href='logo.png' type='image/png' /></head><body>    <div class='container bg-light '>		<div class='row justify-content-center mt-4 pt-4'>			<div class='col-md-8 '>"
        final = "</div>        </div>    </div></body></html>"

        for i in prediction:
            if i[0] > 0.7:
                print("Picadura de araña")
                picadura= inicio+"<h1 class= font-italic class='text-danger text-center'>Te ha picado una abeja .</h1> <br> <br> <h2 class='text-info'>Remedio Casero:</h2> <h3>Para las reacciones leves a moderadas, el tratamiento consiste en quitar el aguijón, lavar la zona con agua y jabón, y aplicar compresas de hielo. Las cremas en la zona afectada pueden reducir el malestar. Las reacciones más graves pueden necesitar epinefrina.</h3><br><br><img src='https://isanidad.com/wp-content/uploads/importado/6648.jpg' align='center' width='300' height='275'> <br><br>"+final
            elif i[1] > 0.7:
                print("picadura de Abeja")
                picadura= inicio+"<h1 class= font-italic class='text-danger text-center'>Te ha picado una abeja .</h1> <br> <br> <h2 class='text-info'>Remedio Casero:</h2> <h3>Para las reacciones leves a moderadas, el tratamiento consiste en quitar el aguijón, lavar la zona con agua y jabón, y aplicar compresas de hielo. Las cremas en la zona afectada pueden reducir el malestar. Las reacciones más graves pueden necesitar epinefrina.</h3><br><br><img src='https://isanidad.com/wp-content/uploads/importado/6648.jpg' align='center' width='300' height='275'> <br><br>"+final
            elif i[2] > 0.7:
                print("Picadura de Hormiga")
                picadura= inicio+"<h1 class= font-italic class='text-danger text-center'>Te ha picado una abeja .</h1> <br> <br> <h2 class='text-info'>Remedio Casero:</h2> <h3>Para las reacciones leves a moderadas, el tratamiento consiste en quitar el aguijón, lavar la zona con agua y jabón, y aplicar compresas de hielo. Las cremas en la zona afectada pueden reducir el malestar. Las reacciones más graves pueden necesitar epinefrina.</h3><br><br><img src='https://isanidad.com/wp-content/uploads/importado/6648.jpg' align='center' width='300' height='275'> <br><br>"+final
            elif i[3] > 0.7:
                print("Picadura de Garrapata")
                picadura= inicio+"<h1 class= font-italic class='text-danger text-center'>Te ha picado una abeja .</h1> <br> <br> <h2 class='text-info'>Remedio Casero:</h2> <h3>Para las reacciones leves a moderadas, el tratamiento consiste en quitar el aguijón, lavar la zona con agua y jabón, y aplicar compresas de hielo. Las cremas en la zona afectada pueden reducir el malestar. Las reacciones más graves pueden necesitar epinefrina.</h3><br><br><img src='https://isanidad.com/wp-content/uploads/importado/6648.jpg' align='center' width='300' height='275'> <br><br>"+final
            elif i[4] > 0.7:
                print("Picadura de Mosquito")
                picadura= inicio+"<h1 class= font-italic class='text-danger text-center'>Te ha picado una abeja .</h1> <br> <br> <h2 class='text-info'>Remedio Casero:</h2> <h3>Para las reacciones leves a moderadas, el tratamiento consiste en quitar el aguijón, lavar la zona con agua y jabón, y aplicar compresas de hielo. Las cremas en la zona afectada pueden reducir el malestar. Las reacciones más graves pueden necesitar epinefrina.</h3><br><br><img src='https://isanidad.com/wp-content/uploads/importado/6648.jpg' align='center' width='300' height='275'> <br><br>"+final
            elif i[5] > 0.7:
                print("Picadura de Pulga")
                picadura= inicio+"<h1 class= font-italic class='text-danger text-center'>Te ha picado una abeja .</h1> <br> <br> <h2 class='text-info'>Remedio Casero:</h2> <h3>Para las reacciones leves a moderadas, el tratamiento consiste en quitar el aguijón, lavar la zona con agua y jabón, y aplicar compresas de hielo. Las cremas en la zona afectada pueden reducir el malestar. Las reacciones más graves pueden necesitar epinefrina.</h3><br><br><img src='https://isanidad.com/wp-content/uploads/importado/6648.jpg' align='center' width='300' height='275'> <br><br>"+final
            elif i[6] > 0.7:
                print("Picadura de Chinche")
                picadura= inicio+"<h1 class= font-italic class='text-danger text-center'>Te ha picado una abeja .</h1> <br> <br> <h2 class='text-info'>Remedio Casero:</h2> <h3>Para las reacciones leves a moderadas, el tratamiento consiste en quitar el aguijón, lavar la zona con agua y jabón, y aplicar compresas de hielo. Las cremas en la zona afectada pueden reducir el malestar. Las reacciones más graves pueden necesitar epinefrina.</h3><br><br><img src='https://isanidad.com/wp-content/uploads/importado/6648.jpg' align='center' width='300' height='275'> <br><br>"+final
            else:
                print("Imagen no reconocida")
        
            return picadura



if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()