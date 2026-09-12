import os
import hashlib
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Antivirus001(App):

    def build(self):
        self.title = "Antivirus001"

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        titulo = Label(
            text="ANTIVIRUS 001",
            font_size=28
        )

        self.ruta = TextInput(
            text="laboratorio_antivirus",
            hint_text="Carpeta a analizar",
            multiline=False,
            size_hint_y=None,
            height=50
        )

        boton = Button(
            text="ANALIZAR CARPETA",
            size_hint_y=None,
            height=60
        )
        boton.bind(on_press=self.escanear)

        self.resultado = Label(
            text="Esperando análisis...",
            halign="left",
            valign="top"
        )

        layout.add_widget(titulo)
        layout.add_widget(self.ruta)
        layout.add_widget(boton)
        layout.add_widget(self.resultado)

        return layout

    def escanear(self, instancia):
        carpeta = self.ruta.text.strip()

        if not os.path.isdir(carpeta):
            self.resultado.text = "La carpeta no existe."
            return

        archivos = 0
        informe = []

        informe.append("=== INFORME ANTIVIRUS 001 ===")
        informe.append(f"Fecha: {datetime.now()}")
        informe.append("")

        for nombre in os.listdir(carpeta):
            ruta = os.path.join(carpeta, nombre)

            if os.path.isfile(ruta):
                try:
                    with open(ruta, "rb") as archivo:
                        hash_archivo = hashlib.sha256(
                            archivo.read()
                        ).hexdigest()

                    archivos += 1

                    informe.append(f"Archivo: {nombre}")
                    informe.append(f"SHA-256: {hash_archivo}")
                    informe.append("Resultado: NO DETECTADO")
                    informe.append("-" * 30)

                except Exception as error:
                    informe.append(
                        f"Error con {nombre}: {error}"
                    )

        informe.append("")
        informe.append(
            f"Archivos analizados: {archivos}"
        )

        texto_informe = "\n".join(informe)

        self.resultado.text = (
            "ANÁLISIS TERMINADO\n\n"
            f"Archivos analizados: {archivos}\n\n"
            "Informe guardado."
        )

        with open(
            "informe_antivirus.txt",
            "w"
        ) as archivo:
            archivo.write(texto_informe)


Antivirus001().run()
