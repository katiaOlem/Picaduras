import web, shutil
from web import form
import os
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import json
from os import remove
from os import path

urls = ('/upload', 'Upload')

class Upload(object):

    def POST(self):
        x = web.input(myfile={})
        filedir = '/workspace/Picaduras/picaduras/static/'
        if 'myfile' in x:
            filepath=x.myfile.filename.replace('\\','/')
            filename=filepath.split('/')[-1]
            fout = open(filedir +'/'+ filename,'wb')
            fout.write(x.myfile.file.read())
            fout.close()
            np.set_printoptions(suppress=True)

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
                if i[0] > 0.85:
                    titulo = " Te pico una abeja"
                    resultado = "El dolor es muy intenso asi que tienes que tener cuidado. ¡OJO SI ERES ALERGICO ACUDE RAPIDDO A UN MEDICO!"
                    descripcion = "Lavar la zona afectada con agua y con jabon. Enfriar la picadura con hielo. Aplicar un antiséptico. Nunca se debe de apretar la picadura de abeja o avispa para tratar de sacar el veneno, ya que este puede extenderse. Se puede paliar el dolor y las molestias con una crema para el picor y un antihistamínico"
                    status = 200

                elif i[1] > 0.85:
                    titulo = "Te pico un mosquito"
                    resultado = "No te preocupes, una picadura de mosco no es grave. ¡OJO SI ERES ALERGICO ACUDE RAPIDDO A UN MEDICO!"
                    descripcion = "Aplica loción, crema o pasta. Aplicar una loción de calamina o una crema de hidrocortisona de venta libre en la picadura puede ayudar a aliviar la picazón. O bien, prueba a untar la picadura con una pasta preparada con bicarbonato de sodio y agua. Vuelve a aplicarla varias veces al día hasta que los síntomas desaparezcan."
                    status = 200

                elif i[2] > 0.85:
                    titulo = "Te pico una chinche"
                    resultado = "No tienes de que preocuparte no es nada grave. ¡OJO SI ERES ALERGICO ACUDE RAPIDDO A UN MEDICO!"
                    descripcion = "Si crees que te ha picado una chinche, lava la picadura con agua y jabón y ponte loción de calamina para aliviar el picor. Un adulto puede conseguir una crema para aliviar la picazón en una farmacia o droguería. Intenta rascar la picadura lo menos posible porque se te podría infectar."
                    status = 200

                elif i[3] > 0.85:
                    titulo = "Te pico una garrapata"
                    resultado = "Si te pico una garrapata tienes que tener cuidado, porque pueden trasmitirte enfermedades graves"
                    descripcion = "Utiliza pinzas pequeñas o de punta fina para agarrar la garrapata lo más cerca posible de la piel. Saca suavemente la garrapata con un movimiento ascendente lento y constante. No la retuerzas ni la aprietes. No agarres la garrapata con las manos desprotegidas. Los expertos no recomiendan usar vaselina, esmalte de uñas ni cerillas (fósforos) calientes para quitar garrapatas."
                    status = 200

                elif i[4] > 0.85:
                    titulo = "Te pico una Hormiga"
                    resultado = "No tienes de que preocuparte no es grave solo tendras un leve hinchazón ¡OJO SI ERES ALERGICO ACUDE RAPIDO A UN MEDICO!"
                    descripcion = "Si alguna vez crees que te ha picado una hormiga.  El veneno de las picaduras de hormigas coloradas puede producir una ligera hinchazón en la zona de la picadura, y puede que el médico quiera echarle un vistazo para asegurarse de que no tienes una reacción alérgica."
                    status = 200

                elif i[5] > 0.85:
                    titulo = "Te pico una Pulga"
                    resultado = "No tienes de que preocuparte no es grave solo tendras un leve hinchazón ¡OJO SI ERES ALERGICO ACUDE RAPIDO A UN MEDICO!"
                    descripcion = "Si crees que te ha picado una pulga, lava la picadura con agua y jabón. Aplica loción de calamina para aliviar la picazón, o un adulto puede conseguirse en la farmacia una crema que alivie la picazón. Trata de no rascarte demasiado porque las picaduras podrían infectarse."
                    status = 200

                elif i[6] > 0.85:
                    titulo = "Te pico una Araña"
                    resultado = "Puedes presentar dolor muy severo ¡OJO SI ERES ALERGICO ACUDE RAPIDO A UN MEDICO!"
                    descripcion = "Lave el área afectada con agua y jabón. Aplique hielo o una compresa húmeda. Si necesita, tome un medicamento para el dolor de venta libre. Considere tomar remedios para la alergia en caso de hinchazón severa. Busque tratamiento médico para niños y adultos con síntomas graves. Lave el área afectada con agua y jabón  Aplique hielo o una compresa húmeda.Si necesita, tome un medicamento para el dolor de venta libre. Considere tomar remedios para la alergia en caso de hinchazón severa Busque tratamiento médico para niños y adultos con síntomas graves"
                    status = 200    


                else:  
                    titulo = "Hay un error"
                    resultado = "La imagen que nos eviaste no la reconosemos, puedes intentar con otra imagen "
                    descripcion = "Al paracer no es una imagen de una picadura"
                    status = 404
                
                if path.exists(filedir+filename):
                    remove(filedir+filename)
        datos = {
            titulo: [
            ]
        }

        picadura = {}
        picadura["resultado"] = resultado
        picadura["descripcion"] = descripcion
        picadura["status"] = status
        datos[titulo].append(picadura)
        return json.dumps(datos)
        
        

if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()