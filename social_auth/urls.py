from django.urls import path

from .views import * 

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),
    path('facebook/', FacebookSocialAuthView.as_view()),
    path('twitter/', TwitterSocialAuthView.as_view()),
    path('CheckOTPAuthView/', CheckOTPAuthView.as_view()),
    path('PhoneNumberAuthView/', PhoneNumberAuthView.as_view()),
    path('LoadingOTView/', LoadingOTView.as_view()),


]
