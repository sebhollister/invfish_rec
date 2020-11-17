# invfish_rec
Code base for Invasive Fish Recognition Project CreateX Senior Capstone Fall 2020

# Directions for PI 
1. Plug in hdmi, keyboard, mouse, and camera to pi
2. Plug in power, should see screen turn on (hit ok / exit all warnings and errors, then cancel on the "welcome to raspberry pi desktop" message)
3. Open terminal by pressing ```Ctrl-alt-t``` or icon in top left
4. To see live real-time video from Camera: 
    - Type command ```raspistill -t 0``` in terminal 
    - To exit back to terminal press ```Ctrl+C```
    - This is ideal for **getting the lens focus correct** because you can see realtime what the camera is looking at
5. To run model on live image, type ```python call_model_live.py```. This is a simple script that capture a single image from the camera then runs image recognition on it.
    - It saves the image captured as ```image.jpg```, then prints the image classification
    - To see what image it took, run ```feh image.jpg```
6. **IMPORTANT**: Before running any scripts, run the command  ```conda activate py36``` to set up the correct python environment
    - Also please don't install any libraries or make any major edits to the files without letting me know, the environment on the PI takes a long time to get setup
7. To **shutdown PI**: run ```sudo halt``` , wait for the green light to stop blinking (only red light should be on, this should take like 15 seconds) and then unplug. 
    - If PI freezes or stops working, just unplug and plug back in. This will be a hard reset and is fine
