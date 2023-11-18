#!/usr/bin/env python3

'''
Entry point to the application
'''
from flask import Flask, jsonify, request, abort, Response, redirect, url_for
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    '''
    Main index page
    '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    '''
    End-point that registers a user
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    '''
    Allow user login
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        Response = jsonify({"email": email, "message": "logged in"})
        Response.set_cookie("session_id", session_id)
        return Response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """ logout a user"""
    try:
        session_id = request.cookies.get("session_id")
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect("/")
        abort(403)
    except NoResultFound:
        abort(403)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
