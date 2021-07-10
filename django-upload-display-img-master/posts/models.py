# posts/models.py
from django.db import models

#from YOLO_func import detection
# import cv2
    
    
# image = cv2.imread("input.jpg")

#yl.detection(image)
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def results(self):
        return self.cover

    def __str__(self):
        return self.title