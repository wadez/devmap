import os
import markdown
import markdown2
from string import Template


def main():
    walk(os.path.join(os.path.dirname(__file__), "posts"), ["md"])

def walk(path, extensions):
    data = []
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            _,ext = os.path.splitext(filename)
            filepath = os.path.join(subdir, filename)
            if ext[1:] in extensions:
                readFile(filepath, data)
    writeIndex(data)


def createStepper(gen):
    prv = None
    cur = next(gen)
    try:
        while True:
            nxt = next(gen)
            yield (prv, cur, nxt)
            prv = cur
            cur = nxt
    except StopIteration:
        yield (prv, cur, None)

def getLines(filepath, lines=[]):
    with open(filepath, 'r') as f:
        for line in f:
            lines.append(line)
            yield line

def getLineStepper(filepath, lines=[]):
    return createStepper(getLines(filepath, lines))

def getWords(filepath, lines=[]):
    for line in getLines(filepath, lines):
        for word in line.split():
            yield word

def getWordsStepper(filepath, lines=[]):
    return createStepper(getWords(filepath, lines))


def getFirstCommentBlock(filepath, lines=[]):
    valid = False
    gen = getWordsStepper(filepath, lines)
    for prevWord, word, nextWord in gen:
        prohibited = ["@", "<!--", "-->"]
        if (word == "<!--"):
            valid = True
            continue
        elif (word == "-->"):
            valid = False
            continue
        elif valid:
            if word[0] == "@":
                tag = word[1:]
                words = []
                while True:
                    g = next(gen)
                    if g != None:
                        p,w,n = g
                        if w not in prohibited:
                            words.append(w)
                        if n == None or n[0] in prohibited or n in prohibited:
                            break
                    else:
                        break

                yield [tag, " ".join(words)]



def readFile(filepath, files=[]):
    lines = []
    gen = getFirstCommentBlock(filepath, lines)
    settings = {}
    for tag,data in gen:
        print([tag, data])
        settings[tag] = data

    # html = markdown.markdown("".join(lines))
    html = markdown2.markdown("".join(lines), extras=['tables'])
    pagePath = os.path.join(os.path.dirname(__file__), "views", "pages", settings["slug"] + ".html")
    # print(pagePath, html)
    with open(pagePath, 'w') as f:
        content = """{% extends 'layouts/page.html' %}

{% block title %}
  $title
{% endblock %}

{% block page %}
  <h1 class="display">$title</h1>
  $html
{% endblock %}
        """
        template = Template(content)
        render = template.substitute(html=html, title=settings['title'])
        f.write(render)
        files.append(settings)

def writeIndex(files):
    links = []
    for settings in files:
        slug = settings['slug']
        title = settings['title']
        links.append(f'<li><a href="/p/{slug}.html">{title}</a></li>')

    pagePath = os.path.join(os.path.dirname(__file__), "views", "index.html")
    with open(pagePath, 'w') as f:
        content = """{% extends 'layouts/welcome.html' %}

        {% block links %}
          $html
        {% endblock %}
                """
        template = Template(content)
        render = template.substitute(html="".join(links))
        f.write(render)

if __name__ == "__main__":
    main()
