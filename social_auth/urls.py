from django.urls import path

from .views import * 

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),
    path('google-with-details/', GoogleSocialAuthWithDetailsView.as_view()),
    path('google-with-details-login/', GoogleSocialAuthWithDetailsLogInView.as_view()),
    path('facebook/', FacebookSocialAuthView.as_view()),
    path('twitter/', TwitterSocialAuthView.as_view()),
    path('CheckOTPAuthView/', CheckOTPAuthView.as_view()),
    path('PhoneNumberAuthLogInView/', PhoneNumberAuthLogInView.as_view()),
    path('PhoneNumberAuthView/', PhoneNumberAuthView.as_view()),
    path('LoadingOTView/', LoadingOTView.as_view()),


]
