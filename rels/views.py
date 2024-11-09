from django.shortcuts import redirect, render
from django.views import View
from rels.models import RealState
from rels.forms import RelsForm

# Create your views here.
class RelsCreateView(View):
    template_name="rels_create.html"
    form_class=RelsForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            RealState.objects.create(**data)
            
            # return redirect("rels-a")
        return render(request,self.template_name,{"form":form_instance})
    

class RelsLIStView(View):
    
    template_name="rels_list.html"
    
    def get(self,request,*args,**kwargs):
        
        qs=RealState.objects.all()
        
        return render (request,self.template_name,{"data":qs})
    

class RelsUpdateView(View):
    
    template_name="rels_edit.html"
    
    form_class=RelsForm
    
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        
        rels_object=RealState.objects.get(id=id)
    
        form_instance=self.form_class(instance=rels_object)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
       
        rels_object=RealState.objects.get(id=id)
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES,instance=rels_object)
        
        if form_instance.is_valid():
            
            form_instance.save()
    
            return redirect("rels-list")
        
        return render(request,self.template_name,{"form":form_instance})



class RelsDetailVIew(View):
    
    template_name="rels-detail.html"
    
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        
        qs=RealState.objects.get(id=id)
        
        return render (request,self.template_name,{"data":qs})


class RelsDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        
        RealState.objects.get(id=id).delete()
        
        return redirect("rels-list")
