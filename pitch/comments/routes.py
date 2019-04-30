
from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from pitch import db
from pitch.models import Comment
from pitch.comments.forms import CommentForm

comments = Blueprint('comments', __name__)

@comments.route("/comment/new", methods=['GET', 'POST'])
@login_required
def new_comment():
    form=CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data, author=current_user)
        db.session.add(comment)
        db.session.commit()
        flash('You have commented on this pitch!', 'success')
        return redirect(url_for('main.home'))
    return render_template('comment_post.html', title='New Comment', form=form, legend= 'New Comment')


@comments.route("/comment/<int:Comment_id>")
def comment(Comment_id):
    comment = Comment.query.get_or_404(Comment_id)
    return render_template('comment.html', comment=comment)


@comments.route("/comment/<int:Comment_id>/update", methods=['GET', 'POST'])
@login_required
def update_comment(Comment_id):
    comment = Comment.query.get_or_404(Comment_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment.comment = form.comment.data
        db.session.commit()
        flash('You have commented on this pitch!', 'success')
        return redirect(url_for('comments.comment', Comment_id=comment.id))
    elif request.method == 'GET':
        form.comment.data = comment.comment
    return render_template('comment_post.html', title='comment post', form=form, legend='update comment')
    
@comments.route("/post/<int:Comment_id>/delete", methods=['POST'])
def delete_comment(Comment_id):
    comment = Comment.query.get_or_404(post_id)
    if comment.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Your comment has been deleted!', 'success')
    return redirect(url_for('main.home'))