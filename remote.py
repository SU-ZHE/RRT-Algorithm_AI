import time

import cv2
import math
import numpy as np

import sim

# Close all the connections.
sim.simxFinish(-1)
# Connect the V-REP.
clientID = sim.simxStart("127.0.0.1", 19999, True, True, 5000, 5)

# Get object handles.
_, bot = sim.simxGetObjectHandle(clientID, 'MyBot', sim.simx_opmode_oneshot_wait)
_, vision_sensor = sim.simxGetObjectHandle(clientID, 'Vision_Sensor', sim.simx_opmode_oneshot_wait)
_, left_motor = sim.simxGetObjectHandle(clientID, 'Left_Motor', sim.simx_opmode_oneshot_wait)
_, right_motor = sim.simxGetObjectHandle(clientID, 'Right_Motor', sim.simx_opmode_oneshot_wait)

if clientID == -1:
    raise Exception("Fail to connect remote API server.")


def init():
    """Initialize the simulation.
    """
    sim.simxGetVisionSensorImage(clientID, vision_sensor, 0, sim.simx_opmode_streaming)
    time.sleep(1)


def get_image(sensor):
    """Retrieve a binary image from Vision Sensor.

    :return: a binary image represented by numpy.ndarray from Vision Sensor
    """
    err, resolution, raw = sim.simxGetVisionSensorImage(clientID, sensor, 0, sim.simx_opmode_buffer)
    if err == sim.simx_return_ok:
        img = np.array(raw, dtype=np.uint8)
        img.resize([resolution[1], resolution[0], 3])
        # Process the raw image.
        _, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
        g = cv2.cvtColor(th1, cv2.COLOR_BGR2GRAY)
        _, th2 = cv2.threshold(g, 250, 255, cv2.THRESH_BINARY)
        # Find the edges using Canny.
        edge = cv2.Canny(th2, 50, 150)  # type: np.ndarray
        return edge
    else:
        return None


def move(v, o):
    """Move the robot.
    :param v: desired velocity
    :param o: desired angular velocity
    """
    wheel_radius = 0.027
    distance = 0.119
    v_l = v - o * distance
    v_r = v + o * distance
    o_l = v_l / wheel_radius
    o_r = v_r / wheel_radius
    sim.simxSetJointTargetVelocity(clientID, left_motor, o_l, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, right_motor, o_r, sim.simx_opmode_oneshot)


def get_beta_angle():
    """Return the degrees of Beta Euler Angle.

    :return: the degrees of Beta Euler Angle
    """
    _, euler_angles = sim.simxGetObjectOrientation(clientID, bot, -1, sim.simx_opmode_oneshot_wait)
    ret = math.degrees(euler_angles[1])
    if euler_angles[0] <= 0 < ret:
        return 180 - ret
    if euler_angles[2] <= 0 and ret < 0:
        return -180 - ret
    return ret
