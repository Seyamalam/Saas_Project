import pathlib
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def homea_page_view(request, *args, **kwargs):
    print(this_dir)
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(html_)