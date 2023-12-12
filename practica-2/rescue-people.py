import cv2
from GUI import GUI
from HAL import HAL
import cv2
import math
import numpy as np

def calculateFaces(img):
  # Convertir la imagen a escala de grises (ya que el detector de caras de OpenCV trabaja con imágenes en escala de grises)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  # Cargar el clasificador Haar Cascade para la detección de caras
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  
  # Aplicar la detección de caras
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
  
    return faces
  
def drawFaces(frame, faces):
  # Dibujar rectángulos alrededor de las caras detectadas
    for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Define the search area based on the orientative GPS locations
boat_location = np.array([569508, 4459162]) # Este, Nort # Survivors' location
people_location = np.array([569468, 4459132])  # Safety boat location
rpp = people_location - boat_location

min_square = [20,-20]
max_square = [60,-50]
positions = []
for x in range(min_square[0], max_square[0] + 1,2):
  for y in range(min_square[1], max_square[1] + 1,-5):
    positions.append((x,y, 2))

next_position = np.array(positions.pop(0))
HAL.takeoff(4)
# Main loop
while True:
  
    vert_img = HAL.get_ventral_image()
    front_img = HAL.get_frontal_image()
    GUI.showImage(vert_img)
    GUI.showLeftImage(front_img)
    
    velocity = HAL.get_velocity()
    
    faces = calculateFaces(vert_img)
    drawFaces(vert_img, faces)
    
  # Cargar la imagen desde la variable vert_img
  
    current_position = np.array(HAL.get_position())
    #HAL.takeoff(y1 + 1)
    min_distance = 1
    distance = next_position - current_position
    distance = math.sqrt(distance[0]**2 + distance[1]**2)
    if distance <= min_distance:
      next_position = positions.pop(0)
    HAL.set_cmd_pos(next_position[0],next_position[1], next_position[2], 0)
    #HAL.set_cmd_vel(vx, vy, vz, az)
    print(next_position, f'distance: {distance}',f'velocity: {velocity}')