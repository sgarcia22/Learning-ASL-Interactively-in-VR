import csv
import os.path
import time
import collections
import Leap, sys, thread, time, math
from Leap import Bone

def getData(controller):
    frame = controller.frame()
    try:
        handList = frame.hands
        if len(handList) != 1:
            raise Exception('Incorrect Number of Hands')
        currentHand = handList[0]
        fingers = currentHand.fingers
        palmPosition = currentHand.palm_position
        allBones = []
        for finger in fingers:
            allBones.append(finger.bone(Bone.TYPE_METACARPAL).next_joint)
            allBones.append(finger.bone(Bone.TYPE_PROXIMAL).next_joint)
            allBones.append(finger.bone(Bone.TYPE_INTERMEDIATE).next_joint)
            allBones.append(finger.bone(Bone.TYPE_DISTAL).next_joint)
        orderedResult = collections.OrderedDict()
        index = 0
        for bone in allBones:
            #Calculate distance from bone to center of palm
            distance = bone.distance_to(palmPosition)
            orderedResult["featureID#"+str(index)] = distance
            index += 1
        return orderedResult
    except Exception as err:
        print('Caught this error: ' + repr(err))
    return None

def storeData(char, data):
    values = data.values()
    keys = data.keys()
    values.insert(0, char)
    keys.insert(0, "character")
    try:
        if os.path.exists("data.csv") == False:
            #make file
            f = open("data.csv","wb+")
            writer = csv.writer(f)
            writer.writerow(keys)
            f.close()
        with open('data.csv', 'ab+') as f:
            writer=csv.writer(f)
            writer.writerow(values)
            f.close()
    except Exception as err:
        print('Caught this error: ' + repr(err))
    return

def countdown():
    count = 3
    while count > 0:
        print(count)
        time.sleep(1)
        count -= 1

def getChar(controller):
    while (True):
        char = raw_input("Enter the character: ")
        countdown()
        data = getData(controller)
        if data == None:
            continue
        storeData(char, data)
        time.sleep(2)
        if char == "exit":
            sys.exit()

def main():
    controller = Leap.Controller() #Leap Motion Controller Attached to Computer
    controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
    getChar(controller)

if __name__ == "__main__":
    main()