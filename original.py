import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan pola sederhana (garis diagonal)
def sample_image(x, y):
    if abs(x - y) <= 2: # Garis diagonal tebal dalam 2 piksel
        return 1.0  # Warna putih untuk garis
    else:
        return 0.0  # Warna hitam untuk area lainnya

# Image properties
width = 20
height = 20

# Membuat gambar dengan resolusi yang diinginkan
image = np.zeros((height, width))

# Melakukan sampel gambar 
for y in range(height):
    for x in range(width):
        image[y, x] = sample_image(x, y)

# Display gambar tanpa supersampling
plt.imshow(image, cmap='gray')
plt.title('Gambar Original')
plt.axis('off')
plt.show()