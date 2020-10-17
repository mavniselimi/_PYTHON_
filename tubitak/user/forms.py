from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Kullanıcı Adı")
    password=forms.CharField(label="Parola",widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username=forms.CharField(min_length=8,max_length=50,label="Kullanıcı Adı")
    email=forms.EmailField(max_length=50,label="Email",widget=forms.EmailInput)
    password=forms.CharField(min_length=8,max_length=20,label="Parola",widget=forms.PasswordInput)
    confirm=forms.CharField(min_length=8,max_length=20,label="Parola Doğrula",widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password") 
        confirm=self.cleaned_data.get("confirm") 
        email=self.cleaned_data.get("email")

        if password and confirm and (password!=confirm):
            raise forms.ValidationError("Parolalar Eşleşmiyor")      

        values = {
            "username" : username,
            "password" : password,
            "email" : email,
        }
        return values