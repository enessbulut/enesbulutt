import cv2
import numpy as np

# Kamera ile görüntü yakala (veya bir video dosyası da kullanılabilir)
cap = cv2.VideoCapture(0)

# mavi renk için genişletilmiş HSV aralığı1
lower_blue_1 = np.array([120,150,50])
upper_blue_1 = np.array([120,255,255])

lower_blue_2 = np.array([90,80,50])
upper_blue_2 = np.array([130,255,255])

while True:
    # Kameradan görüntü al
    ret, frame = cap.read()
    
    # Görüntüyü HSV renk uzayına çevir2
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # mavi renk için maskeler oluştur
    mask_1 = cv2.inRange(hsv, lower_blue_1, upper_blue_1)
    mask_2 = cv2.inRange(hsv, lower_blue_2, upper_blue_2)
    
    # Maskeleri birleştir
    mask = cv2.bitwise_or(mask_1, mask_2)
    
    # Maskeyi kullanarak kırmızı bölgeyi tespit et
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Orijinal görüntü ve sonuçları göster
    cv2.imshow('Orijinal Görüntü', frame)
    cv2.imshow('mavi Obje Tespiti', result)
    
    # 'q' tuşuna basılana kadar bekle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Her şey tamamlanınca pencereyi kapat
cap.release()
cv2.destroyAllWindows()