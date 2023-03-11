from django.urls import path, include
from Portail_Etudiant import views
# from .views import CategoryView
from PARTIEL import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base,name='base'),
    path('registre/',views.registre,name='registre'),
    path('thanks/',views.thanks),
    path('sub1/',views.sub1),
    path('sub2/',views.sub2),
    path('login/',views.login,name='login'),
    path('lesson/<int:val>',views.lessons,name='less'),
    path('logout/',views.logout_view, name='logout'),
    path('youtube/',views.ytb, name='youtube'), 
    path('profile/',views.profile,name='profile'),
    path('sub3/',views.profilesumitted),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)