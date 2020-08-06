from django.shortcuts import render, redirect
from django.contrib import messages

from contact.forms import ContactForm


def message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['content']
            send_copy = form.cleaned_data['send_copy']
            form.save()

            if send_copy:
                print("There is Send Copy Checked!")
            messages.success(
                request, 'Thank you! Your message has been received!')
            return redirect('thanks')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def thanks(request):
    return render(request, 'contact/thanks.html')