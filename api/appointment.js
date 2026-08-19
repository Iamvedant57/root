const { saveAppointment } = require('../lib/db');
const { sendOwnerWhatsAppNotification } = require('../lib/whatsapp');

// Simple in-memory rate limiter to prevent spam
const rateLimitMap = new Map();
const RATE_LIMIT_WINDOW_MS = 60 * 1000; // 1 minute
const MAX_REQUESTS_PER_WINDOW = 5;

function isRateLimited(ip) {
  const now = Date.now();
  const record = rateLimitMap.get(ip);
  if (!record) {
    rateLimitMap.set(ip, { count: 1, resetAt: now + RATE_LIMIT_WINDOW_MS });
    return false;
  }
  if (now > record.resetAt) {
    rateLimitMap.set(ip, { count: 1, resetAt: now + RATE_LIMIT_WINDOW_MS });
    return false;
  }
  record.count += 1;
  return record.count > MAX_REQUESTS_PER_WINDOW;
}

module.exports = async function handler(req, res) {
  // CORS & Security headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method not allowed. Use POST.' });
  }

  // Anti-spam check
  const clientIp = req.headers['x-forwarded-for'] || req.socket?.remoteAddress || '127.0.0.1';
  if (isRateLimited(clientIp)) {
    return res.status(429).json({
      success: false,
      error: 'Too many requests. Please wait a moment before booking again.'
    });
  }

  try {
    let body = req.body;
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    body = body || {};

    const { customer_name, customer_phone, service, appointment_date, appointment_time } = body;

    // Server-side validation
    const errors = [];

    if (!customer_name || !customer_name.trim() || customer_name.trim().length < 2) {
      errors.push('Please enter a valid full name (minimum 2 characters).');
    }

    const cleanPhone = (customer_phone || '').replace(/\D/g, '');
    if (!cleanPhone || cleanPhone.length < 10) {
      errors.push('Please enter a valid 10-digit phone number.');
    }

    if (!service || !service.trim()) {
      errors.push('Please select a service.');
    }

    if (!appointment_date) {
      errors.push('Please select an appointment date.');
    } else {
      const selectedDate = new Date(appointment_date);
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      if (isNaN(selectedDate.getTime()) || selectedDate < today) {
        errors.push('Appointment date cannot be in the past.');
      }
    }

    if (!appointment_time || !appointment_time.trim()) {
      errors.push('Please select an appointment time.');
    }

    if (errors.length > 0) {
      return res.status(400).json({ success: false, errors, error: errors[0] });
    }

    // Prepare appointment data
    const appointmentId = `apt_${Date.now()}_${Math.random().toString(36).substr(2, 6)}`;
    const appointmentData = {
      appointment_id: appointmentId,
      customer_name: customer_name.trim(),
      customer_phone: cleanPhone,
      service: service.trim(),
      appointment_date,
      appointment_time: appointment_time.trim(),
      status: 'pending'
    };

    // Save to Database
    const dbResult = await saveAppointment(appointmentData);

    // Automatically trigger WhatsApp notification to salon owner
    const whatsappResult = await sendOwnerWhatsAppNotification(appointmentData);

    return res.status(200).json({
      success: true,
      message: 'Appointment request received successfully',
      appointment_id: appointmentId,
      status: 'pending',
      whatsapp_notified: whatsappResult.success
    });

  } catch (err) {
    console.error('[API] Appointment processing error:', err);
    return res.status(500).json({
      success: false,
      error: 'Something went wrong while processing your request. Please try again or contact the salon directly.'
    });
  }
};
