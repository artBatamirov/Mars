import flask
from flask import request, make_response, jsonify

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'job_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['POST', 'GET'])
def get_jobs():
    if request.method == 'GET':
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        return flask.jsonify(
            {
                'news':
                    [item.to_dict(only=(
                'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                     for item in jobs]
            }
        )
    else:
        if not request.json:
            return make_response(jsonify({'error': 'Empty request'}), 400)
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader=request.json['team_leader'],
            job=request.json['job'],
            work_size=request.json['work_size'],
            collaborators=request.json['collaborators'],
            start_date=request.json['start_date'],
            end_date=request.json['end_date'],
            is_finished=request.json['is_finished']
        )
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'id': job.id})

@blueprint.route('/api/jobs/<int:job_id>')
def get_job_by_id(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
    if not job:
        return flask.make_response(flask.jsonify({'error': 'Not found'}), 404)
    return flask.jsonify(
        {
            'news':
                job.to_dict()

        }
    )

