import cv2
import os

image_folder = 'frames'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(filename="my_video.avi",  #Provide a file to write the video to
fourcc=cv2.VideoWriter_fourcc(*'DIVX'),            #Use whichever codec works for you...
fps=15,                                        #How many frames do you want to display per second in your video?
frameSize=(width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()