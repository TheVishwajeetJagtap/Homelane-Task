from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from urllib import request
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.