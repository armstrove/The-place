from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import ReadOnlyPasswordHashField
    


User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('full_name','email',) # full name 
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self,commit=True):
        user=super(UserAdminCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user    


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on 
    the user, but replaces the password field with admin's 
    password hash display field."""    
    password = ReadOnlyPasswordHashField(),
    
    class Meta:
        model = User 
        fields = ('full_name','email', 'password', 'active', 'admin')
        
    def clean_password(self):        
        # Regardless of what the user provides, return the initial value. 
        # This is done here, rather than on the field, because the 
        # field does not have access to the initial value return self.initial["password"]
        return self.initial["password"]

  
class LoginForm(forms.Form):
    email    = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('full_name','email',) # full name 
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self,commit=True):
        user=super(RegisterForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = False # send confirmation email
        if commit:
            user.save()
        return user        
    
 