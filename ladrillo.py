import pygame

class Brick:

   def __init__ (self, posx, posy, img):
       self.__posx = posx
       self.__posy = posy
       self.__img = self.__img = pygame.image.load(img)
       self.__rect = self.__img.get_rect()
       self.__rect.move_ip(posx,posy)

   @property
   def rect(self):
       return self.__rect

   @rect.setter
   def rect(self, valor):
       self.__rect = valor

   @property
   def img(self):
       return self.__img

   @img.setter
   def img(self, valor):
       self.__img = valor

   @property
   def posx(self):
       return self.__posx

   @img.setter
   def posx(self, valor):
       self.__posx = valor

   @property
   def posy(self):
       return self.__posy

   @posy.setter
   def posy(self, valor):
    self.__posy = valor