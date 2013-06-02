#!/usr/bin/env python
#-*-coding: utf8-*-

from tornado import web

from demo.views.base import BaseHandler
from demo.utils.decorate import render

from demo.models.contract_template import CTDAO
from demo.models.user import UserDAO

class CTListHandler(BaseHandler):
    @render("ct.html")
    @web.authenticated
    def get(self):
        return {}


class CTAjaxListHandler(BaseHandler):
    def check_xsrf_cookie(self):
        pass

    @render()
    @web.authenticated
    def post(self):
        page = int(self.get_argument("page", 1))
        offset = int(self.get_argument("row", 20))
        ok_img = self.static_url("img/ok.png")
        delete_img = self.static_url("img/delete.png")
        data = CTDAO.get_ct_list(page, ok_img, delete_img, offset)
        return data


class CTAddHandler(BaseHandler):
    @render("add_ct.html")
    @web.authenticated
    def get(self):
        data = UserDAO.get_users()
        return data


    @render()
    @web.authenticated
    def post(self):
        user_id = self.get_argument("user_id", None)
        if not user_id:
            return {"errmsg": u"请选择合同模板拥有者!"}
        tpl_name = self.get_argument("tpl_name", None)
        if not tpl_name:
            return {"errmsg": u"请填写合同模板名称!"}
        tpl_instruction = self.get_argument("tpl_instruction", None)
        if not tpl_instruction:
            return {"errmsg": u"请填写合同模板说明!"}
        tpl_content = self.get_argument("tpl_content", None)
        if not tpl_content:
            return {"errmsg": u"请填写合同模板内容!"}
        values = {"user_id": int(user_id),
                  "tpl_name": tpl_name,
                  "tpl_instruction": tpl_instruction,
                  "tpl_content": tpl_content}
        CTDAO.insert_new_ct(values)
        return {"msg": u"添加成功!"}


class CTUpdateHandler(BaseHandler):
    @render()
    @web.authenticated
    def post(self):
        pass


class CTRemoveHandler(BaseHandler):
    @render()
    @web.authenticated
    def post(self):
        ct_id = self.get_argument("ct_id", None)
        if not ct_id:
            return {"errmsg": u"删除失败"}
        CTDAO.remove_ct(ct_id)
        return {"msg": u"删除成功"}