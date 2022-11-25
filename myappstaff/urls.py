from django.urls import path
from .views import * 

urlpatterns = [
    # staff
    path('staff_login/', staff_login),
    path('staff_borrow_detail/', staff_borrow_detail),
    path('staff_borrowing_history_detail/', staff_borrowing_history_detail),
    path('staff_borrowing_history/', staff_borrowing_history),
    path('staff_index_borrow/', staff_index_borrow),
    path('staff_index_borrownow/', staff_index_borrownow),
    path('staff_index_return/', staff_index_return),
    path('staff_introduction_detail/', staff_introduction_detail),
    path('staff_introduction_hisdetail/', staff_introduction_hisdetail),
    path('staff_introduction/', staff_introduction),
    path('staff_manage_detail/', staff_manage_detail),
    path('staff_manage_parcel/', staff_manage_parcel),
    path('staff_manage_durable/', sstaff_manage_durable),
    path('staff_personal_info_edit/', staff_personal_info_edit),
    path('staff_personal_info/', staff_personal_info),
    path('staff_report_borrowReport/', staff_report_borrowReport),
    path('staff_report_dispose/', staff_report_dispose),
    path('staff_report/', staff_report),
    path('staff_report_remaining/', staff_report_remaining),
    path('staff_setting/', staff_setting),
    path('staff_Including_borrowing/', staff_Including_borrowing),
    
    
]
