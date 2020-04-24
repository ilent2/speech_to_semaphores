
Speech to Semaphores
====================

Python speech to (maritime) semaphore flags.
Tools for converts speech to text and displaying the corresponding
[semaphore](https://en.wikipedia.org/wiki/Flag_semaphore) flags.
Very little practical purposes, may be useful for communicating with
similarly inclined friends via Zoom during a Pandemic lock-down.

Requirements
------------

  * Python (2.7 | 3.6)
  * SpeechRecognition (3.8.1)
  * matplotlib (2.0 | 3.2.1)
  * pyaudio (0.2.11)
  * gif (1.0.3, required for gif generation)

Example usage
-------------

Either run from the command line

```bash
python speech_to_semaphores.py
```

or from the python interpreter

```python
from speech_to_semaphores import SpeakSemaphores
joke = SpeakSemaphores()
joke.run()
```

Use a keyboard interrupt `Ctrl+C` to stop the program.

You can also display ASCII characters with

```python
joke.run(show_ascii=True)
```

Generate a gif
--------------

You can also use the Semaphore generator to create a GIF

```python
from text_to_semaphores import Display
test_string = "OH CATHERINE   OH HEATHCLIFFE"
disp = Display()
disp.to_gif("test.gif", test_string, show_ascii=True, duration=500)
```

![Wuthering Heights](/example_gif/heights.gif)

