# -*- coding: utf8 -*- 

# imports
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext

from documents.models import Document 

import locale
import sys
# this must be passed to template: 

# Create your views here.

def index(request):
    return render_to_response('exteriors/index.html', locals(),
    			context_instance=RequestContext(request)) 