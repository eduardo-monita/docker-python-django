from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from example_app.models import Client

@csrf_exempt
def client_list(request):
    try:
        results = []
        clients = Client.objects.filter(active=True)
        for client in clients:
            results.append({
                "id": client.id,
                "name": client.name,
                "cpf": client.cpf,
                "birth_date": client.birth_date,
                "active": client.active,
                "created_at": client.created_at,
                "updated_at": client.updated_at
            })
        return JsonResponse({"clients": results})
    except Exception as e:
        return JsonResponse({"error": str(e)})

@csrf_exempt
def client_detail(request, client_id):
    try:
        if Client.objects.filter(pk=client_id, active=True).exists():
            client = Client.objects.get(pk=client_id, active=True)
        else:
            JsonResponse({"error": "Client id doesn't exists"})
        result = {
                "id": client.id,
                "name": client.name,
                "cpf": client.cpf,
                "birth_date": client.birth_date,
                "active": client.active,
                "created_at": client.created_at,
                "updated_at": client.updated_at
            }
        return JsonResponse({"client": result})
    except Exception as e:
        return JsonResponse({"error": str(e)})