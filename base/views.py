from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe 


stripe.api_key = "sk_test_NMIcR8aD4uywmzL6yD6RpEpu00Bwny5raQ"

# Create your views here.

def index(request):
	return render(request, 'base/index.html')


def charge(request):
	amount=int(request.POST['amount'])
	if request.method == 'POST':
		print('Data:', request.POST)
		customer=stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['username'],
			source=request.POST['stripeToken']
		)
		
		charge=stripe.Charge.create(
			customer=customer,
			amount=amount,
			currency='INR',
			description="Donation"
		)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount':amount})