from django.conf.urls import url

from . import views

app_name = 'placement'

urlpatterns = [

    url(r'^$', views.Placement, name='placement'),
    url(r'^student_records/$', views.StudentRecords, name='student_records'),
    url(r'^manage_records/$', views.ManageRecords, name='manage_records'),
    url(r'^statistics/$', views.PlacementStatistics, name='placement_statistics'),
    # url(r'^event_add/$', views.ScheduleSubmit, name='add_schedule'),
    # url(r'^event_delete/$', views.ScheduleSubmit, name='delete_schedule'),
    # url(r'^search_record/$', views.SearchRecord, name='search_record'),
    # url(r'^manage_records/$', views.ManageRecords, name='manage_record'),
    # url(r'^html_to_pdf_view/$', views.html_to_pdf_view, name='html_to_pdf_view'),
    url(r'^cv/(?P<username>[a-zA-Z0-9\.]{1,20})/$', views.cv, name="cv"),

]
