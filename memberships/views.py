from django.shortcuts import render
from .models import UserMembership,Membership,Subscriptions
# Create your views here.
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
import stripe

def  get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None

def get_user_subscription(request):
    user_subscription_qs = Subscriptions.objects.filter(
        user_membership=get_user_membership(request)
    )
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None
def get_selected_membership(request):
    membership_type = request.session['selected_membership_type']
    selected_membership_qs  = Membership.objects.filter(
            membership_type=membership_type
        )
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None
class MembershipSelectView(ListView):
    model = Membership
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        current_membership = get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
        return context
    def post(self,request,**kwargs):
        selected_membership_type = request.POST.get('membership_type')
        user_subscription = get_user_subscription(request)
        user_membership = get_user_membership(request)

        selected_membership_qs = Membership.objects.filter(
            membership_type=selected_membership_type
        )
        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()
        '''
        ====================
        VALIDATION
        ====================
        '''
        if user_membership.membership ==  selected_membership:
            if user_subscription != None:
                print("No need")
                pass
        #assign to the session
        request.session['selected_membership_type'] = selected_membership.membership_type
        return HttpResponseRedirect(reverse('memberships:payment'))
# class CourseDetailView(DetailView):
#     model = Course
def PaymentView(request):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)
    publishKey = settings.STRIPE_PUBLISHABLE_KEY

    context = {
        'publishKey':publishKey,
        'selected_membership':selected_membership
    }
    return render(request,"memberships/memberships_payment.html",context)