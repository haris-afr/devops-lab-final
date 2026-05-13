from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

courses = [
    {"id": 1, "title": "DevOps Engineering", "instructor": "Memoona Amjad"},
    {"id": 2, "title": "Software Design", "instructor": "Adnan Shah"},  
]
next_id = 3

#done
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

#done
@app.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify(courses), 200

#done
@app.route('/api/courses/<int:cid>', methods=['GET'])
def get_course(cid):
    course = next((c for c in courses if c['id'] == cid), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    return jsonify(courses), 200

#TODO
@app.route('/api/courses', methods=['POST'])
def post_course():
    pass

#TODO
@app.route('/api/courses/<int:cid>', methods=['PUT'])
def update_course(cid):
    course = next((c for c in courses if c['id'] == cid), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    return jsonify(courses), 200

#TODO 
@app.route('/api/courses/<int:cid>', methods=['DELETE'])
def delete_course(cid):
    course = next((c for c in courses if c['id'] == cid), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    courses.remove(cid)
    return jsonify(courses), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)