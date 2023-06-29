from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=25, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=25, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    employee_id = forms.CharField(label="", max_length=25, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Employee ID'}))
    
    class Meta:
        model = User
        fields = ('username', 'employee_id', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

# Create Add Record Form
class AddRecordForm(forms.ModelForm):

    GENDER_CHOICES = [
        ('G', 'Gender'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    DEP_CHOICES = [
        ('department', 'Department'),
		('general','General'),
        ('cardiology', 'Cardiology'),
		('dermatology', 'Dermatology'),
		('endocrinology', 'Endocrinology'),
		('gastroenterology', 'Gastroenterology'),
		('general_surgery', 'General Surgery'),
		('hematology', 'Hematology'),
		('neurology', 'Neurology'),
		('obstetrics_gynecology', 'Obstetrics and Gynecology'),
		('oncology', 'Oncology'),
		('ophthalmology', 'Ophthalmology'),
		('orthopedics', 'Orthopedics'),
		('otolaryngology', 'Otolaryngology'),
		('pediatrics', 'Pediatrics'),
		('psychiatry', 'Psychiatry'),
		('radiology', 'Radiology'),
		('urology', 'Urology'),
	]
    INDIA_STATES = [
        ('ST', 'State'),
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TS', 'Telangana'),
        ('TR', 'Tripura'),
        ('UK', 'Uttarakhand'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('DL', 'Delhi'),
        ('JK', 'Jammu and Kashmir'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'),
	]
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="First Name")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="Last Name")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="Email")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="Phone")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="Address")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="City")
    state = forms.ChoiceField(required=True, choices=INDIA_STATES, widget=forms.widgets.Select(attrs={"class": "form-control"}), label="State")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="Pincode")
    department = forms.ChoiceField(required=True, choices=DEP_CHOICES, widget=forms.widgets.Select(attrs={"class": "form-control selectpicker", "data-live-search": "true"}), label="Department")
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES, widget=forms.widgets.Select(attrs={"class": "form-control selectpicker", "data-live-search": "true"}), label="Gender")
    employee_id = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Employee ID", "class":"form-control"}), label="Employee ID")  # Add the Employee ID field
    history_record = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Case History", "class":"form-control"}), label="Case History")
    file = forms.FileField(required=False, label="File")


    class Meta:
        model = Record
        fields = '__all__'
        exclude = ("user",)