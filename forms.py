from django import forms
from .models import SanPham

class SanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = ['ma_hang', 'ten_san_pham', 'nhom_hang', 'hinh_anh', 'don_vi', 'so_luong', 'don_gia', 'mo_ta']
        widgets = {
            'ma_hang': forms.TextInput(attrs={'placeholder': 'Mã hàng'}),
            'ten_san_pham': forms.TextInput(attrs={'placeholder': 'Tên hàng'}),
            'nhom_hang': forms.TextInput(attrs={'placeholder': 'Nhóm hàng'}),
            'hinh_anh': forms.FileInput(),
            'don_vi': forms.TextInput(attrs={'placeholder': 'Đơn vị'}),
            'so_luong': forms.NumberInput(attrs={'placeholder': 'Tồn kho'}),
            'don_gia': forms.NumberInput(attrs={'placeholder': 'Đơn giá'}),
            'mo_ta': forms.Textarea(attrs={'placeholder': 'Mô tả hàng hóa'}),
        }