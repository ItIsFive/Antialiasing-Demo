import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan pola sederhana (garis diagonal)
def sample_image(x, y):
    if abs(x - y) <= 2: # Garis diagonal tebal dalam 2 piksel
        return 1.0  # Warna putih untuk garis
    else:
        return 0.0  # Warna hitam untuk area lainnya

# Fungsi Supersampling 
def supersample_image(width, height, super_factor):
    super_width = width * super_factor
    super_height = height * super_factor

    # Membuat gambar dengan resolusi tinggi
    higher_res_img = np.zeros((super_height, super_width))

    # Melakukan sampel gambar dengan resolusi tinggi 
    for y in range(super_height):
        for x in range(super_width):
            orig_x = x / super_factor
            orig_y = y / super_factor

            higher_res_img[y, x] = sample_image(orig_x, orig_y)

    # Mengurangi resolusi gambar (rata-rata piksel)
    downsampled_img = higher_res_img.reshape(height, super_factor, width, super_factor).mean(axis=(1, 3))

    return downsampled_img

# Image properties
width = 20
height = 20
super_factor = 5  # Supersampling factor

# Menghasilkan gambar Supersampling
supersampled_image = supersample_image(width, height, super_factor)

# Display supersampled image
plt.imshow(supersampled_image, cmap='gray')
plt.title('Supersampling')
plt.axis('off')
plt.show()
