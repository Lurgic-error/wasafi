from PIL import Image
from django import forms
from django.core.files import File
from api.models import Images
from django.contrib.auth.models import User
from account.models import Profile

class ImageForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Images
        fields = ('file', 'x', 'y', 'width', 'height', )

    def save(self,request):
        photo = super(ImageForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        username = request.POST.get('username')




        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        try:
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            profile.image = photo;
            profile.save();
            return user
        except User.DoesNotExist:
            return None


