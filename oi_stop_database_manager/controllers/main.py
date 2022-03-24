'''
Created on Nov 18, 2018

@author: Zuhair Hammadi
'''
from odoo.addons.web.controllers.main import Database
from odoo import http
from werkzeug.exceptions import BadRequest

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
