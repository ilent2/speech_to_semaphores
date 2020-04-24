# Converts from speech to semaphores
#
# Uses speech_to_text and text_to_semaphores
#
# Usage
#   joke = SpeakSemaphores()
#   joke.run()
#   # Speak some text, watch the result, press Ctrl+C to stop

from speech_to_text import Listener
from text_to_semaphores import Display

class SpeakSemaphores(object):
    """ A speech to semaphore converter """

    def __init__(self):
        """ Set-up the display and listener objects """

        self._display = Display()
        self._listener = Listener()

    def run(self):
        """ Run the joke (convert from text to semaphores) """

        while True:

            # Get some text
            text = self._listener.listen()
            if not text:
                return

            # Display the result
            self._display.show(text)

if __name__ == '__main__':
    joke = SpeakSemaphores()
    joke.run()

