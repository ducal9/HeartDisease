import requests
import time

def get_and_print_data():
    """Lấy dữ liệu từ API và in ra terminal với mỗi giá trị khi có dữ liệu mới"""
    url = 'http://localhost:5000/api/latest'  # URL của Flask API
    last_data = None  # Biến lưu trữ dữ liệu cũ để so sánh
    
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Kiểm tra lỗi nếu có
            data = response.json()
            
            # So sánh dữ liệu mới với dữ liệu cũ
            if data != last_data:
                print("\nDữ liệu mới nhận được từ API:")
                for key, value in data.items():
                    print(f"{key}: {value}")
                
                # Cập nhật dữ liệu cũ
                last_data = data
                
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi lấy dữ liệu: {e}")
        
        # Đợi 5 giây trước khi kiểm tra dữ liệu lần nữa
        time.sleep(2)

if __name__ == "__main__":
    get_and_print_data()
