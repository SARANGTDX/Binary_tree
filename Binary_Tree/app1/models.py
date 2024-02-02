from django.db import models

# Create your models here.

class BinaryTree(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    vchr_name = models.CharField(max_length=100)
    vchr_type =  models.CharField(max_length=100)
    int_parent_id = models.IntegerField(null=True,blank=True)
    # bln_child = models.BooleanField(default=False)
