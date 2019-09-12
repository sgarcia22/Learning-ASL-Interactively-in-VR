import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeapMotionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_Names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    # On Leap Motion Initialized
    def on_init(self, controller):
        print "Initialized"

    # On sensor connect
    def on_connect(self, controller):
        print "Motion Sensor Connected"

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    # On sensor disconnect
    def on_disconnect(self, controller):
        print "Motion Sensor Disconnected"

    # End Program
    def on_exit(self, controller):
        print "Exited"
    
    # 290 frames per second
    # Access to data of frame
    def on_frame(self, controller):
        frame = controller.frame()

        # Unique ID Per Frame
        # Timestamp: Microseconds since Leap has started
        """print "Frame ID: " + str(frame.id) \
            + " Timestamp: " + str(frame.timestamp) \
            + " # of Hands: " + str(len(frame.hands)) \
            + " # of Fingers: " + str(len(frame.fingers)) \
            + " # of Tools: " + str(len(frame.tools)) \
            + " # of Gestures: " + str(len(frame.gestures()))"""

        for hand in frame.hands:
            handType = "Left Hand" if hand.is_left else "Right Hand"
        
            print handType + " Hand ID: " + str(hand.id) + " Palm Position: " \
                + str(hand.palm_position)

            normal = hand.palm_normal
            direction = hand.direction

            print "Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) \
                + "Roll: " + str(normal.row * Leap.RAD_TO_DEG) \
                + "Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG)

def main():
    listener = LeapMotionListener()
    controller = Leap.Controller() #Leap Motion Controller Attached to Computer

    controller.add_listener(listener)

    print "Press enter to quit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()