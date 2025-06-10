from django.shortcuts import redirect,render
from models import image
from formcustomer import imageform
def image(request):
        def image_upload(request):  
            if request.method == "POST":
                form = imageform(request.POST, request.FILES)
                if form.is_valid():
                    form.save()  # saves to MongoDB
                    return redirect('success')  # redirect to success page
                else:
                    return render(request, 'upload.html', {'form': form})
            else:
                form = imageform()
                return render(request, 'upload.html', {'form': form})


            return render(request,image)   