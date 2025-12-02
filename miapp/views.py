from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Movimiento

def mano_robotica_view(request):
    return render(request, 'miapp/ManoRobotica.html')


def login(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # --- REGISTRO ---
        if action == "register":
            if User.objects.filter(username=username).exists():
                messages.error(request, "El usuario ya existe")
                return redirect('login')

            User.objects.create_user(username=username, password=password)
            messages.success(request, "Usuario creado correctamente, ahora inicia sesión")
            return redirect('login')

        # --- LOGIN ---
        elif action == "login":
            user = authenticate(request, username=username, password=password)

            if user:
                auth_login(request, user)
                return redirect('ManoRobotica')  # Página después de iniciar sesión
            else:
                messages.error(request, "Credenciales incorrectas")
                return redirect('login')
    return render(request, 'miapp/login.html')

@csrf_exempt
@login_required
def guardar_movimiento(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Movimiento.objects.create(
            user=request.user,
            thumb=data["thumb"],
            index=data["index"],
            middle=data["middle"],
            ring=data["ring"],
            pinky=data["pinky"],
        )

        return JsonResponse({"status": "ok", "message": "Guardado con éxito"})

    return JsonResponse({"status": "error"}, status=400)




@login_required
def cargar_movimiento(request):
    ultimo = Movimiento.objects.filter(user=request.user).order_by("-fecha").first()

    if ultimo is None:
        return JsonResponse({"status": "no_data"})

    data = {
        "thumb": ultimo.thumb,
        "index": ultimo.index,
        "middle": ultimo.middle,
        "ring": ultimo.ring,
        "pinky": ultimo.pinky,
    }

    return JsonResponse({"status": "ok", "data": data})





