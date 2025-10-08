from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import SanPham, NhapKho, XuatKho

@login_required
def tong_quan(request):
    tong_san_pham = SanPham.objects.count()
    san_pham_sap_het = SanPham.objects.filter(so_luong__lt=10).count()
    gia_tri_ton_kho = SanPham.objects.aggregate(Sum('gia_tri'))['gia_tri__sum'] or 0
    phieu_nhap_gan_nhat = NhapKho.objects.last().id if NhapKho.objects.exists() else 'N/A'
    phieu_xuat_gan_nhat = XuatKho.objects.last().id if XuatKho.objects.exists() else 'N/A'
    phieu_gan_nhat = f'N{phieu_nhap_gan_nhat or phieu_xuat_gan_nhat}'
    tong_don_hang = XuatKho.objects.count()
    tong_nhap = NhapKho.objects.aggregate(Sum('so_luong_nhap'))['so_luong_nhap__sum'] or 0
    tong_xuat = XuatKho.objects.aggregate(Sum('so_luong_xuat'))['so_luong_xuat__sum'] or 0
    tong_tong = tong_nhap + tong_xuat
    ty_le_nhap = (tong_nhap / tong_tong * 100) if tong_tong else 0
    ty_le_xuat = (tong_xuat / tong_tong * 100) if tong_tong else 0
    canh_bao_het_hang = SanPham.objects.filter(canh_bao_het_hang=True)[:3]

    context = {
        'tong_san_pham': tong_san_pham,
        'san_pham_sap_het': san_pham_sap_het,
        'gia_tri_ton_kho': gia_tri_ton_kho,
        'phieu_gan_nhat': phieu_gan_nhat,
        'tong_don_hang': tong_don_hang,
        'ty_le_nhap': round(ty_le_nhap),
        'ty_le_xuat': round(ty_le_xuat),
        'canh_bao_het_hang': canh_bao_het_hang,
    }
    return render(request, 'tong_quan.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import SanPhamForm
from .models import SanPham

@login_required
def danh_muc(request):
    san_pham_list = SanPham.objects.all()
    return render(request, 'danh_muc.html', {'san_pham_list': san_pham_list})

@login_required
def them_san_pham(request):
    if request.method == 'POST':
        form = SanPhamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('danh_muc')
    else:
        form = SanPhamForm()
    return render(request, 'them_san_pham.html', {'form': form})

@login_required
def sua_san_pham(request, pk):
    san_pham = get_object_or_404(SanPham, pk=pk)
    if request.method == 'POST':
        form = SanPhamForm(request.POST, request.FILES, instance=san_pham)
        if form.is_valid():
            form.save()
            return redirect('danh_muc')
    else:
        form = SanPhamForm(instance=san_pham)
    return render(request, 'sua_san_pham.html', {'form': form})

@login_required
def xoa_san_pham(request, pk):
    san_pham = get_object_or_404(SanPham, pk=pk)
    if request.method == 'POST':
        san_pham.delete()
        return redirect('danh_muc')
    return render(request, 'xoa_san_pham.html', {'san_pham': san_pham})