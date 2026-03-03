import json
import os
from django.shortcuts import render
from django.conf import settings

def load_data():
    file_path = os.path.join(settings.BASE_DIR, 'menu', 'data.json')
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def menu_list(request):
    items = load_data()

    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', 'all')

    # Search
    if search_query:
        items = [
            item for item in items
            if search_query.lower() in item['name'].lower()
        ]

    # Category filter
    if category_filter != "all":
        items = [
            item for item in items
            if item['category'] == category_filter
        ]

    # Get unique categories for dropdown
    categories = list(set(item['category'] for item in load_data()))

    context = {
        "items": items,
        "categories": categories,
    }

    return render(request, "menu/menu_list.html", context)