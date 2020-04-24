
speech_to_semaphores
####################

Python speech to (maritime) semaphore flags.
Tools for converts speech to text and displaying the corresponding
[semaphore](https://en.wikipedia.org/wiki/Flag_semaphore) flags.
Very little practical purposes, may be useful for communicating with
similarly inclined friends via Zoom during a Pandemic lock-down.

Requirements
============

  * Python (2.7, but should work with 3.x)
  * SpeechRecognition (3.8.1)
  * matplotlib (2.0)
  * pyaudio (0.2.11)

Example usage
=============

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

