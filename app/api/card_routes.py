from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Set, SetCard
from sqlalchemy.orm import joinedload
from random import *
from ..forms.card_form import CreateEditCardForm

card_routes = Blueprint('cards', __name__)

@card_routes.put("/<int:id>")
@login_required
def edit_set_card(id):
    current_card = SetCard.query.options(joinedload(SetCard.card_set)).get(id)

    if current_card == None:
        return {"message": "Card could not be found"}, 404

    if current_card.card_set.user_id != int(current_user.get_id()):
        return {"message": "Forbidden"}, 403

    data = request.json
    form = CreateEditCardForm(
        title=data.get("title"),
        artist=data.get('artist'),
        image_url=data.get('image_url'),
        display_date=data.get('display_date'),
        notes=data.get('notes')
        )
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate():
        current_card.title = form.title.data
        current_card.artist = form.artist.data
        current_card.image_url = form.image_url.data
        current_card.display_date = form.display_date.data
        current_card.notes = data.get('notes')
        current_card.marker_obj = data.get('marker_obj')

        db.session.commit()
        return new_card.to_dict()
    return form.errors

@card_routes.delete("/<int:id>")
@login_required
def delete_set_card(id):
    current_card = SetCard.query.options(joinedload(SetCard.card_set)).get(id)

    if current_card == None:
        return {"message": "Card could not be found"}, 404

    if current_card.card_set.user_id != int(current_user.get_id()):
        return {"message": "Forbidden"}, 403

    db.session.delete(current_card)
    db.session.commit()
    return { "message": "Successfully deleted" }
