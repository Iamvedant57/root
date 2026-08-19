const express = require('express');
const cors = require('cors');
const path = require('path');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static frontend files
app.use(express.static(path.join(__dirname)));

// Route serverless API function
const appointmentHandler = require('./api/appointment');
app.post('/api/appointment', (req, res) => {
  appointmentHandler(req, res);
});

// Admin endpoint to view appointments
const { getAppointments } = require('./lib/db');
app.get('/api/appointments', async (req, res) => {
  const list = await getAppointments();
  res.json({ success: true, count: list.length, appointments: list });
});

app.listen(PORT, () => {
  console.log(`✨ Roots Magma Salon Server running at http://localhost:${PORT}`);
  console.log(`📅 Appointment API endpoint ready at http://localhost:${PORT}/api/appointment`);
});
