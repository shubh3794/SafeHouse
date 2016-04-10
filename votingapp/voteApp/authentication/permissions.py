from rest_framework import permissions

class IsAccountOwner(permissions.BasePermission):
	'''returns true if the user is owner of account being accessed'''
	def has_object_permission(self, request, view, account):
		'''perm object'''
		if request.user:
			return account == request.user
		return False

class IsReportedBy(permissions.BasePermission):
	'''returns true if the user is owner of ques being accessed'''
	def has_object_permission(self, request, view, disaster):
		'''perm object'''
		if request.user:
			return disaster.reportedby == request.user
		return False


