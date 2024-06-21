<h1>Báo cáo bổ sung DA1 - chương 4: Mô phỏng lập trình lượng tử</h1>
<div>Chủ đề: Mô hình hóa hệ thống lượng tử</div>

<h2>1. Thành viên và nhiệm vụ</h2>
<ul>
  <li>Nguyễn Thường Quân - 21522498: Thực hiện Backend</li>
  <li>Nguyễn Vũ Anh Minh - 21520350: Thực hiện Frontend</li>
</ul>

<h2>2. Về các thư mục</h2>
<ul>
  <li>File source "simulator.py" là file code gốc, sử dụng testcase là các file có sẵn trong thư mục "testcase". In ra kết quả trong thư mục "result"</li>
  <li>Các testcase được tự động tạo lập bằng file "testcase_generate.py"</li>
  <li>Các thư mục còn lại thuộc về lập trinh website</li>
  
</ul>

<h2>3. Cấu trúc hệ thống website (thư mục frontend)</h2>
<ul>
  <li>File "app.py" là backend simulator, sử dụng server flask để gửi đến frontend</li>
  <li>Các thư mục "about us", "guilde", "main"... chứa các file frontend và backend của chúng.</li>
</ul>

<h2>4. Lưu ý khi tải về chạy thử</h2>
<ul>
  <li>Do hiện tại đồ án chỉ chạy dưới dạng code chưa deloy web nên cần download từ Frontend về!!!</li>
  <li>Trước khi chạy cần đưa các file html, css, js từ các folder nhỏ bên trong Frontend vào chung 1 folder</li>
  <li>Lưu ý chạy file app.py trước để connect server Flask, sau đó có thể mở các file html để thử nghiệm</li>
</ul>
