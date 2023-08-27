import math

JINJA_FILTERS = {
    "count_to_font_size": lambda c: "{p:.1f}%".format(p=100 + 25 * math.log(c, 2)),
}

AUTHOR = "Zhang, Zijian"
SITENAME = "Zijian's Hunting Cabin"
SITEURL = "joshuaghost.github.io"

PATH = "content"
STATIC_PATHS = ["images", "pdfs", "blog", "pages", "extra"]
ARTICLE_PATHS = ["blog"]
ARTICLE_SAVE_AS = "{date:%Y}/{slug}.html"
ARTICLE_URL = "{date:%Y}/{slug}.html"

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("宋壬初", "http://renchusong.github.io/portfolio/"),
    ("Wrfly's blog", "http://wrfly.kfd.me/"),
    ("Avishek's Homepage", "https://www.l3s.de/~anand/"),
    ("Jaspreet's Homepage", "http://www.l3s.de/~singh/"),
    ("科学空间", "https://spaces.ac.cn/"),
)

# Social widget
SOCIAL = (
    ("GitHub", "http://github.com/JoshuaGhost"),
    ("Tweet", "http://twitter.com/Joshua_Ghost/"),
    ("Mail me", "mailto:zhangzijian0523@gmail.com"),
    ("My Medium page", "https://medium.com/@zhangzijian0523"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True

# Custom settings
USE_CUSTOM_MENU = True
SUMMARY_MAX_LENGTH = 25
THEME = "theme/foundation-default-colours/"
SITEDESCRIPTION = "Zijian's personal blog"
CONTACT_EMAIL = "zhangzijian0523@gmail.com"
PLUGINS = ["liquid_tags", "render_math"]
EXTRA_PATH_METADATA = {"extra/favicon.ico": {"path": "favicon.ico"}}
MATH_JAX = {
    # "color": "blue",
    "align": "left",
    "tex_extensions": ["color.js", "mhchem.js"],
}
FOUNDATION_PYGMENT_THEME = "emacs"
