const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 5000;  // Thay đổi port thành 5000

app.use(cors());
app.use(bodyParser.json());

let latestData = null;

app.post('/api/predict', (req, res) => {
  const formData = req.body;
  console.log('Đã nhận dữ liệu:', formData);
  latestData = formData;  // Lưu dữ liệu mới nhất
  res.json({
    message: 'Đã nhận dữ liệu thành công',
    data: formData,
    prediction: 'Dự đoán mẫu dựa trên dữ liệu'
  });
});

// Thêm endpoint mới để lấy dữ liệu mới nhất
app.get('/api/latest', (req, res) => {
  if (latestData) {
    res.json(latestData);
  } else {
    res.status(404).json({ message: 'Chưa có dữ liệu' });
  }
});

app.listen(port, () => {
  console.log(`API server running on port ${port}`);
});