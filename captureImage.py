import pygame
import pygame.camera
from pygame.locals import *
import pygame.image
import awsRekognition



# pip install Pygame

def list_cameras():
    camlist = pygame.camera.list_cameras()
    if camlist:
        for acam in camlist:
            print ('Available Camera: '+ acam)
        return camlist[0]


def capture_image(cam_location):
    cam = pygame.camera.Camera(cam_location,(640,480))
    cam.start()
    image = cam.get_image()
    pygame.image.save(image, "/var/tmp/capturedImage.JPG")


def main():
    # As the camera module is optional, import it
    # # and initialize it manually.
    #pygame.init()
    pygame.camera.init()
    cameraLocation = list_cameras()
    capture_image(cameraLocation)
    print('Took image')
    pygame.camera.quit()
    awsRekognition.init_process_local_file("/var/tmp/capturedImage.JPG")


if __name__=="__main__":
    main()