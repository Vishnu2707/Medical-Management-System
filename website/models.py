from django.db import models


class Record(models.Model):

	GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
	DEP_CHOICES = [
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
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50, choices=INDIA_STATES, default=None, blank=True, null=True)
	zipcode =  models.CharField(max_length=20)
	department =  models.CharField(max_length=50)
	department = models.CharField(max_length=50, choices=DEP_CHOICES, default=None, blank=True, null=True)
	gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=None, blank=True, null=True)
	employee_id = models.CharField(max_length=50, default=None, blank=True, null=True) # Add the Employee ID field
	history_record = models.CharField(max_length=1000, default=None, blank=True, null=True)
	file = models.FileField(upload_to='uploads/', default=None, blank=True, null=True)
	def __str__(self):
		return(f"{self.first_name} {self.last_name}")