from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Ticket
from .. import db,photos
from flask_login import login_required,current_user
import datetime
from .forms import TicketsForm
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

    return render_template('index.html',title = title,requester=requester)

@main.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

@main.route('/technician')
def technician():
    return render_template('technician.html')

@main.route('/requester',methods=["GET","POST"])
@login_required
def requester():

    form = TicketsForm()

    if form.validate_on_submit():
        
        ticket = Ticket(ticket_title = form.title.data, ticket_description = form.description.data)

        ticket.save_ticket()

        flash('request successfull!')

        return redirect(url_for('.ticket'))

    
    return render_template('requester.html', form =form)

@main.route('/ticket',methods= ['GET','POST'])
def ticket():
   '''
   View root page function that returns the dashboard page and its data
   '''
   form=TicketsForm()

   tickets = Ticket.query.filter_by().all()

   if form.validate_on_submit():
       title = form.title.data
       description=form.description.data
       new_ticket=Ticket(ticket_title=title,ticket_description=description,ticket=current_user)
       new_ticket.save_ticket()
       return redirect(url_for('.requester'))
   return render_template('tickets.html',ticket_form=form,tickets = tickets)


