import web, shutil
from web import form
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

render = web.template.render("picaduras/")

fileForm = form.Form(form.File('myfile'))

class Index(object):
    def Get(self):
        datos = fileForm()
        return render.index(datos)
    
    def POST(self):
        x = web.input(myfile={})
        filedir ='/workspace/Picaduras/picaduras/static/'
        if 'myfile' in x:
            filepath=x.myfile.filename.replace('\\','/')
            filename=filepath.split('/')[-1]
            fout = open(filedir +'/'+ filename,'wb')
            fout.write(x.myfile.file.read())
            fout.close()
         
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
  if i[0] > 0.7:
    print("Picadura de araña")
  elif i[1] > 0.7:
    print("picadura de Abeja")
  elif i[2] > 0.7:
    print("Picadura de Hormiga")
  elif i[3] > 0.7:
    print("Picadura de Garrapata")
  elif i[4] > 0.7:
    print("Picadura de Mosquito")
  elif i[5] > 0.7:
    print("Picadura de Pulga")
  elif i[6] > 0.7:
    print("Picadura de Chinche")
  else:
    print("Imagen no reconocida")
  
