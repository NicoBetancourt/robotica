from GUI import GUI
from HAL import HAL
# Enter sequential code!
import numpy as np
import cv2

# Constantes de control PID
kp = 0.005  # Ganancia proporcional
ki = 0.000001  # Ganancia integral
kd = 0.01  # Ganancia derivativa

# Variables de control PID
last_error = 0
integral = 0

i = 0
while True:
    # Captura la imagen de la cámara
    img = HAL.getImage()
    h , ancho , d = img.shape
    # Preprocesamiento de la imagen (ajusta estos valores según la realidad)
    lower_bound = np.array([0, 0, 200])
    upper_bound = np.array([50, 50, 255])
    masked_image = cv2.inRange(img, lower_bound, upper_bound)
    # Encuentra el centro de la línea (ajusta esta parte según la realidad)
    M = cv2.moments(masked_image)
    
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0
      
    # Control PID
    error = 317 - cx   # Error de seguimiento
    integral += error  # Término integral
    derivative = error - last_error  # Término derivativo
    last_error = error

    # Calcular velocidad angular usando PID
    w = kp * error + ki * integral + kd * derivative

    # Establecer velocidad lineal y angular
    vel = 4# - abs(error*6/317)
    HAL.setV(vel)  # Velocidad lineal constante
    HAL.setW(w)
    
    GUI.showImage(masked_image)
    #print(f'cx: {cx}, Error: {error}, w: {w}')
    print('%d cx: %.0f cy: %.0f w: %.3f error: %.3f derivative: %.3f integral: %.3f vel: %.0f' % (i, cx, cy, w, error, derivative, integral, vel))
    i = i + 1
    