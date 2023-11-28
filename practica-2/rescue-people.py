from GUI import GUI
from HAL import HAL
import cv2

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


while True:
  # Cargar la imagen desde la variable vert_img
    vert_img = HAL.get_ventral_image()
    front_img = HAL.get_frontal_image()
  
    faces = calculateFaces(vert_img)
    drawFaces(vert_img, faces)
    x, y, z = HAL.get_position()
    HAL.takeoff(y + 1)
  
  # Mostrar la imagen con las caras detectadas
    GUI.showImage(vert_img)
    GUI.showLeftImage(front_img)