from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Set, SetCard
from sqlalchemy.orm import joinedload
from random import *
from ..forms.set_form import CreateEditSetForm
from ..forms.card_form import CreateEditCardForm

set_routes = Blueprint('sets', __name__)


@set_routes.get('/featured')
def get_featured():
    all_sets = Set.query.options(joinedload(Set.user)).all()
    featured = sample(all_sets, k=6)
    payload=[]
    for featured_set in featured:
        set_dct = featured_set.to_dict()
        set_dct["username"]=featured_set.user.username
        cards = SetCard.query.filter(SetCard.set_id == featured_set.id).all()
        set_dct["cards"]=[card.to_dict() for card in cards]
        set_dct["numCards"]=len(set_dct["cards"])
        payload.append(set_dct)
    return {"sets":payload}


@set_routes.get('/session')
@login_required
def get_session_sets():
    all_sets = Set.query.options(joinedload(Set.user), joinedload(Set.cards)).filter(Set.user_id==current_user.id).all()
    payload=[]
    for user_set in all_sets:
        set_dct = user_set.to_dict()
        set_dct["username"]=user_set.user.username
        set_dct["cards"]=[card.to_dict() for card in user_set.cards]
        set_dct["numCards"]=len(set_dct["cards"])
        payload.append(set_dct)
    return {"sets":payload}

@set_routes.get("/<int:id>")
def get_one_set(id):
    print("-------------",id)
    one_set = Set.query.options(joinedload(Set.user), joinedload(Set.cards)).get(id)
    if not one_set:
        return {"message": "Set not found"}, 404
    else:
        set_dct = one_set.to_dict()
        set_dct["username"]=one_set.user.username
        set_dct["cards"]=[card.to_dict() for card in one_set.cards]
        set_dct["numCards"]=len(set_dct["cards"])
        return {"sets":[set_dct]}

@set_routes.post('')
@login_required
def post_set():
    data = request.json
    form = CreateEditSetForm(title=data["title"])
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate():
        new_set = Set(title=form.title.data, user_id=current_user.id)
        db.session.add(new_set)
        db.session.commit()
        return new_set.to_dict()
    return form.errors


@set_routes.put("/<int:id>")
@login_required
def edit_set(id):
    put_set = Set.query.get(id)

    if put_set == None:
        return {"message": "Set could not be found"}, 404

    if put_set.user_id != int(current_user.get_id()):
        return {"message": "Forbidden"}, 403

    data = request.json
    form = CreateEditSetForm(title=data["title"])
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate():
        put_set.title = form.data['title']
        db.session.commit()
        return put_set.to_dict()
    return form.errors

@set_routes.delete("/<int:id>")
@login_required
def delete_set(id):
    deleted_set = Set.query.get(id)

    if deleted_set == None:
        return {"message": "Set could not be found"}, 404

    if deleted_set.user_id != int(current_user.get_id()):
        return {"message": "Forbidden"}, 403

    db.session.delete(deleted_set)
    db.session.commit()
    return { "message": "Successfully deleted" }

@set_routes.post("/<int:id>/cards")
@login_required
def post_set_card(id):
    current_set = Set.query.get(id)

    if current_set == None:
        return {"message": "Set could not be found"}, 404

    if current_set.user_id != int(current_user.get_id()):
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
        new_card = SetCard(
        title=form.title.data,
        set_id=id,
        artist=form.artist.data,
        image_url=form.image_url.data,
        display_date=form.display_date.data,
        notes=data.get('notes'),
        marker_obj=data.get('marker_obj')
        )
        db.session.add(new_card)
        db.session.commit()
        return new_card.to_dict()
    return form.errors
