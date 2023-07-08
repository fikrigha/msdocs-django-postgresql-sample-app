from django.shortcuts import render

overview_statistics = [
    {'name': 'My items', 'value': 4346},
    {'name': 'Weak passwords', 'value': 0},
]
pinned_items = [
    {'name': 'Google Login', 'username': 'myusername@gmail.com', 'password': '********', 'url': 'https://www.google.com'},
    {'name': 'Twitter', 'username': '@mytwitterhandle', 'password': '********', 'url': 'https://www.twitter.com'},
    {'name': 'Azure Portal', 'username': 'myusername@azure.com', 'password': '********', 'url': 'https://portal.azure.com'},
    {'name': 'Facebook', 'username': 'myusername', 'password': '********', 'url': 'https://www.facebook.com'},
    {'name': 'GitHub', 'username': 'myusername', 'password': '********', 'url': 'https://www.github.com'},
    {'name': 'LinkedIn', 'username': 'myusername', 'password': '********', 'url': 'https://www.linkedin.com'},
    {'name': 'Dropbox', 'username': 'myusername', 'password': '********', 'url': 'https://www.dropbox.com'},
    {'name': 'Netflix', 'username': 'myusername', 'password': '********', 'url': 'https://www.netflix.com'},
    {'name': 'Amazon', 'username': 'myusername', 'password': '********', 'url': 'https://www.amazon.com'},
    {'name': 'Microsoft Account', 'username': 'myusername@hotmail.com', 'password': '********', 'url': 'https://account.microsoft.com'},
]
organizations = [
    {'name': 'IT'},
    {'name': 'QA'},
    {'name': 'Cloud and Developments'}
]

# Create your views here.
def index(request):
    context = {
        'overview_statistics': overview_statistics,
        'pinned_items': pinned_items,
        'organizations': organizations
    }
    return render(request, 'index.html', context)