
## Command to make the file run ##
#
# sudo '../../../mnt/c/Program Files/Blender Foundation/Blender 3.2/blender.exe'  -b -P importscript.py -- 1 1 1
#
## ARGV ##
#ARGV[0] - Convert fbx files into obj files for each frame 1=YES 0=NO
#ARGV[1] - Convert obj files into STL files 1=YES 0=NO
#ARGV[2] - Convert stl files into a spl4 file 1=YES 0=NO
#

import bpy
import math
import os
import re
import sys

## Values that could change ##
# Directory load .fbx files from
fbxDirectory = '/home/dandorado/blender/fbxfiles'
# save/load .obj files to/from
objDirectory = '/home/dandorado/blender/objFrames'
# save/load .stl files to/from
stlDirectory = '/home/dandorado/blender/stlFrames'
# save/load custom .spl4 files to/from
spl4Directory = '/home/dandorado/blender/spl4Objects'

# default w-axis increment by frame
wAxisInc = 0.1


# Get the arguments and save as strings
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"
print(argv)

# delete starting objects generated by Blender by Default
print("Deleting Starting Objects")
print("")
startingObjects = ["Light", "Camera"]
for obj in startingObjects:
    bpy.data.objects[obj].select_set(True)    
    bpy.context.view_layer.objects.active = bpy.data.objects[obj]
bpy.ops.object.delete()


######## Convert fbx to Obj ##########

if (argv[0] == '1'):
    print("beginning to convert fbx files to obj frames.")
    # For each fbx animation.
    for filename in os.listdir(fbxDirectory):
        fbxFile = os.path.join(fbxDirectory, filename)
        # checking if it is a file
        if os.path.isfile(fbxFile):
            print("Beginning import of "+fbxFile)
            # Import FBX into the scene
            bpy.ops.import_scene.fbx(filepath=fbxFile)

        # Make sure nothing selected
        bpy.ops.object.select_all(action='DESELECT')

        # Make sure that the scene only contains frames of actual animation for your fbx
        if bpy.data.actions:
            print("Trimming Frames")
            # get all actions
            action_list = [action.frame_range for action in bpy.data.actions]
            # sort, remove doubles and create a set
            keys = (sorted(set([item for sublist in action_list for item in sublist])))
            # print first and last keyframe
            print ("{} {}".format("first keyframe:", keys[0]))
            print ("{} {}".format("last keyframe:", keys[-1]))
            # set the frames to fit
            bpy.data.scenes[0].frame_start = int(keys[0])
            bpy.data.scenes[0].frame_end = int(keys[-1])
        else:
            print ("no actions for frames")

        # Get everything imported
        objects = bpy.context.scene.objects
        print("Now exporting frames as obj")
        for obj in objects:
            # Make sure nothing else selected
            bpy.ops.object.select_all(action='DESELECT')
            objectToSelect = obj
            print("Considering "+obj.name)
            objectToSelect.select_set(True)
            # Check if the frame contains the Armature name using regex
            if re.search("Armature", obj.name):
                print(obj.name+" is going to be used.")
                # If so create a directory for the animation and export it
                bpy.context.view_layer.objects.active = obj
                newpath = objDirectory+"/"+obj.name 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)   
                bpy.context.view_layer.objects.active = objectToSelect
                bpy.ops.export_scene.obj(filepath=newpath+"/"+obj.name+".obj",use_animation=True)

        # Delete everything for the next animation to have a blank canvas
        print("Deleting all objects in secene")
        objects = bpy.context.scene.objects
        for obj in objects:
            obj.select_set(True)    
            bpy.context.view_layer.objects.active = obj
        bpy.ops.object.delete()


######## Convert Obj to STL ##########

if (argv[1] == '1'):
    # For each subdirectory with obj frames, then for each frame import it back in
    for subdir in os.listdir(objDirectory):
        for filename in os.listdir(os.path.join(objDirectory, subdir)):
            if re.search("obj", filename):
                f = os.path.join(objDirectory, subdir, filename)
                # checking if it is a file
                if os.path.isfile(f):
                    print(f)
                    # Import obj into the scene
                    bpy.ops.import_scene.obj(filepath=f)

        # Create a new subdirectory to store the STL outputs
        newpath = stlDirectory+"/"+subdir 
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        # deselect all meshes
        bpy.ops.object.select_all(action='DESELECT')

        # Select each obj image, export it as an STL, then delete it
        objects = bpy.context.scene.objects
        for obj in objects:
            print(obj.name)
            obj.select_set(True)
            bpy.ops.export_mesh.stl(filepath = newpath+"/"+obj.name+".stl",ascii=True,use_selection=True)
            bpy.ops.object.delete()

######## Convert STL to SPL4 ##########

if (argv[2] == '1'):
    # For each subdirectory with stl frames, then for each frame create a new .spl4 object
    for subdir in os.listdir(stlDirectory):
        spl4 = open(spl4Directory+'/'+subdir+'.spl4', 'w+')
        depth=0
        stlFrames = sorted(os.listdir(os.path.join(stlDirectory, subdir)))
        stl2 = open(stlDirectory+'/'+subdir+'/'+stlFrames[0], 'r').readlines()
        for i in range(len(stlFrames)-1):
            stlFrame1 = stlFrames[i]
            stlFrame2 = stlFrames[i+1]
            print(stlFrame1)
            print(stlFrame2)
            print(i)
            stl1 = stl2
            stl2 = open(stlDirectory+'/'+subdir+'/'+stlFrame2, 'r').readlines()
            for i in range(len(stl1)):
                if re.search("outer loop", stl1[i]):
                    spl4.write("prism start\n")
                    spl4.write(stl1[i+1][:-1]+' '+str(depth*wAxisInc)+'\n')
                    spl4.write(stl1[i+2][:-1]+' '+str(depth*wAxisInc)+'\n')
                    spl4.write(stl1[i+3][:-1]+' '+str(depth*wAxisInc)+'\n')
                    depth = depth+1
                    spl4.write(stl2[i+1][:-1]+' '+str(depth*wAxisInc)+'\n')
                    spl4.write(stl2[i+2][:-1]+' '+str(depth*wAxisInc)+'\n')
                    spl4.write(stl2[i+3][:-1]+' '+str(depth*wAxisInc)+'\n')
            