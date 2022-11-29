from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Comparison
from sqlalchemy.orm import joinedload
from random import *

comparison_routes = Blueprint('comparisons', __name__)


@comparison_routes.get('/featured')
def get_featured():
    all_comps = Comparison.query.options(joinedload(Comparison.user)).all()
    featured = sample(all_comps, k=3)
    payload = []
    for comp in featured:
        comp_dct = comp.to_dict()
        comp_dct['username']=comp.user.username
        payload.append(comp_dct)
    return {"comparisons":payload}


@comparison_routes.get('/session')
@login_required
def get_session_comps():
    all_comps = Comparison.query.options(joinedload(Comparison.user)).filter(Comparison.user_id==current_user.id).all()
    payload = []
    for comp in all_comps:
        comp_dct = comp.to_dict()
        comp_dct['username']=comp.user.username
        payload.append(comp_dct)
    return {"comparisons":payload}

@comparison_routes.get("/<int:id>")
def get_one_comp(id):
    one_comp = Comparison.query.options(joinedload(Comparison.user)).get(id)
    if not one_comp:
        return {"message": "Comparison not found"}, 404
    else:
        comp_dct = one_comp.to_dict()
        comp_dct['username'] = one_comp.user.username
        return {"comparisons":[comp_dct]}
