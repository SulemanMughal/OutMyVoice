


# ****************************************************************
# Find Response Object for a given petition
# ****************************************************************

from django import template
from mysite.models import *
from django.contrib.auth.models import User

register = template.Library()


def FindResponseObject(user_value, petition_id):
    try:
        response = PetitionResponseFeedback.objects.get(
            user=User.objects.get(id=user_value), 
            petition = Petition.objects.get(id=petition_id)
        )
        return response
    except:
        return None

register.filter(FindResponseObject)