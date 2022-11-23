from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import db, Set, SetCard
from sqlalchemy.orm import joinedload
from random import *

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
