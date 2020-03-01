from django.shortcuts import render

def Register(request):
	data = {}
	if request.method == "POST":
		input_data = request.POST

		## Write similar logic like employee add



	return render(request, "register.html", data)