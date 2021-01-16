from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/score', methods=['POST'])
def write_score():
    chno_receive = request.form['chno_give']
    name_receive = request.form['name_give']
    sex_receive = request.form['sex_give']
    age_receive = request.form['age_give']
    re1_receive = request.form['re1_give']
    re2_receive = request.form['re2_give']
    re3_receive = request.form['re3_give']
    re4_receive = request.form['re4_give']
    re5_receive = request.form['re5_give']
    re6_receive = request.form['re6_give']
    re7_receive = request.form['re7_give']
    re8_receive = request.form['re8_give']
    re9_receive = request.form['re9_give']
    re10_receive = request.form['re10_give']
    ret_total_receive = request.form['ret_total_give']

    # DB에 삽입할 review 만들기
    score = {
        'chno': chno_receive,
        'name': name_receive,
        'sex': sex_receive,
        'age': age_receive,
        're1': re1_receive,
        're2': re2_receive,
        're3': re3_receive,
        're4': re4_receive,
        're5': re5_receive,
        're6': re6_receive,
        're7': re7_receive,
        're8': re8_receive,
        're9': re9_receive,
        're10': re10_receive,
        'ret_total': ret_total_receive

    }
    # reviews에 review 저장하기
    db.scores.insert_one(score)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/score', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.scores.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})

#
# @app.route('/api/list', methods=['GET'])
# def show_stars():
#     # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
#     score = list(db.scores.find({}, {'_id': False}))
#     # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
#     # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
#     return jsonify({'result': 'success', 'stars_list': stars})
#
#
#
# @app.route('/api/list', methods=['GET'])
# def show_stars():
#     # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
#     stars = list(db.mystar.find({}, {'_id': False}).sort('like', -1))
#     # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
#     # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
#     return jsonify({'result': 'success', 'stars_list': stars})


#
#
# @app.route('/api/like', methods=['POST'])
# def make_score():
#     # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
#     chno_receive = request.form['chno_receive']
#     name_receive = request.form['name_give']
#     sex_receive = request.form['sex_give']
#     age_receive = request.form['age_give']
#     re1_receive = request.form['re1_give']
#     re2_receive = request.form['re2_give']
#     re3_receive = request.form['re3_give']
#     re4_receive = request.form['re4_give']
#     re5_receive = request.form['re5_give']
#     re6_receive = request.form['re6_give']
#     re7_receive = request.form['re7_give']
#     re8_receive = request.form['re8_give']
#     re9_receive = request.form['re9_give']
#     re10_receive = request.form['re10_give']
#     ret_receive = request.form['ret_give']
#
#     # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
#     star = db.mystar.find_one({'name': name_receive})
#     # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.\
#     new_like = star['like'] + 1
#     # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
#     # 참고: '$set' 활용하기!
#     db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})
#     # 5. 성공하면 success 메시지를 반환합니다.
#     return jsonify({'result': 'success'})
#

# API 역할을 하는 부분



@app.route('/api/delete', methods=['POST'])
def delete_star():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    chno_receive = request.form['chno_give']
    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
    db.scores.delete_one({'chno': chno_receive})
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
