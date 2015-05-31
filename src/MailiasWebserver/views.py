'''
Created on May 30, 2015

@author: Gavi
'''

from django.views.generic import View
from django.shortcuts import render

class HomePageView(View):
    def get(self, request):
        
        site = "index.html"
        return render(request, site)
