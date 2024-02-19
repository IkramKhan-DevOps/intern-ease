from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from src.accounts.bll import is_account_complete
from src.accounts.forms import UserProfileForm
from src.portals.company.models import Company


@method_decorator(login_required, name='dispatch')
class CrossAuthView(View):

    def get(self, request):

        user = request.user

        # SUPER USER
        if user.is_staff:
            return redirect("/admin/")

        # NOT IDENTIFIED
        if not request.user.is_completed:
            return redirect('accounts:identification-check')

        # NOT COMPLETE
        if not is_account_complete(request.user):
            messages.warning(request, "Please complete your profile for better recommendations")
            return redirect("accounts:user-change")

        # CUSTOMER OR COMPANY
        if request.user.is_company:
            return redirect('company:dashboard')
        else:
            return redirect('customer:dashboard')


@method_decorator(login_required, name='dispatch')
class UserUpdateView(View):

    def get(self, request):
        form = UserProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, template_name='accounts/user_update_form.html', context=context)

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            messages.success(request, "Your profile updated successfully")
            form.save(commit=True)
        context = {'form': form}
        return render(request, template_name='accounts/user_update_form.html', context=context)


@method_decorator(login_required, name='dispatch')
class IdentificationCheckView(View):

    def get(self, request):

        # IS USER ALREADY IDENTIFIED
        if request.user.is_completed:
            return redirect('accounts:cross-auth-view')

        return render(request, 'accounts/identification-check.html')

    def post(self, request):

        # IF USER ALREADY IDENTIFIED
        if request.user.is_completed: return redirect('accounts:cross-auth-view')

        user_type = request.POST.get('user_type', None)

        # IF USER HAS TYPE
        if user_type is not None:
            user = request.user

            # IF USER HAS CORRECT TYPE
            if user_type == '1' or user_type == '2':
                if user_type == '1':
                    messages.success(request, "Post a job wait for applications and find a best employees.")
                    user.is_company = True
                else:
                    messages.success(request, "so you are here to find a job")
                    user.is_customer = True
                user.is_completed = True
                user.save()
                if user_type == '1':
                    Company.objects.create(user=user)
                return redirect('accounts:cross-auth-view')
            else:
                messages.error(request, "Please provide correct user type")
        else:
            messages.error(request, "Please provide user type")

        return render(request, 'accounts/identification-check.html')
