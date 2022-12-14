from django.shortcuts import render
from django.utils.decorators import method_decorator
# from ratelimit.decorators import ratelimit
from django.views import View
from .utils import FileReader, TextMatch


class FirstView(View):
    """Create simple interface that contains drop-down list with all keys from the file and a search button. """

    # @method_decorator(ratelimit(key='ip', rate='5/m', method='GET'))
    def get(self, request):
        reader = FileReader()
        context = {"keys": reader.read_keys()}
        return render(request, "interface.html", context)


class SecondView(View):
    """Create simple table to list all of the results for example """

    # @method_decorator(ratelimit(key='ip', rate='5/m', method='GET'))
    def get(self, request):
        context = {}
        if request.GET.get('key'):
            key = request.GET.get('key')
            algo = TextMatch()
            matches = algo.matching(key, FileReader().read_keys())
            # We are aiming to find all similar values of a selected key and the percentage
            context = {"matches": matches , "key": key}
        return render(request, "response.html", context)
