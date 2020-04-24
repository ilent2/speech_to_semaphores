# Display a text string using semaphores
#
# Usage
#   from text_to_semaphores import Display
#   disp = Display()
#   disp.show('This is some text')

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

flags_dir = "flags"         # Directory containing flags

# Files names for each display signal
char_fnames = {

    # Alphabet
    'a' : '75px-Semaphore_Alpha.svg.png',
    'b' : '75px-Semaphore_Bravo.svg.png',
    'c' : '75px-Semaphore_Charlie.svg.png',
    'd' : '75px-Semaphore_Delta.svg.png',
    'e' : '75px-Semaphore_Echo.svg.png',
    'f' : '75px-Semaphore_Foxtrot.svg.png',
    'g' : '75px-Semaphore_Golf.svg.png',
    'h' : '75px-Semaphore_Hotel.svg.png',
    'i' : '75px-Semaphore_India.svg.png',
    'j' : '75px-Semaphore_Juliet.svg.png',
    'k' : '75px-Semaphore_Kilo.svg.png',
    'l' : '75px-Semaphore_Lima.svg.png',
    'm' : '75px-Semaphore_Mike.svg.png',
    'n' : '75px-Semaphore_November.svg.png',
    'o' : '75px-Semaphore_Oscar.svg.png',
    'p' : '75px-Semaphore_Papa.svg.png',
    'q' : '75px-Semaphore_Quebec.svg.png',
    'r' : '75px-Semaphore_Romeo.svg.png',
    's' : '75px-Semaphore_Sierra.svg.png',
    't' : '75px-Semaphore_Tango.svg.png',
    'u' : '75px-Semaphore_Uniform.svg.png',
    'v' : '75px-Semaphore_Victor.svg.png',
    'w' : '75px-Semaphore_Whiskey.svg.png',
    'x' : '75px-Semaphore_X-ray.svg.png',
    'y' : '75px-Semaphore_Yankee.svg.png',
    'z' : '75px-Semaphore_Zulu.svg.png',

    # Special signals
    ':error' : '75px-Semaphore_Error.svg.png',
    ':numeric' : '75px-Semaphore_Numeric.svg.png',
    ':alpha' : '75px-Semaphore_Juliet.svg.png',
    ':cancel' : '75px-Semaphore_Cancel.svg.png',
    ':ready' : '75px-Semaphore_Ready.svg.png',
    ':ok' : '75px-Semaphore_Charlie.svg.png',

    # Non-alpha characters
    ' ' : '75px-Semaphore_Ready.svg.png',
    '#' : '75px-Semaphore_Numeric.svg.png',
    '1' : '75px-Semaphore_Alpha.svg.png',
    '2' : '75px-Semaphore_Bravo.svg.png',
    '3' : '75px-Semaphore_Charlie.svg.png',
    '4' : '75px-Semaphore_Delta.svg.png',
    '5' : '75px-Semaphore_Echo.svg.png',
    '6' : '75px-Semaphore_Foxtrot.svg.png',
    '7' : '75px-Semaphore_Golf.svg.png',
    '8' : '75px-Semaphore_Hotel.svg.png',
    '9' : '75px-Semaphore_India.svg.png',
    '0' : '75px-Semaphore_Kilo.svg.png',
}

class Display(object):
    """ A class for displaying semaphore flag images """

    def __init__(self, delay=0.3):
        """ Loads the semaphore images and gets ready for displaying.

        disp = Display([delay=1.0])

        Creates a new display.  Sets the delay between displaying
        images, default 1 second.
        """

        self._delay = delay

        # Load the images using PIL
        self._images = {}
        for k, fname in char_fnames.items():
            fname = os.path.join(flags_dir, fname)
            self._images[k] = mpimg.imread(fname)

        # TODO: Open a window for display
        plt.ion()

    def _show_image(self, text, im, show_ascii):
        """ Display an image using matplotlib """

        # Display the image
        plt.cla()
        plt.imshow(im)
        plt.axis('image')

        # Display the ascii representation
        if show_ascii:
            plt.text(65, 10, text, fontsize=30)

        plt.pause(self._delay)

    def show(self, text, show_ascii=False):
        """ Display text using semaphore flags

        disp.show("test")
        Displays the flags

        disp.show("test", show_ascii=True)
        Also dispays the ASCII text
        """

        # Check if we have work to do
        if not text:
            im = self._images[':error']
            self._show_image('ER!', im, show_ascii)
            return

        # Display the contents of text
        for ch in text:
            im = self._images[ch.lower()]
            self._show_image(ch, im, show_ascii)

        # Display the ready message
        im = self._images[':ready']
        self._show_image('', im, show_ascii)


if __name__ == '__main__':

    test_string = "This is some text"
    disp = Display()
    disp.show(test_string, show_ascii=True)

