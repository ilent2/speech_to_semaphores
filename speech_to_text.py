# Speech to text conversion
#
# Based on the realpython.com tutorial
# https://realpython.com/python-speech-recognition/
#
# Usage
#   from speech_to_text import Listener
#   listener = Listener()
#   text = listener.listen()

import speech_recognition as sr

class Listener(object):
    """ A speech to text listener. """

    def __init__(self):

        # Setup the conversion object and microphone
        self._recognizer = sr.Recognizer()
        self._mic = sr.Microphone()

    def listen(self):
        """ Records some audio and attempts to translate it to text.

        Records audio until silence is detected.
        Waits a couple of moments before recording
        """

        # Record some audio
        with self._mic as source:
            self._recognizer.adjust_for_ambient_noise(source)
            print('listening...')
            audio = self._recognizer.listen(source)
            print('done')

        # Translate text
        try:
            text = self._recognizer.recognize_google(audio)

        except sr.RequestError:
            # API was unreachable or unresponsive
            print('request error')
            text = None

        except sr.UnknownValueError:
            # Speech was not matched
            print('translation error')
            text = None

        return text

if __name__ == '__main__':
    listener = Listener()
    text = listener.listen()
    print(text)

