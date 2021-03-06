from urllib.parse import urlparse
from urllib.parse import parse_qs
from django import template

register = template.Library()


def get_page(url):
    """Return current page number after URL Parsing."""

    parsed = urlparse(url)
    return int(parse_qs(parsed.query)["page"][0])


@register.filter(name="prevpage")
def prevpage(url, cur):
    """Change the URL to previous page number."""

    if url.find("&page=") > -1:
        page = get_page(url)
        return url.replace(f"page={page}", f"page={page-1}")
    else:
        return f"{url}&page={cur-1}"


@register.filter(name="nextpage")
def nextpage(url, cur):
    """Change the URL to next page number."""

    if url.find("&page=") > -1:
        page = get_page(url)
        return url.replace(f"page={page}", f"page={page+1}")
    else:
        return f"{url}&page={cur+1}"
