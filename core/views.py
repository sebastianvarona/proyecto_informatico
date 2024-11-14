from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import XRayDiagnosis

# Create your views here.


@login_required
def home(request):
    diagnosis = XRayDiagnosis.objects.all()
    return render(request, 'index.html', {'diagnosis': diagnosis})

@login_required
def diagnosis_detail(request, diagnosis_id):
    diagnosis = get_object_or_404(XRayDiagnosis, id=diagnosis_id)
    return render(request, 'diagnosis_detail.html', {'diagnosis': diagnosis})

