from flask import Blueprint, jsonify

bp = Blueprint('sample', __name__)
from .tasks import add_2_digits, sub_2_digits


@bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Happy Day Ahead"})


@bp.route("/add", methods=["GET"])
def add_digits():
    add_2_digits.delay(2, 2)
    return jsonify({"message": "Added Successfully"})


@bp.route("/sub", methods=["GET"])
def sub_digits():
    sub_2_digits.delay(2, 2)
    return jsonify({"message": "Added Successfully"})
