from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from users.views import SignUpView, LoginPageView, log_out,profile,ProfileView, verify_code
from . import views
app_name = 'user'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LoginPageView.as_view(), name="login"),
    path('profile_update/', profile, name= 'profile-update'),
    path('profile/', login_required(ProfileView.as_view()), name="profile"),
    path('logout/', log_out, name="logout"),
    path('verify/', views.verify_code),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
