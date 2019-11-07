 
# Python Script for Webpages
top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()
project = open('content/art.html').read()
blog = open('content/Blog.html').read()
about = open('content/about.html').read()

art = top + project + bottom
blog = top + blog + bottom
about = top + about + bottom
open('docs/art.html', 'w+').write(art)
open('docs/blog.html', 'w+').write(blog)
open('docs/about.html', 'w+').write(about)
