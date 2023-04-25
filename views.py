from flask import Blueprint, render_template,request,flash,redirect,url_for
from .models import Note
from .forms import CreateNotesForm,UpdateNotesForm
from . import db
from flask_login import login_required,current_user

views = Blueprint('views', __name__)

#Route for the navigation page
@views.route('/')
def base():

    return render_template('base.html',user=current_user)

#Route for the home page
@views.route('/home',methods=['POST','GET'])
@login_required
def home():
    notes = Note.query.all()
    return render_template('home.html',notes=notes,user=current_user)

#Route for the create-notes page
@views.route('/notes/new', methods=['POST', 'GET'])
def create_notes():
    form = CreateNotesForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        notes = Note(title=title, content=content, author=current_user.id)
        db.session.add(notes)
        db.session.commit()
        flash('Notes created!', category='success')
        return redirect(url_for('views.home'))

    return render_template('notes.html',user=current_user,form=form)

#Route for the update-notes page
@views.route('/notes/<int:id>/update', methods=['POST','GET'])
def update_notes(id):
    form = UpdateNotesForm()
    notes = Note.query.filter_by(id=id).first()
    if form.validate_on_submit():
        new_title = form.title.data
        new_content = form.content.data

        notes.title = new_title
        notes.content = new_content
        db.session.commit()
        return redirect(url_for('views.home'))
    
    return render_template('update-notes.html',form=form,user=current_user)

#Route for deleting a note
@views.route('/notes/<int:id>/delete')
def delete_notes(id):
    notes = Note.query.filter_by(id=id).first()
    db.session.delete(notes)
    db.session.commit()
    return redirect(url_for('views.home'))
