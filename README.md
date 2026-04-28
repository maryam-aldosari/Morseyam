# final-project

Hello, everyone!



(CORRECTION: FILE SHOWCASED IN THE VIDEO IS THE READER FILE NOT SENDER, I HAVE ATTACHED BOTH TO THE REPO).

Thank you for reviewing my project. 

The video above consist of 3 clips:
  - Demoing the project.
  - The video of the arduinos as the LED flashes when I typed "send_message("python project") in the demo video.
  - A close-up of the hardware and a brief explaination of how it works.

CODE:
There are a few things that I had forgot to mention, one being is the way I obtained the webrpl link for both arduinos is that I connected to each arduinos and ran the "boot.py" and afterwards I hit CTRL-D and once I do I'd be given a unique link. I do this to both arduinos and once I have them I open the WebRPL website and connect to each arduino's unique WebRPL link. From there, we could send codes directly from online instead of having to do it over, and over again. 

During the project, the way that I tracked the voltage so that I'd be able to code accordingly is found in the "main_reader.py" file on line 19. Simply
removing the comment and then saving and running the file will show you the current voltage/brightness its picking up.

HARDWARE:
As for hardware, as you'll see in an attached video, It's sort of in a rather weird setting, the reason being is that the photoresister in which it picks up the flashes(voltage), is EXTREMELY sensitive and I settled on placing it there to keep the voltage from changing drastically. What will happen if it were to change is that it'll mix up the letters which will lead me to constantly having to change the "led_threshold". 
