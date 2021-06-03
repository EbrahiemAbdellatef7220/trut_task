# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request


class login(http.Controller):

    @http.route('/trust/login', type='http', auth="public", csrf=False)
    def index(self, **args):

        db = request.env.cr.dbname

        user_name = args.get('user_name') or False
        password = args.get('password') or False

        _response = {"data": None, "itemsCount": 0, "success": False, "statusCode": 404,
                     "message": ""}
        if not user_name:
            _response["message"] = "Missing UserName"
            return json.dumps(_response)

        if not password:
            _response["message"] = "Missing Password"
            return json.dumps(_response)

        user = request.env['res.users'].sudo().search([('login', '=', user_name)])
        if not user:
            _response["message"] = "UserName isn't exist "
            return json.dumps(_response)

        try:
            success = request.session.authenticate(db, user_name, password)
            if success:
                _response = {"data": request.session.sid, "itemsCount": 0, "success": True, "statusCode": 200,
                             "message": "Login Successful"}
                return json.dumps(_response)
            else:
                _response = {"data": None, "itemsCount": 0, "success": False, "statusCode": 404,
                             "message": "Password Incorrect !"}
                return json.dumps(_response)
        except Exception as e:
            _response = {"data": None, "itemsCount": 0, "success": False, "statusCode": 500, "message": str(e)}
            return json.dumps(_response)
