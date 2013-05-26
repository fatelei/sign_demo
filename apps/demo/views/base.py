#!/usr/bin/env python
#-*-coding: utf8-*-

from tornado import web

from demo.models.user import UserDAO

class BaseHandler(web.RequestHandler):
    def get_login_url(self):
        return self.reverse_url("login")

    @property
    def user(self):
        return self.get_current_user()

    def get_current_user(self):
        user_id = self.get_secure_cookie("user_id")
        if user_id:
            user = UserDAO.get_user_by_user_id(user_id)
            if user:
                return user
            else:
                return None
        else:
            return None

    def render_string(self, template_name, **kwargs):
        """Generate the given template with the given arguments.

        We return the generated byte string (in utf8). To generate and
        write a template as a response, use render() above.
        """
        # If no template_path is specified, use the path of the calling file
        template_path = self.get_template_path()
        if not template_path:
            frame = sys._getframe(0)
            web_file = frame.f_code.co_filename
            while frame.f_code.co_filename == web_file:
                frame = frame.f_back
            template_path = os.path.dirname(frame.f_code.co_filename)
        with web.RequestHandler._template_loader_lock:
            if template_path not in web.RequestHandler._template_loaders:
                loader = self.create_template_loader(template_path)
                web.RequestHandler._template_loaders[template_path] = loader
            else:
                loader = web.RequestHandler._template_loaders[template_path]
        t = loader.load(template_name)
        kwargs.update({"current_user": self.user})
        namespace = self.get_template_namespace()
        namespace.update(kwargs)
        return t.generate(**namespace)