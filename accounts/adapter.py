from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from webpage import models
from django.utils.translation import gettext_lazy as _
from allauth.account.models import EmailAddress
from django.urls import reverse
from django.utils.safestring import SafeString
from django.shortcuts import redirect


class MyAccountAdapter(DefaultAccountAdapter):
    def __init__(self, request=None):
        super().__init__(request)
        # popover_str = _("If you believe this is a mistake or simply don't remember your password then go to Sign In page and follow 'Forgot Password' button.")
        self.error_messages['email_taken'] = _('A user is already registered with this e-mail address. If you believe this is a mistake or simply don\'t remember your password then go to Login page and follow \'Forgot Password\' button.') # SafeString(_('A user is already registered with this e-mail address.') + f' <i class="fa fa-question-circle" data-bs-toggle="tooltip" title="{popover_str}"></i>')
    
    def get_login_redirect_url(self, request):
        if not hasattr(request.user, 'workoutprofile'):
            # create an empty profile for the user and redirect to edit it
            profile = models.WorkoutProfile(user=request.user)
            profile.save()
            return reverse('webpage:wprofile-edit')
        else:
            return super().get_login_redirect_url(request)
    
    def get_signup_redirect_url(self, request):
        profile = models.WorkoutProfile(user=request.user)
        profile.save()
        return reverse('webpage:wprofile-edit')
        
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
        
    def get_login_redirect_url(self, request):
        #return super().get_connect_redirect_url(request)
        if not hasattr(request.user, 'workoutprofile'):
            # create an empty profile for the user and redirect to edit it
            profile = models.WorkoutProfile(user=request.user)
            profile.save()
            return reverse('webpage:wprofile-edit')
        else:
            return super().get_login_redirect_url()
        
    def get_signup_redirect_url(self, request):
        profile = models.WorkoutProfile(user=request.user)
        profile.save()
        return reverse('webpage:wprofile-edit')
    
    # ASSUMING GOOGLE EMAILS ARE ALWAYS VERIFIED    
    def pre_social_login(self, request, sociallogin):
        if sociallogin.is_existing:
            return

        # some social logins don't have an email address, e.g. facebook accounts
        # with mobile numbers only, but allauth takes care of this case so just
        # ignore it
        if 'email' not in sociallogin.account.extra_data:
            return

        # check if given email address already exists.
        # Note: __iexact is used to ignore cases
        try:
            email = sociallogin.account.extra_data['email'].lower()
            email_address = EmailAddress.objects.get(email__iexact=email)

        # if it does not, let allauth take care of this new social account
        except EmailAddress.DoesNotExist:
            return

        # if it does, connect this new social login to the existing user
        user = email_address.user
        sociallogin.connect(request, user)
