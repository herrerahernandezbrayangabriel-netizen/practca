import flet as flet
form sklear.feature_extraccion-text import CountVectorizer
fom sklearn.naive_bayes import MultinomialNB

preguntas =[
"hola, "holaa buenos dias", "buenas tardes", "buenas noches", "que tal", "como estas", "puedo preguntar lo que quiera ", 
"¿cuanto es 50+20?", "¿quien fuel el primer presidente de mexico", "¿como te llamas?", "¿la lokura es normal?", "¿que piensas de la programacion?, "¿el ser humano es bueno?",
"¿cuantos piases hay en el mundo?", "¿cuantos paises hay?", "¿el ser humano es inteligente?",
"¿que es python?", "¿santa closs es real?", "¿que hora es?", "cuentame un chiste", "cuentame otro chiste", 
"feliz año nuevo", "feliz navidad", "¿ que es un problema?" "feliz hallowen", "que es python", "como se independiso mexico"]
""

respuestas = [
    "¡hola! ¿Enque te puedo ayudar?", 
    "¡hola! ¿"Enque puedo ayudarte?"
    "que tal muy buenas noches en que puedo ayudarter", "muy bien y tu que tal", "muy bien y tu como va tu dia", "claro que si,pregunta lo que gustes",
    "el resultado es =70"
    "el primer presidente de mexico es (GUADALUPE VICTORIA)",
    "soy una inteligencia artificial", "la palabra lokura derivada a la inquietud, emocionalmente es normal", "Pienso que la programacion es un conjunto de conocimientos, que se desarrolla con una finalidad de superar a la realidad ",
    "la sifra conocida es de 195 países: Esta es la cifra más utilizada y generalmente se refiere a los 193 países miembros de la ONU más los dos Estados observadores (Ciudad del Vaticano y Palestina", "Un sacerdote le pregunta a un asesino convicto en la silla eléctrica: ¿Tiene algún último deseo? "Sí", responde el asesino. ¿Puede por favor tomar mi mano?", "el ser humano es inteligente una prueba simple estas las maquinas de computacion es un ejemplo de la inteligencia del ser humano y su razomaniento",
    "python es un leguaje de programacion que sirve para crear programas y crear para todo tipo de utilidades en la vida real", "santa closs no existe, es un cuento de adas para un personaje navideño", "no tengo acceso aun al clima", "Un marido le dice a su esposa: Cariño, ¿qué quieres que te regale por nuestro aniversario? ¿Un coche, un collar o un viaje? La esposa le responde: ¡Cariño, lo que yo quiero es que te compres una moto! Porque cada vez que salimos, me siento como si estuviera en un coche de segunda mano", 
    "mexico se independiso el 16 de septiembre de 1810, atraves de una guerra de once años en contra de los franceses", "el problema es un desacuerdo entre dos o tre sujetos",
    "sabes que las avejas pueden reconocer rostros humanos",]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(preguntas)


modelo = MultinomialNB()
modelo.fit(X, range(len(respuestas)))


def responder(mensaje: srt) -> srt:
    """Devuelve la respuesta mas problable para un mensaje"""

    X_test = vectorizer.transform([mensaje])
    idx =modelo.predict(X_test) [0]
    return respuestas[idx]

def main(page: ft.Page):
    page.title = "Asistente Virtual"
    page.theme_mode = ft.ThemeMode.DARK
    
    
    #lista de mensajes del chat

    chat = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=True,
    )

input_box = ft.TextField(
    hint_text="escribe tu mensaje...",
    autofocus=True,
    border_radius=20
    filled=True,
    bgcolor=ft.Colors.BLUE_GREY_800,
    color=ft.Colors.WHITE,
    on_submit=lambda e: enviari)

def burbuja(mensaje, es_usuario) :
    return ft.Row
    (   ft.Container(),
        content=ft.Text(
            mensaje,
            color=ft.Colors.WHITE if
es_usuario else ft.Colors.BLACK,
            selectable=True,
        ),
        padding=12,
        bgcolor=ft.Colors.BLUE_700 if
es_ususario else ft.Colors.GREY_200
            border_radius=20,
            aligment=ft.aligment.center_right if es_usuario else ft.aligment.center_left,
            margin=ft.margin.only(left=40)
            if es_usuario else
            ft.margin.only(right=40),
        )                   width=350,



    aligment=ft.MainAxisalAligment.END if
    es_usuario else ft.MainAxisaAligment.START,

    
def enviar():
    user_msg = input_box.value.strip()
    
    if not user_msg:
        return
    
    #AGREGAR MENSAJE DEL USUSARI
    chat.controls.append(burbuja(f"{user_msg}", True))
    bot.msg = responder(user_msg.lower())
    chat

    input_box.value = ""
    page.update()
    page.add(
        ft,Container(
            content=ft.Column(

                #encabezado
                ft.Row(




                    ft.Icon(ft.Icons.SMART_TOY, size=40, color=ft.Colors.BLUE_400),
                    ft.Text("asistente virtual", size=28, weight="bold",
                            color=ft.Colors.BLUE_100), 
        )nment.CENTER,


            ),


            ft.Container(
                chat,
                expand=True,
                height=450,
                bgcolor=ft.Colors.BLUE_GR
        EY_800,
                border_radius=15,
                padding=10,
                margin=ft.margin.only(top=10,botton=10),
                ft.Row(

                    input_box,
                    ft.IconButton(
                        icon=ft.Icons.SEND,
                        icon_color=ft.Colors.BLUE_400,
                        tooltip="enviar"
                        on_click=lambda
                        e: enviar(),

                    ),
                ),
                aligment=ft.MainAxisAligment.CENTER,
                expand=True,
                spacing=10,
                width=500,
                padding=20,
                border_radius=20,
                bgcolor=ft.Colors.BLUE_GREY_800,
                aligment=ft.aligment.center,






            )
    )


           