const https = require('https');

/**
 * Sends automatic WhatsApp notification to the salon owner via Meta WhatsApp Cloud API
 */
async function sendOwnerWhatsAppNotification(appointment) {
  const token = process.env.WHATSAPP_ACCESS_TOKEN;
  const phoneNumberId = process.env.WHATSAPP_PHONE_NUMBER_ID;
  const ownerNumber = (process.env.OWNER_WHATSAPP_NUMBER || '919890640303').replace(/\D/g, '');

  const messageText = 
`🔔 NEW APPOINTMENT

Customer: ${appointment.customer_name}
Phone: ${appointment.customer_phone}

Service: ${appointment.service}

Date: ${appointment.appointment_date}
Time: ${appointment.appointment_time}

Status: Pending

Please contact the customer to confirm the appointment.`;

  // Log message payload on server
  console.log('[WhatsApp] Notification payload prepared for owner:', ownerNumber);

  if (!token || !phoneNumberId) {
    console.warn('[WhatsApp] WHATSAPP_ACCESS_TOKEN or WHATSAPP_PHONE_NUMBER_ID not set in environment. Notification logged on server.');
    return { success: false, reason: 'Missing Meta API credentials in environment' };
  }

  const payload = JSON.stringify({
    messaging_product: 'whatsapp',
    to: ownerNumber,
    type: 'text',
    text: { body: messageText }
  });

  const options = {
    hostname: 'graph.facebook.com',
    path: `/v18.0/${phoneNumberId}/messages`,
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(payload)
    }
  };

  return new Promise((resolve) => {
    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => { data += chunk; });
      res.on('end', () => {
        if (res.statusCode >= 200 && res.statusCode < 300) {
          console.log('[WhatsApp] Automatic notification sent successfully to owner:', data);
          resolve({ success: true, data: JSON.parse(data || '{}') });
        } else {
          console.error('[WhatsApp] Meta API error response:', res.statusCode, data);
          resolve({ success: false, statusCode: res.statusCode, error: data });
        }
      });
    });

    req.on('error', (err) => {
      console.error('[WhatsApp] HTTPS request failed:', err.message);
      resolve({ success: false, error: err.message });
    });

    req.write(payload);
    req.end();
  });
}

module.exports = {
  sendOwnerWhatsAppNotification
};
