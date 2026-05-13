from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route('/api/courses', methods=['POST'])
def post_course():
    data = request.get_json()
    if data['title'] == None or data['instructor'] == None:
        return 400
    data['id': next_id]
    next_id += 1
    courses.insert(data)
    return jsonify(courses), 200


@app.route('/api/courses/<int:cid>', methods=['PUT'])
def update_course(cid):
    course = next((c for c in courses if c['id'] == cid), None)
    if not course:
        return jsonify({'error': 'course not found'}), 404
    data = request.get_json()
    course.update(data)
    return jsonify(courses), 200


#done
@app.route('/api/courses/<int:cid>', methods=['DELETE'])
def delete_course(cid):
    global courses
    original_len = len(courses)
    courses = [c for c in courses if c['id'] != cid]
    if len(courses) == original_len:
        return jsonify({'error': 'course not found'}), 404
    return jsonify({'message': 'course deleted'}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)