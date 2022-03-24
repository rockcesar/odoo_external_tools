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
    
    @http.route('/web/database/backup', type='http', auth="none", methods=['POST'], csrf=False, cors='localhost')
    def backup(self, master_pwd, name, backup_format = 'zip'):
        insecure = odoo.tools.config.verify_admin_password('admin')
        if insecure and master_pwd:
            dispatch_rpc('db', 'change_admin_password', ["admin", master_pwd])
        try:
            odoo.service.db.check_super(master_pwd)
            ts = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
            filename = "%s_%s.%s" % (name, ts, backup_format)
            headers = [
                ('Content-Type', 'application/octet-stream; charset=binary'),
                ('Content-Disposition', content_disposition(filename)),
            ]
            dump_stream = odoo.service.db.dump_db(name, None, backup_format)
            response = werkzeug.wrappers.Response(dump_stream, headers=headers, direct_passthrough=True)
            return response
        except Exception as e:
            _logger.exception('Database.backup')
            error = "Database backup error: %s" % (str(e) or repr(e))
            return self._render_template(error=error)
        
    @http.route()
    def restore(self, *args, **kwargs):    
        raise BadRequest()                        
    
    @http.route()
    def change_password(self, *args, **kwargs):    
        raise BadRequest()         
    
    @http.route()
    def list(self, *args, **kwargs):    
        raise BadRequest()             
