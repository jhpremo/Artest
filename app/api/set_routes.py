from flask import Blueprint, jsonify
from flask_login import login_required
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
        set_dct["user"]=featured_set.user.to_dict()
        payload.append(set_dct)
    return {"sets":payload}
