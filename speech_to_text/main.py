"""
    Autor: Iago Magalhães
    Descrição:
        - Programa speech to text utilizando a lib SpeechRecognition
        - Capta audio com microfone do computador
        - Abre alguns aplicativos por comando de voz (Ex: Chorme e Excel)
"""

import speech_recognition as sr
import os

def ouvir_microfone():
    """
        Função para ouvir microfone do computador
        :return: retorna uma string com o valor captado pelo microfone
    """
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('Diga alguma coisa: ')
        audio = microfone.listen(source)
    
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        if('navegador' in frase):
            os.system("start Chrome.exe")
        elif('Excel' in frase):
            os.system("start Excel.exe")
        print('Você disse: ' + frase)
    except sr.UnknownValueError:
        print('Não entendi!')
    return frase

ouvir_microfone()