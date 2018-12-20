from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    Name = forms.CharField(required=True)



class adv(forms.Form):
    customer_id = forms.CharField()
    latitude = forms.CharField()
    longitude = forms.CharField()
    radius = forms.CharField()
    video_id = forms.CharField()
    


