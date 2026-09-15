
from datetime import datetime
import time
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


class RestrictTimeMiddleware(MiddlewareMixin):

    def process_request(self,request):
        self.start_time = time.time()
        current_hour = datetime.now().hour
        if  9 > current_hour or current_hour > 22:
            return HttpResponseForbidden('The site does not work before 9 and after 22')
        return None

    def process_response(self,request,response):
        self.end_time= time.time()
        execution_time = self.end_time - self.start_time
        print(f'{execution_time:.4f}')

        return response