import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan pola sederhana (garis dalam kasus ini)
def sample_image(x, y):
    if abs(x - y) <= 2:  # Garis diagonal tebal dalam 2 piksel
        return 1.0  # Warna putih untuk garis
    else:
        return 0.0  # Warna hitam untuk area lainnya

# Fungsi Supersampling dengan Area sampling
def supersample_image_area_sampling(width, height, super_factor):
    super_width = width * super_factor
    super_height = height * super_factor

    # Membuat gambar dengan resolusi tinggi
    higher_res_img = np.zeros((super_height, super_width))

    # Mencoba sampel gambar dengan resolusi tinggi dengan Area sampling
    for y in range(super_height):
        for x in range(super_width):
            orig_x = x / super_factor
            orig_y = y / super_factor

            # Area sampling: Menambahkan offset acak
            orig_x += np.random.uniform(-0.5, 0.5)
            orig_y += np.random.uniform(-0.5, 0.5)

            higher_res_img[y, x] = sample_image(orig_x, orig_y)

    # Mengurangi resolusi gambar (rata-rata piksel)
    downsampled_img = higher_res_img.reshape(height, super_factor, width, super_factor).mean(axis=(1, 3))

    return downsampled_img

# Properti gambar
width = 20
height = 20
super_factor = 5  # Faktor Supersampling

# Membuat gambar Supersampling dengan Area Sampling
result_image = supersample_image_area_sampling(width, height, super_factor)

# Menampilkan gambar Supersampling dengan Area Sampling
plt.imshow(result_image, cmap='gray')
plt.title('Supersampling dengan Area Sampling dan Pixel Phasing')
plt.axis('off')
plt.show()
