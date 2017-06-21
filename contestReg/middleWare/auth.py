from django.shortcuts import redirect
from django.http import HttpResponseRedirect

class AuthenticationMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response
		# One-time configuration and initialization.

	def __call__(self, request):
		# Code to be executed for each request before
		# the view (and later middleware) are called.
		if '/login/' != request.get_full_path():
		# print(dir(request))
			print('checking....')
			if request.session.get('logged',False) is not True:
				print('Redirecting .....')
				return HttpResponseRedirect('/login/')
		response = self.get_response(request)
		return response