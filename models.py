from django.db import models

class SanPham(models.Model):
    ma_hang = models.CharField(max_length=10, unique=True)  # Mã hàng
    ten_san_pham = models.CharField(max_length=100)  # Tên hàng
    nhom_hang = models.CharField(max_length=50)  # Nhóm hàng
    hinh_anh = models.CharField(max_length=255, blank=True, null=True)
    don_vi = models.CharField(max_length=20, default='Cái')  # Đơn vị tính
    so_luong = models.IntegerField(default=0)  # Tồn kho
    don_gia = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # Đơn giá
    mo_ta = models.TextField(blank=True)  # Mô tả hàng hóa
    canh_bao_het_hang = models.BooleanField(default=False)  # Flag cảnh báo

    def __str__(self):
        return self.ten_san_pham

    def tinh_trang(self):
        if self.so_luong > 10:
            return 'Còn nhiều'  # Xanh
        elif self.so_luong > 0:
            return 'Sắp hết'  # Vàng
        else:
            return 'Hết'  # Đỏ

class NhapKho(models.Model):
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    so_luong_nhap = models.IntegerField()
    ngay_nhap = models.DateTimeField(auto_now_add=True)

class XuatKho(models.Model):
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    so_luong_xuat = models.IntegerField()
    ngay_xuat = models.DateTimeField(auto_now_add=True)