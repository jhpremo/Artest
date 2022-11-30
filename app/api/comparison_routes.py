from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Comparison
from sqlalchemy.orm import joinedload
from ..forms.comparison_form import CreateEditCompForm
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

@comparison_routes.post('')
@login_required
def post_set():
    data = request.json
    form = CreateEditCompForm(
        title=data.get("title"),
        work_1_title=data.get('work_1_title'),
        work_1_artist=data.get('work_1_artist'),
        work_1_image_url=data.get('work_1_image_url'),
        work_1_display_date=data.get('work_1_display_date'),
        work_2_title=data.get('work_2_title'),
        work_2_artist=data.get('work_2_artist'),
        work_2_image_url=data.get('work_2_image_url'),
        work_2_display_date=data.get('work_2_display_date'),
        comparison_text=data.get('comparison_text')
        )
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate():
        new_comp = Comparison(
        title=form.title.data,
        user_id=current_user.id,
        work_1_title=data.get('work_1_title'),
        work_1_artist=data.get('work_1_artist'),
        work_1_image_url=data.get('work_1_image_url'),
        work_1_display_date=data.get('work_1_display_date'),
        work_1_marker_obj=data.get('work_1_marker_obj'),
        work_2_title=data.get('work_2_title'),
        work_2_artist=data.get('work_2_artist'),
        work_2_image_url=data.get('work_2_image_url'),
        work_2_display_date=data.get('work_2_display_date'),
        work_2_marker_obj=data.get('work_2_marker_obj'),
        comparison_text=data.get('comparison_text')
        )
        db.session.add(new_comp)
        db.session.commit()
        return new_comp.to_dict()
    return form.errors


@comparison_routes.put("/<int:id>")
@login_required
def edit_comp(id):
    put_comp = Comparison.query.get(id)

    if put_comp == None:
        return {"message": "Comparison could not be found"}, 404

    if put_comp.user_id != int(current_user.get_id()):
        return {"message": "Forbidden"}, 403

    data = request.json
    form = CreateEditCompForm(
        title=data.get("title"),
        work_1_title=data.get('work_1_title'),
        work_1_artist=data.get('work_1_artist'),
        work_1_image_url=data.get('work_1_image_url'),
        work_1_display_date=data.get('work_1_display_date'),
        work_2_title=data.get('work_2_title'),
        work_2_artist=data.get('work_2_artist'),
        work_2_image_url=data.get('work_2_image_url'),
        work_2_display_date=data.get('work_2_display_date'),
        comparison_text=data.get('comparison_text')
        )
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate():
        put_comp.title=data.get('title')
        put_comp.work_1_title=data.get('work_1_title')
        put_comp.work_1_artist=data.get('work_1_artist')
        put_comp.work_1_image_url=data.get('work_1_image_url')
        put_comp.work_1_display_date=data.get('work_1_display_date')
        put_comp.work_1_marker_obj=data.get('work_1_marker_obj')
        put_comp.work_2_title=data.get('work_2_title')
        put_comp.work_2_artist=data.get('work_2_artist')
        put_comp.work_2_image_url=data.get('work_2_image_url')
        put_comp.work_2_display_date=data.get('work_2_display_date')
        put_comp.work_2_marker_obj=data.get('work_2_marker_obj')
        put_comp.comparison_text=data.get('comparison_text')
        db.session.commit()
        return put_comp.to_dict()
    return form.errors

@comparison_routes.delete("/<int:id>")
@login_required
def delete_comp(id):
    current_comp = Comparison.query.get(id)

    if current_comp == None:
        return {"message": "Comparison could not be found"}, 404

    if current_comp.user_id != int(current_user.get_id()):
        return {"message": "Forbidden"}, 403

    db.session.delete(current_comp)
    db.session.commit()
    return { "message": "Successfully deleted" }
