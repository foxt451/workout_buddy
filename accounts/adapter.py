from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from webpage import models
from allauth.account.models import EmailAddress
from django.urls import reverse


class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        if not hasattr(request.user, 'workoutprofile'):
            # create an empty profile for the user and redirect to edit it
            profile = models.WorkoutProfile(user=request.user)
            profile.save()
            return reverse('webpage:wprofile-edit')
        else:
            return super().get_login_redirect_url(request)
        
class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_connect_redirect_url(self, request):
        #return super().get_connect_redirect_url(request)
        if not hasattr(request.user, 'workoutprofile'):
            # create an empty profile for the user and redirect to edit it
            profile = models.WorkoutProfile(user=request.user)
            profile.save()
            return reverse('webpage:wprofile-edit')
        else:
            return super().get_connect_redirect_url()
    
    # ASSUMING GOOGLE EMAILS ARE ALWAYS VERIFIED    
    # def pre_social_login(self, request, sociallogin):
    #     """
    #     Invoked just after a user successfully authenticates via a
    #     social provider, but before the login is actually processed
    #     (and before the pre_social_login signal is emitted).

    #     We're trying to solve different use cases:
    #     - social account already exists, just go on
    #     - social account has no email or email is unknown, just go on
    #     - social account's email exists, link social account to existing user
    #     """
    #     print('got there')
    #     # Ignore existing social accounts, just do this stuff for new ones
    #     if sociallogin.is_existing:
    #         return
    #     print('got heremda')
    #     # some social logins don't have an email address, e.g. facebook accounts
    #     # with mobile numbers only, but allauth takes care of this case so just
    #     # ignore it
    #     if 'email' not in sociallogin.account.extra_data:
    #         return

    #     # check if given email address already exists.
    #     # Note: __iexact is used to ignore cases
    #     print('got here')
    #     try:
    #         email = sociallogin.account.extra_data['email'].lower()
    #         email_address = EmailAddress.objects.get(email__iexact=email)

    #     # if it does not, let allauth take care of this new social account
    #     except EmailAddress.DoesNotExist:
    #         return

    #     # if it does, connect this new social login to the existing user
    #     user = email_address.user
    #     sociallogin.connect(request, user)
