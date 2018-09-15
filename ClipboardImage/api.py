from flask import request, jsonify, Response
from werkzeug.utils import secure_filename

from pathlib import Path
from datetime import datetime
from nonrepeat import nonrepeat_filename
import shutil

from . import app

filename = None


@app.route('/api/images/create', methods=['POST'])
def create_image():
    global filename

    if 'file' in request.files:
        image_path = Path(request.form.get('imagePath'))
        if image_path.suffix:
            image_path = image_path.parent
        image_path.mkdir(parents=True, exist_ok=True)

        file = request.files['file']
        filename = str(image_path.joinpath(secure_filename(file.filename)))
        filename = nonrepeat_filename(filename,
                                      primary_suffix=datetime.now().isoformat()[:10])
        file.save(filename)

        return jsonify({
            'filename': filename
        }), 201

    return Response(status=304)


@app.route('/api/images/rename', methods=['POST'])
def rename_image():
    global filename

    if filename is not None:
        new_filename = Path(request.get_json()['filename']).with_suffix(Path(filename).suffix)
        new_filename.parent.mkdir(parents=True, exist_ok=True)

        new_filename = new_filename.with_name(secure_filename(new_filename.name))
        new_filename = nonrepeat_filename(str(new_filename))

        shutil.move(filename, new_filename)
        filename = new_filename

        return jsonify({
            'filename': filename
        }), 201

    return Response(status=304)
