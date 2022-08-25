from flask import Blueprint, render_template, request
from app.models import User, Journal
from flask_login import current_user
from app.views.journal.forms import EditJournalForm

home_bp = Blueprint("home", __name__, url_prefix="/home",
                        template_folder="templates", static_folder="static")


@home_bp.route("/", defaults={"page": None}) # for url args (example.com/?page=8)
@home_bp.route("/", methods=["GET", "POST"])
def homepage():
    edit_form = EditJournalForm()
    user = None
    if current_user.is_authenticated:    
        user = User.query.filter(User.username==current_user.username).first()

    # get the query object (not the query result) holding the required journals
    # so we can later add a pagination query to it
    journals_query = Journal.query.filter(
        (Journal.author==user)
        | (Journal.is_private==None) 
        | (Journal.is_private==False) ).order_by(Journal.id.desc())

    # pagination
    page_num = request.args.get("page")
    page_num = int(page_num) if page_num else None
    current_page = journals_query.paginate(page=page_num, per_page=2)
    journals = current_page.items

    return render_template("index.html", journals=journals,
                            edit_form=edit_form, current_page=current_page)
                            