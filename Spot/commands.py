import os
import time
from spot_controller import SpotController
import math
import subprocess
from groq_ai import get_commands
# import cv2

# import cv2

ROBOT_IP = "192.168.80.3"#os.environ['ROBOT_IP']
SPOT_USERNAME = "admin"#os.environ['SPOT_USERNAME']
SPOT_PASSWORD = "2zqa8dgw7lor"#os.environ['SPOT_PASSWORD']

class SpotCommands:
    def __init__(self, spot: SpotController) -> None:
        self.spot = spot
        self.mic_process = None
        self.sample_name = "command.wav"
    def foward(self):
        self.spot.move_to_goal(goal_x=.5, goal_y=0)
        return

    def back(self):
        self.spot.move_to_goal(goal_x=-.5, goal_y=0)
        return

    def turnLeft(self):
        self.spot.move_by_velocity_control(v_x=0.0, v_y=0.0, v_rot=math.pi/2, cmd_duration=1)
        return

    def turnRight(self):
        self.spot.move_by_velocity_control(v_x=0.0, v_y=0.0, v_rot=-math.pi/2, cmd_duration=1)
        return

    def getCommands(self):
        
        print("Start recording audio")
        sample_name = "commands.wav"
        cmd = f'arecord -vv --format=cd --device={os.environ["AUDIO_INPUT_DEVICE"]} -r 48000 --duration=10 -c 1 {sample_name}'
        print(cmd)
        os.system(cmd)

        #API CALL TO DEEPGRAM HERE
        commands = get_commands(text)
        
        command_set = ["forward", "turnLeft", "turnRight", "back"]
        final_commands = text.split()
       



