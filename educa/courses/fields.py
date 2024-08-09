# for automatic indexing of the content  object
from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    def __init__(self,for_fields=None,*args,**kwargs):
        self.for_fields = for_fields
        super().__init__(*args,**kwargs)
        
        
    # custom method for the if any value is not given then we will check then before save
    # give the value after calculation and save it 
    def pre_save(self,model_instance,add):
        if getattr(model_instance,self.attname) is None:
            # the value given is 0 then have to calculate it
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    query = { field : getattr(model_instance,add) for field in self.for_fields }
                    qs = qs.filter(**query)
                # get the last item of the query
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            
            setattr(model_instance,add,value)
            return value
        else:
            return super().pre_save(model_instance,add)