from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'wordcounter/index.html')

def counter(request):
    text = request.POST['words']
    amount = len(text.split()) if text else 0
    return render(request, 'wordcounter/counter.html', {
        'amount': amount,
        'text': text,
    })