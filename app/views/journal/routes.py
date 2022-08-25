from flask import Blueprint, render_template, request, url_for,redirect
from flask_login import current_user

from .forms import AddJournalForm, EditJournalForm
from app.models import db, Journal, User

journal_bp = Blueprint("journal", __name__, url_prefix="/journal",
                        template_folder="templates", static_folder="static")

PERMISSIONS = {
    "none": 0,
    "r": 1,
    "w": 2,
    "rw": 3
}


@journal_bp.route("/add", methods=["GET", "POST"])
def add_journal():
    form=AddJournalForm()

    if request.method == "GET":
        return render_template("add_journal.html", form=form)

    elif request.method == "POST":
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            private = form.is_private.data
            anonymous = form.is_anonymous.data
            
            author = User.query.filter(
                            User.username==current_user.username).first()
            new_journal = Journal(title=title, content=content, author=author,
            is_private=private, is_anonymous=anonymous)
            db.session.add(new_journal)
            db.session.commit()
            print(f"\n\n\nNew journal added!\n\n\n")

            return redirect(url_for("home.homepage"))

        else:
        # didn't validate
            print("\n\n\nDid not validate on submit\n\n\n")
            return redirect(url_for("journal.add_journal"))


@journal_bp.route("/read/<int:id>")
def read_journal(id):

    if request.method == "GET":
        journal = Journal.query.get(id)
        
        if not journal_access_granted(journal=journal, permission="r"):
            return f"<h1>Oops! 😳 Permission Denied</h1>"

        return render_template("read_journal.html", journal=journal)


@journal_bp.route("/edit/<int:id>", methods=["POST"])
def edit_journal(id):
    form = EditJournalForm()

    if request.method == "POST":
        
        if form.validate_on_submit():
            journal = Journal.query.get(id)

            if not journal_access_granted(journal=journal, permission="rw"):
                return f"<h1>Oops! 😳 Permission Denied</h1>"
            
            print(f"\n\n\nEditing Journal: {journal.title}\n\n\n")

            journal.title = form.title.data
            journal.content = form.content.data
            journal.is_private = form.is_private.data
            journal.is_anonymous = form.is_anonymous.data

            db.session.add(journal)
            db.session.commit()

            return redirect(url_for("home.homepage"))


@journal_bp.route("/delete/<int:id>", methods=["POST"])
def delete_journal(id):
    if request.method == "POST":
        journal = Journal.query.get(id)
        if not journal_access_granted(journal=journal, permission="w"):
            return f"<h1>Oops! 😳 Permission Denied</h1>"

        db.session.delete(journal)
        db.session.commit()
        print(f"J\n\n\nJournal: {journal.title} deleted\n\n\n")
        return redirect(request.referrer)


def journal_permission(journal: Journal, user: User):
    if journal.author == user:
        return PERMISSIONS["rw"]

    elif not journal.is_private:
        return PERMISSIONS["r"]

    else:
        return PERMISSIONS["none"]


def journal_access_granted(journal: Journal, permission: str):
    required_permission = PERMISSIONS[permission]
    user = None
    if current_user.is_authenticated:
        user = User.query.filter(User.username==current_user.username).first()
    else:
        user = User()
    if journal_permission(journal=journal, user=user) < required_permission:
        return False
    return True
    