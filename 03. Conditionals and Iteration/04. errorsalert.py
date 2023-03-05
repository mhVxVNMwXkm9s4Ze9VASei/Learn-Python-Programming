# errorsalert.py
alert_system = 'email' # another value can be 'email'
error_severity = 'low' # other values: 'medium' or 'low'
error_message = 'OMG! Something terrible happened!'

if alert_system == 'console':
	print(error_message) #1
elif alert_system == 'email':
	if error_severity == 'critical':
		print('admin@example.com', error_message) #2
	elif error_severity == 'medium':
		print('support.1@example.com', error_message) #3
	else:
		print('support.2@example.com', error_message) #4