from django.contrib.auth.views import LoginView
from .forms import PhoneNumberAuthenticationForm

class PhoneNumberLoginView(LoginView):
    form_class = PhoneNumberAuthenticationForm
    template_name = 'login.html'  # ایجاد این تمپلیت را فراموش نکنید
