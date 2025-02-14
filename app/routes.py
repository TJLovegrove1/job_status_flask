from flask import Blueprint, render_template
import json
from pathlib import Path

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    data_file = Path(__file__).parent.parent / 'data' / 'data.json'
    with data_file.open('r') as file:
        data = json.load(file)
    return render_template('index.html', jobs=data['jobs'])
