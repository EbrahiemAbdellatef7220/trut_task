# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request


class GetPartners(http.Controller):

    @http.route('/trust/company_partner', type='http', auth="user", csrf=False)
    def index(self, **args):

        comp_id = args.get('company_id') or False

        _response = {"data": None, "itemsCount": 0, "success": False, "statusCode": 404,
                     "message": ""}

        if not comp_id:
            _response["message"] = "Missing Company ID"
            return json.dumps(_response)

        Partners = []
        try:
            partner = request.env['res.partner'].sudo().search([('company_id', '=', comp_id)])
            if partner:
                
                for p in partner:
                    Partners.append(p.name)
                    
                _response = {"data": Partners, "itemsCount": 0, "success": True, "statusCode": 200,
                             "message": "success"}
                return json.dumps(_response)
            else:
                _response["message"] = "This Company Doesn't Have any Partner "
                return json.dumps(_response)

        except Exception as e:
            _response = {"data": None, "itemsCount": 0, "success": False, "statusCode": 500, "message": str(e)}
            return json.dumps(_response)
