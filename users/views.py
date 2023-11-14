from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models import Customer
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.

class CreateAccount(SuccessMessageMixin, FormView):

    '''
    Creates a new account by receiving the parameters : -
    Username
    Password
    Password(confirmed)
    On success, class will bring user to main page of Website
    with successful message.
    On error, class will return user to the 'create account' form.
    '''

    template_name = 'create_account.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_message = 'Account created successfully!'
    success_url = reverse_lazy('golfgear')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CreateAccount, self).form_valid(form)

    @receiver(post_save, sender=User)
    def create_or_update_customer(
        sender,
        instance,
        created,
        **kwargs
         ):
        """Create or update the Customer"""

        if created:
            cust_name = str(instance)
            Customer.objects.create(user=instance, name=cust_name,
                                    email=cust_name + '1979@gmail.com')
        instance.customer.save()

    def state(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('golfgear')
        return super(CreateAccount, self).get(*args, **kwargs)


class Login(SuccessMessageMixin, LoginView):

    '''
    Recieve login details from registered user
    if user details are recognised, bring them
    to the main Website product page
    if not recognised, return to Login page
    '''

    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = 'Login successful!'

    def get_success_url(self):
        return reverse_lazy('golfgear')


class Logout(LogoutView):

    '''
    Recieves a logout instruction
    returns user to the Logout page
    '''

    template_name = 'logout.html'
    redirect_authenticated_user = True
    success_message = 'Logout successful!'


def logout(request):
    '''
    Link to Logout page
    '''

    context = {}
    return render(request, 'logout.html', context)
