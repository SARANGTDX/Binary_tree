from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BinaryTree
# Create your views here.

class HomePageApi(APIView):
    def get(self, request):
        ins_name =  BinaryTree.objects.values()
        return render(request, "home.html",{'names':ins_name})

class BinaryTreeApi(APIView):
    def post(self,request):
        # import pdb;pdb.set_trace()
        data = request.data
        ins_parent = BinaryTree.objects.create(
            vchr_name = data.get('parent_name'),
            vchr_type = data.get('type'),
            int_parent_id = BinaryTree.objects.values('pk_bint_id').last().get('pk_bint_id') if BinaryTree.objects.exists() else None,
        )
        ins_parent.save()

        ins_child = BinaryTree.objects.create(
            vchr_name = data.get('child_name'),
            vchr_type = data.get('type'),
            int_parent_id = ins_parent.pk_bint_id,
            bln_child = True,
        )
        ins_parent.save()
        
        return render(request, "home.html")

class ListTree(APIView):
    def get(self,request):
        # ins_data =  BinaryTree.objects.values()
        # ins_name =  BinaryTree.objects.values('vchr_name')
        # if ins_data:
        #     dct_data ={}

        #     for data in ins_data:
        #         if 'parent'  not in dct_data.keys():
        #             dct_data['parent'] = ins_data[0].get('vchr_name')
        #             dct_data['id'] = ins_data[0].get('pk_bint_id')
        #             dct_data['lst_data'] = []
                      
                    
        
        return render(request, "tree.html")

class SearchApi(APIView):
    # def get(self,request):
        
       
    #     return render(request, "tree.html")

    def post(self,request):
        # ins_data = BinaryTree.objects.fiter()
        return render(request, "tree.html")
        