from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import never_cache
from duck.processor.processor import process
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


@never_cache
def logout_page(request):
    logout(request)
    return redirect("/")


@never_cache
def upload(request):
    if request.method == 'POST':
        try:
            uploaded_filename = process_uploaded_file(request)
            uploaded_file_path = './media/' + uploaded_filename
            process_result = process(uploaded_file_path)
            if process_result.result == '':
                return render(request, 'upload.html', {
                    'process_result': process_result
                })
            else:
                return render(request, 'upload.html', {
                    'error_message': 'Oops, you have used wrong file!'
                })
        except Exception as e:
            print('------------------------------------')
            print(e)
            print('------------------------------------')
            return render(request, 'upload.html', {
                'error_message': 'Oops, your file is in wrong format!'
            })
    else:
        if request.user.is_authenticated:
            return render(request, 'upload.html')
        else:
            return redirect("/login")


def process_uploaded_file(request):
    uploaded_file = request.FILES['document']

    print('file name:' + uploaded_file.name)
    print('content_type:' + uploaded_file.content_type)
    print('file size:' + str(uploaded_file.size))

    fs = FileSystemStorage()

    fs.save(uploaded_file.name, uploaded_file)

    return uploaded_file.name
