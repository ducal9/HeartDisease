from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Giả sử bạn có dữ liệu về thời tiết với các yếu tố như nhiệt độ, độ ẩm, gió
data = {
    'temperature': [25, 28, 30, 22, 24, 27, 29, 31, 33, 26],
    'humidity': [80, 60, 85, 78, 79, 55, 60, 63, 82, 75],
    'wind_speed': [10, 12, 8, 5, 7, 6, 9, 15, 14, 11],
    'rain': [1, 0, 1, 0, 1, 0, 0, 1, 1, 0]  # 1: Mưa, 0: Không mưa
}

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data)

# X và y
X = df[['temperature', 'humidity', 'wind_speed']]  # Các yếu tố đầu vào
y = df['rain']  # Kết quả (mưa hay không)

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Khởi tạo và huấn luyện mô hình cây quyết định
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Dự đoán kết quả
y_pred = clf.predict(X_test)

print(f"Dự đoán mưa hay không: {y_pred}")
