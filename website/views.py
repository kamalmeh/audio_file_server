"""
Frontend of the project i.e website
"""
from django.shortcuts import render
from django.views import View

class Home(View):
    """
    End Point   : /server/delete/
    Parameters  : None
    Author      : Kamal Mehta
    Created     : 15-Mar-2021
    Last Updated: 16-Mar-2021
    Update Logs :
        16-Mar-2021 - Updated docstring Log
        15-Mar-2021 - Created
    """
    def get(self, request):
        """HTTP Get Method Override"""
        return render(request, "home.html")