from django.http import HttpResponse

from django.shortcuts import render

def index(request):

    return render(request,'index.html')


def analyze(request):

 #getting text
 djtext= request.POST.get('text','defualt')

 #checkbox selection
 removepunc=request.POST.get('removepunc','off')
 fullcaps=request.POST.get('fullcaps','off')
 newlineremove=request.POST.get('newlineremove','off')
 exspaceremover=request.POST.get('exspaceremover','off')
 countchar=request.POST.get('countchar','off')

#perform if statements on selected checkboxes
 if removepunc=="on":
     punctuation='''!@#$%^&*()_+~`{}[]|\:;"'<,>.?/='''
     analyze=""
     for char in djtext:
         if char not in punctuation:
             analyze=analyze+char

     parms={'purpose':'Remove Punctuations' , 'analyze_text':analyze}
     djtext = analyze

 if fullcaps=="on":
     analyze=""
     for char in djtext:
         analyze=analyze+char.upper()


     parms={'purpose':'convert the text in UPPERCASE' , 'analyze_text':analyze}
     djtext = analyze


 if newlineremove=="on":
     analyze=""
     for char in djtext:
         if char!="\n" and char!="\r":
             analyze=analyze+char


     parms={'purpose':'Remove New Lines' , 'analyze_text':analyze}
     djtext = analyze


 if exspaceremover=="on":
     analyze=""
     for index,char in enumerate(djtext):
         if not(djtext[index]==" " and djtext[index+1]==" "):
             analyze=analyze+char


     parms={'purpose':'Remove extra spaces' , 'analyze_text':analyze}
     djtext = analyze


 if (removepunc!="on" and fullcaps!="on" and exspaceremover!="on" and newlineremove!="on" and countchar!="on"):
     return HttpResponse("Error")
 return render(request, 'analyze.html',parms)




