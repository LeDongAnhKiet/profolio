# Portfolio Website

## Triển khai trên Render
1. Push code lên GitHub.
2. Vào [Render](https://render.com/).
3. Chọn "New Web Service".
4. Kết nối GitHub và chọn repository.
5. Cấu hình:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Python Version:** 3.9+
6. Nhấn "Deploy" và chờ hoàn tất.
