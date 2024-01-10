import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan pola sederhana (garis diagonal)
def sample_image(x, y):
    if abs(x - y) <= 2: # Garis diagonal tebal dalam 2 piksel
        return 1.0  # Warna putih untuk garis
    else:
        return 0.0  # Warna hitam untuk area lainnya

# Fungsi Supersampling dengan Sampel Area dan Pembagian Piksel
def supersample_image_area_pixel(width, height, super_factor):
    super_width = width * super_factor
    super_height = height * super_factor

    # Membuat gambar dengan resolusi tinggi
    higher_res_img = np.zeros((super_height, super_width))

    # Melakukan sampel gambar dengan resolusi tinggi dengan sampel area dan pembagian piksel
    for y in range(super_height):
        for x in range(super_width):
            orig_x = x / super_factor
            orig_y = y / super_factor

            # Area sampling: Menambahkan offset random
            orig_x += np.random.uniform(-0.5, 0.5)
            orig_y += np.random.uniform(-0.5, 0.5)

            pixel_value = sample_image(orig_x, orig_y)

            # Pixel phasing: Menambahkan noise random
            pixel_value += np.random.uniform(-0.25, 0.25)

            higher_res_img[y, x] = pixel_value

    # Mengurangi resolusi gambar (rata-rata piksel)
    downsampled_img = higher_res_img.reshape(height, super_factor, width, super_factor).mean(axis=(1, 3))

    return downsampled_img

# Image properties
width = 20
height = 20
super_factor = 5  # Faktor Supersampling

# Menghasilkan gambar Supersampling dengan Area Sampling dan Pixel Phasing
result_image = supersample_image_area_pixel(width, height, super_factor)

# Menampilkan gambar pensampling dengan Area Sampling dan Pixel Phasing
plt.imshow(result_image, cmap='copper')
plt.title('Supersampling dengan Area Sampling dan Pixel Phasing')
plt.axis('off')
plt.show()
