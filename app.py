from flask import Flask, jsonify, request

app = Flask(__name__)

# Đường dẫn chính
@app.route('/')
def home():
    return 'Chào mừng đến với Giai Quyết Việc Làm Từ Xa!'

# API tìm kiếm việc làm
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    # Thêm logic để lấy danh sách việc làm từ cơ sở dữ liệu
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)