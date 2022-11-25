from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# ล็อคอิน
def staff_login(req):
    return render(req,'pages/staff_login.html')

# รายละเอียดการยืม
def staff_borrow_detail(req):
    return render(req,'pages/staff_borrow_detail.html')

# ประวัติการยืม
def staff_borrowing_history_detail(req):
    return render(req,'pages/staff_borrowing_history_detail.html')

# ข้อมูลการคืนพัสดุ-ครุภัณฑ์
def staff_borrowing_history(req):
    return render(req,'pages/staff_borrowing_history.html')

# จัดการรายการยืม
def staff_index_borrow(req):
    return render(req,'pages/staff_index_borrow.html')

# จัดการรายการยืม
def staff_index_borrownow(req):
    return render(req,'pages/staff_index_borrownow.html')

# จัดการรายการคืน
def staff_index_return(req):
    return render(req,'pages/staff_index_return.html')

# จัดการข้อมูลการแนะนำพัสดุเข้าสู่ระบบ
def staff_introduction_detail(req):
    return render(req,'pages/staff_introduction_detail.html')

# ข้อมูลการแนะนำพัสดุเข้าสู่ระบบ
def staff_introduction_hisdetail(req):
    return render(req,'pages/staff_introduction_hisdetail.html')

# การแนะนำพัสดุเข้าสู่ระบบ
def staff_introduction(req):
    return render(req,'pages/staff_introduction.html')

# รายละเอียดจัดการพัสดุ-ครุภัณฑ์
def staff_manage_detail(req):
    return render(req,'pages/staff_manage_detail.html')

# จัดการพัสดุ
def staff_manage_parcel(req):
    return render(req,'pages/staff_manage_parcel.html')

# จัดการครุภัณฑ์
def sstaff_manage_durable(req):
    return render(req,'pages/staff_manage_durable.html')

# แก่ไขข้อมูลส่วนตัว
def staff_personal_info_edit(req):
    return render(req,'pages/staff_personal_info_edit.html')

# จัดการข้อมูลส่วนตัว
def staff_personal_info(req):
    return render(req,'pages/staff_personal_info.html')

# รายละเอียดรายงานการยืมพัสดุ
def staff_report_borrowReport(req):
    return render(req,'pages/staff_report_borrowReport.html')

# รายงานจำนวนรายการพัสดุที่จำหน่ายทิ้ง
def staff_report_dispose(req):
    return render(req,'pages/staff_report_dispose.html')

# รายงานภาพรวมพัสดุ
def staff_report(req):
    return render(req,'pages/staff_report.html')

# รายงานจำนวนรายการพัสดุที่คงเหลือในระบบ
def staff_report_remaining(req):
    return render(req,'pages/staff_report_remaining.html')

# การตั้งค่า
def staff_setting(req):
    return render(req,'pages/staff_setting.html')

# รายงานการยืมทั้งหมด
def staff_Including_borrowing(req):
    return render(req,'pages/staff_Including_borrowing.html')
    