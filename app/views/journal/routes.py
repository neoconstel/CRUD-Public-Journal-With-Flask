from flask import Blueprint, render_template, request, url_for,redirect
from flask_login import current_user
from .forms import AddJournalForm
from app.models import db, Journal, User

journal_bp = Blueprint("journal", __name__, url_prefix="/journal",
                        template_folder="templates", static_folder="static")


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