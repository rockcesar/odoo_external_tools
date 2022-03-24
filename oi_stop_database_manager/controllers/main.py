'''
Created on Nov 18, 2018

@author: Zuhair Hammadi
'''
from odoo.addons.web.controllers.main import Database
from odoo import http, tools
from werkzeug.exceptions import BadRequest

import babel.messages.pofile
import base64
import copy
import datetime
import functools
import glob
import hashlib
import io
import itertools
import jinja2
import json
import logging
import operator
import os
import re
import sys
import tempfile

import werkzeug
import werkzeug.exceptions
import werkzeug.utils
import werkzeug.wrappers
import werkzeug.wsgi
from collections import OrderedDict, defaultdict, Counter
from werkzeug.urls import url_encode, url_decode, iri_to_uri
from lxml import etree
import unicodedata


import odoo
import odoo.modules.registry
from odoo.api import call_kw, Environment
from odoo.modules import get_module_path, get_resource_path
from odoo.tools import image_process, topological_sort, html_escape, pycompat, ustr, apply_inheritance_specs, lazy_property, float_repr
from odoo.tools.mimetypes import guess_mimetype
from odoo.tools.translate import _
from odoo.tools.misc import str2bool, xlsxwriter, file_open
from odoo.tools.safe_eval import safe_eval, time
from odoo.http import content_disposition, dispatch_rpc, request, serialize_exception as _serialize_exception, Response
from odoo.exceptions import AccessError, UserError, AccessDenied
from odoo.models import check_method_name
from odoo.service import db, security

_logger = logging.getLogger(__name__)

class MyDatabase(Database):

    @http.route()
    def selector(self, *args, **kwargs):    
        raise BadRequest()
    
    @http.route()
    def manager(self, *args, **kwargs):    
        raise BadRequest()
    
    @http.route()
    def create(self, *args, **kwargs):    
        raise BadRequest()
    
    @http.route()
    def duplicate(self, *args, **kwargs):    
        raise BadRequest()
    
    @http.route()
    def drop(self, *args, **kwargs):    
        raise BadRequest()
    
    #@http.route()
    #def backup(self, *args, **kwargs):    
    #    raise BadRequest()
        
    @http.route()
    def restore(self, *args, **kwargs):    
        raise BadRequest()                        
    
    @http.route()
    def change_password(self, *args, **kwargs):    
        raise BadRequest()         
    
    @http.route()
    def list(self, *args, **kwargs):    
        raise BadRequest()             
