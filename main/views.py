from django.shortcuts import render,redirect
from .models import ConsultationRequest,TeamMember
from django.core.mail import send_mail

# Create your views here.
def index(request):
    
    team_members= TeamMember.objects.filter(is_active=True)
    
    context = {
        'team_members': team_members
    }
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        
        # save in database
        ConsultationRequest.objects.create(
            full_name=full_name,
            email=email,
            phone=phone
        )
        
        #send to email
        send_mail(subject='New Consultation Request',
                  message=f'''
You have recieved a new consultationn request.
                  
Full Name = {full_name}
Email = {email}
Phone Number = {phone}
                  
                  
            Submitted through the website''',
from_email='emogyee@gmail.com',
recipient_list = ['emogyee@gmail.com'],
fail_silently = False
)
        
        return redirect('index')
        
        
    return render(request,'index.html',context)
