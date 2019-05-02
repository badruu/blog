from flask import render_template, request, Blueprint
from pitch.models import Post
from pitch.request import get_quote

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    quote=get_quote()
    title = 'Welcome to quotes'
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', title=title, quote=quote, posts = posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/quotes")
def quotes():
    quote=get_quote()
    title = 'Welcome to quotes'

    return render_template('quote.html', title=title, quote=quote)