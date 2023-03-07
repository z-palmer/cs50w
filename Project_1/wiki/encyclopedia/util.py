import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


# def convert(document):
#     '''
#     Reads a markdown document and converts it to HTML
#     '''
#     heading = re.compile('^#{1,6}')
#     bold = re.compile(r'.*\*\*.*\*\*.*')
#     italic = re.compile(r'\s?\*\w*\*.*')
#     ul = re.compile(r'^[-*+]\w*')
#     link = re.compile(r'\[.*\]')
#     url = re.compile(r'\(.*\)')
#     list = False
#     paragraph = False
#     md = open(f'{document}.md')
#     f = open(
#         f'{document}.html', 'w+')
#     f.write('''
#     {% extends "encyclopedia/layout.html" %}

#     {% block body %}
#     ''')
#     for line in md:
#         for item in line.split():
#             if heading.search(item):
#                 raw_size = heading.findall(item)
#                 size = len(raw_size[0])
#                 f.write(f'<h{size}>' +
#                         line.lstrip(('#' * size)) + f'</h{size}>')
#                 break
#             elif bold.search(item):
#                 f.write('<b>' + item.strip('**') + '</b> ')
#             elif italic.search(item):
#                 f.write('<em>' + item.strip('*') + '</em> ')
#             elif link.search(item):
#                 raw_link = link.search(item)
#                 formatted_link = raw_link.group(0)
#                 route = url.search(item)
#                 href = route.group(0)
#                 f.write(item.split('[')[0] + '<a ')
#                 href.strip('()')
#                 f.write(f'href="{href}">' +
#                         formatted_link.strip('[]') + '</a> ')
#             else:
#                 if ul.search(line):
#                     continue
#                 elif line == '\n':
#                     continue
#                 else:
#                     f.write(item + ' ')
#         if ul.search(line) and list == False:
#             f.write('<ul>' + '<li>' + line.lstrip('* ') + '</li>')
#             list = True
#         elif ul.search(line) and list == True:
#             f.write('<li>' + line.lstrip('* ') + '</li>')
#         elif not ul.search(line) and list == True:
#             f.write('</ul>')
#             list = False
#         elif line == '\n' and paragraph == False:
#             f.write('<p>')
#             paragraph = True
#         elif line == '\n' and paragraph == 1:
#             f.write('</p>\n<p>')
#             paragraph = False
#     if paragraph == True:
#         f.write('\t\t</p>{% endblock %}')
#     else:
#         f.write('{% endblock %}')
#     return f
