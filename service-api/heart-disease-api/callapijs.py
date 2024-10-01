import requests

def get_and_print_data():
    """Lấy dữ liệu từ API và in ra terminal với mỗi giá trị trên một dòng"""
    url = 'http://localhost:5000/api/latest'  # Thay đổi URL nếu cần
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra lỗi
        data = response.json()
        
        # In từng trường trong dữ liệu ra từng dòng
        for key, value in data.items():
            print(f"{key}: {value}")
            
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi lấy dữ liệu: {e}")

if __name__ == "__main__":
    get_and_print_data()
