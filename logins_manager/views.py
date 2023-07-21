import json
from .models import Item, Folder
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render


overview_statistics = [
    {'name': 'My items', 'value': 4346},
    {'name': 'Weak passwords', 'value': 0},
]
pinned_items = [
    {'name': 'Google Login', 'username': 'myusername@gmail.com',
        'password': '********', 'url': 'https://www.google.com'},
    {'name': 'Twitter', 'username': '@mytwitterhandle',
        'password': '********', 'url': 'https://www.twitter.com'},
    {'name': 'Azure Portal', 'username': 'myusername@azure.com',
        'password': '********', 'url': 'https://portal.azure.com'},
    {'name': 'Facebook', 'username': 'myusername',
        'password': '********', 'url': 'https://www.facebook.com'},
    {'name': 'GitHub', 'username': 'myusername',
        'password': '********', 'url': 'https://www.github.com'},
    {'name': 'LinkedIn', 'username': 'myusername',
        'password': '********', 'url': 'https://www.linkedin.com'},
    {'name': 'Dropbox', 'username': 'myusername',
        'password': '********', 'url': 'https://www.dropbox.com'},
    {'name': 'Netflix', 'username': 'myusername',
        'password': '********', 'url': 'https://www.netflix.com'},
    {'name': 'Amazon', 'username': 'myusername',
        'password': '********', 'url': 'https://www.amazon.com'},
    {'name': 'Microsoft Account', 'username': 'myusername@hotmail.com',
        'password': '********', 'url': 'https://account.microsoft.com'},
]
organizations = [
    {'name': 'IT'},
    {'name': 'QA'},
    {'name': 'Cloud and Developments'}
]


@login_required
def index(request):
    context = {
        'overview_statistics': overview_statistics,
        'pinned_items': pinned_items,
        'organizations': organizations
    }
    return render(request, 'index.html', context)


@login_required
def create(request):
    data = [{'test': 'test'}, {'test': 'test'}, {'test': 'test'}]
    context = {'data': json.dumps(data)}
    return render(request, 'create.html', context)


@login_required
def item_list(request, folder_id):
    folder = get_object_or_404(
        Folder, id=folder_id, team__members=request.user)
    items = folder.items.filter(user=request.user)
    return render(request, 'item_list.html', {'items': items, 'folder': folder})


@login_required
def item_create(request, folder_id):
    folder = get_object_or_404(
        Folder, id=folder_id, team__members=request.user)
    if request.method == 'POST':
        item = Item.objects.create(
            title=request.POST['title'],
            username=request.POST['username'],
            password=request.POST['password'],
            extra_properties=request.POST.get('extra_properties', ''),
            notes=request.POST.get('notes', ''),
            user=request.user
        )
        folder.items.add(item)
        return redirect('item-list', folder_id=folder_id)

    return render(request, 'item_create.html', {'folder': folder})


@login_required
def item_update(request, folder_id, item_id):
    folder = get_object_or_404(
        Folder, id=folder_id, team__members=request.user)
    item = get_object_or_404(
        Item, id=item_id, user=request.user, folder=folder)

    if request.method == 'POST':
        item.title = request.POST['title']
        item.username = request.POST['username']
        item.password = request.POST['password']
        item.extra_properties = request.POST.get('extra_properties', '')
        item.notes = request.POST.get('notes', '')
        item.save()
        return redirect('item-list', folder_id=folder_id)

    return render(request, 'item_update.html', {'folder': folder, 'item': item})


@login_required
def item_delete(request, folder_id, item_id):
    folder = get_object_or_404(
        Folder, id=folder_id, team__members=request.user)
    item = get_object_or_404(
        Item, id=item_id, user=request.user, folder=folder)
    if request.method == 'POST':
        item.delete()
        return redirect('item-list', folder_id=folder_id)
    return render(request, 'item_delete.html', {'item': item, 'folder': folder})
