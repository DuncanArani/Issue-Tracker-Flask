from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from .. import db,photos
from flask_login import login_required,current_user
import datetime

# Views
@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Perfect Pitch'
    if current_user.role_id == 1:
        return redirect(url_for('.admin'))
    elif current_user.role_id == 2:
        return redirect(url_for('.technician'))
    else:
        return redirect(url_for('.requester'))

    return render_template('index.html',title = title)

@main.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

@main.route('/technician')
def technician():
    return render_template('technician.html')

@main.route('/requester')
def requester():
    return render_template('requester.html')
