import math

# 2D uzaydaki noktaları temsil eden demetlerin bir listesi
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Her nokta çifti arasındaki Öklid mesafesini hesaplayıp distances listesine ekleyen döngü
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Minimum mesafeyi yazdırma
print("Minimum mesafe:", min_distance)
