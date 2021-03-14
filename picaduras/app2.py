from flask import Flask, render_template

app= Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/mosquito')
def mosquito():
    return render_template('mosquito.html')
if __name__ == '__main__':
        app.run(debug=True)

"""<html><head><meta charset="utf-8">
	            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	            <title>Mosquito</title>
	            <!-- CSS only -->
	            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                crossorigin="anonymous"></head><body><div class="container bg-light ">
                <center>
		            <div class="row justify-content-center mt-4 pt-4">
			        <div class="col-md-10 ">
                    <a href="https://ibb.co/6R8Ythq"><img src="https://i.ibb.co/jvzhwKj/89973373-mosquito-cdc.jpg" alt="89973373-mosquito-cdc" border="0"></a>
                    <br>
                    <body>
                        <h1>Te pico un Mosquito</h1>
                        <h5>Aplica loción, crema o pasta. Aplicar una loción de calamina o una crema de hidrocortisona de venta libre en la picadura puede ayudar a aliviar la picazón. O bien, prueba a untar la picadura con una pasta preparada con bicarbonato de sodio y agua. Vuelve a aplicarla varias veces al día hasta que los síntomas desaparezcan.
Aplica una compresa fría. Intenta calmar la picadura aplicando una compresa fría o un paño frío y húmedo durante unos minutos.
Toma un antihistamínico oral. Para las reacciones más fuertes, prueba tomando un antihistamínico de venta libre (Benadryl, Chlor-Trimeton y otros).</h5>
                    </body>
                </html>"""