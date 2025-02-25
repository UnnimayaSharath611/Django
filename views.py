from django.shortcuts import render,redirect
from .models import Profile
from .forms import ContactForm
from .models import FooterData 

# Create your views here.
def get_footer_data():
    # Get the first footer entry (FooterData)
    footer_data = FooterData.objects.first()
    
    if footer_data:
        return {
            'phone_number': footer_data.phone_number,
            'email': footer_data.email,
            'linkedin': footer_data.linkedin,
            'twitter': footer_data.twitter,
            'instagram': footer_data.instagram,
        }
    else:
        return {
            'phone_number': 'Not available',
            'email': 'Not available',
            'linkedin': '#',
            'twitter': '#',
            'instagram': '#',
        }
def home(request):
    context = {
        'profile_name': 'Unnimaya Sharath',
        'profile_description': 'Web Developer',
        'social_links': {
            'linkedin': 'https://linkedin.com/in/unnimaya-sharath',
            'twitter': 'https://twitter.com/unnimaya',
            'instagram': 'https://www.instagram.com/unniimayaa?igsh=MXE4YmQxZnpxbmdiag==',
        },
        'footer_data': get_footer_data(),  # Ensure it's consistent
    }
    return render(request, 'portfolio/portfolio.html', context)

def resume(request):
    profile = Profile.objects.prefetch_related(
        'education', 'experience_entries', 'skill_entries', 'social_links',
    ).first()
    
    footer_data = get_footer_data()  # Ensure it's consistent
    return render(request, 'portfolio/resume.html', {'profile': profile, 'footer_data': footer_data})

def projects(request):
    footer_data = get_footer_data()  # Ensure it's consistent
    return render(request, 'portfolio/project.html', {'footer_data': footer_data})

def contact(request):
    form_submitted = False
    footer_data = get_footer_data()  # Ensure it's consistent

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves to database if using ModelForm
            form_submitted = True
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {
        'form': form,
        'form_submitted': form_submitted,
        'footer_data': footer_data,
    })
