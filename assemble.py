import glob, re, math, shutil, time, os

#get the listing of how many files there are
files = glob.glob("images/*.png")
print str(len(files)) + " files to be sorted"

#sort them
filenames = map(lambda v: int(v.split("/")[-1].split(".")[0]), files) # map by lane
filenames.sort()

#check the list consistency
inconsistent=False
for i, name in enumerate(filenames):
  if i == len(filenames)-1:
	if (~inconsistent):
            print "List Consistency Verified"
            break
        else:
            break
  if name >= filenames[i+1]:
    print "Inconsistency detected."
    inconsistent = True

#figure out the parameters for copy list
runTime = float(raw_input("How long should the film be in minutes? "))
runTime = runTime * 60
frameRate = int(raw_input("What frame-rate (in fps)?" ))

#compute the number of frames needed
numFrames = runTime * frameRate
print "You need " + str(numFrames) + " frames."

#work out exactly WHICH frames to get
framesToGet = range(0, len(filenames), int(math.floor(len(filenames)/numFrames)))

#clean the build directory
print "Cleaning the build directory"
os.system("rm imageset/*")

#begin the copy
startTime=time.time()
print "Copying files..."
i=0
for frame in framesToGet:
  shutil.copyfile("images/" + str(filenames[frame]) + ".png", "imageset/image" + str(i) + ".png")
  i=i+1

print "File copy completed in " + str(time.time()-startTime) + " seconds."


#Render the film
startTime = time.time()
print "Beginning Render"
os.system("ffmpeg -r {0} -i imageset/image%d.png timelapse.mp4".format(frameRate))
print "Render completed in " + str(time.time()-startTime) + " seconds."
