from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Wolves
from myapp.wolves.forms import WolvesForm

wolves_posts = Blueprint('wolves_posts', __name__)

@wolves_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = WolvesForm()
    if form.validate_on_submit():
        wolf = Wolves(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(wolf)
        db.session.commit()
        flash('Wolf Created')
        print('Your Wolf was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)

# Make sure the wolves_id is an integer!

@wolves_posts.route('/<int:wolves_id>')
def wolf(wolves_id):
    wolf = Wolves.query.get_or_404(wolves_id) 
    return render_template('wolves.html', title=wolf.title, date=wolf.date, post=wolf)

@wolves_posts.route('/<int:wolves_id>/update',methods=['GET','POST'])
@login_required
def update(wolves_id):
    wolf = Wolves.query.get_or_404(wolves_id)

    if wolf.author != current_user:
        abort(403)

    form = WolvesForm()

    if form.validate_on_submit():
        wolf.title = form.title.data
        wolf.text = form.text.data
        db.session.commit()
        flash('Wolf Updated')
        return redirect(url_for('wolves_posts.wolf',wolves_id=wolf.id))

    elif request.method == 'GET':
        form.title.data = wolf.title
        form.text.data = wolf.text

    return render_template('create_post.html',title='Updating',form=form)

@wolves_posts.route('/<int:wolves_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(wolves_id):

    wolf = Wolves.query.get_or_404(wolves_id)
    if wolf.author != current_user:
        abort(403)

    db.session.delete(wolf)
    db.session.commit()
    flash('Wolf Deleted')
    return redirect(url_for('core.index'))