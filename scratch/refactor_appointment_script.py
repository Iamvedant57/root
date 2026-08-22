import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove demo elements added at the end (lines 1711 to 1845)
if '<button id="openBookingBtn"' in html:
    idx = html.find('<!-- 1. The Booking Button -->')
    if idx != -1:
        html = html[:idx] + '</body>\n</html>'

# 2. Update the Ruth Magma Appointment Modal Script logic
old_script = """const aptOverlay = document.getElementById('aptOverlay');
const aptClose = document.getElementById('aptClose');
const appointmentForm = document.getElementById('appointmentForm');
const aptFormView = document.getElementById('aptFormView');
const aptSuccessView = document.getElementById('aptSuccessView');
const aptAlert = document.getElementById('aptAlert');
const aptSubmitBtn = document.getElementById('aptSubmitBtn');
const aptDate = document.getElementById('aptDate');

if (aptDate) {
  const todayIso = new Date().toISOString().split('T')[0];
  aptDate.min = todayIso;
}

function openAppointmentModal(defaultService) {
  if (defaultService) {
    const select = document.getElementById('aptService');
    if (select) {
      for (let opt of select.options) {
        if (opt.value.toLowerCase().includes(defaultService.toLowerCase())) {
          opt.selected = true;
          break;
        }
      }
    }
  }
  aptFormView.style.display = 'block';
  aptSuccessView.style.display = 'none';
  aptAlert.style.display = 'none';
  aptAlert.className = 'apt-alert';
  aptOverlay.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeAppointmentModal() {
  aptOverlay.classList.remove('open');
  document.body.style.overflow = '';
}

aptClose?.addEventListener('click', closeAppointmentModal);
aptOverlay?.addEventListener('click', (e) => {
  if (e.target === aptOverlay) closeAppointmentModal();
});
document.getElementById('aptDoneBtn')?.addEventListener('click', closeAppointmentModal);

// Wire triggers across the website to open modal
document.querySelectorAll('.trigger-apt-modal, .btn-solid, .hero-actions a').forEach(el => {
  if (el.innerText.toLowerCase().includes('visit') || el.innerText.toLowerCase().includes('book') || el.classList.contains('btn-solid')) {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      openAppointmentModal();
    });
  }
});

// Form Submission
appointmentForm?.addEventListener('submit', async function(e) {
  e.preventDefault();
  
  const name = document.getElementById('aptName').value.trim();
  const phone = document.getElementById('aptPhone').value.trim();
  const service = document.getElementById('aptService').value;
  const date = document.getElementById('aptDate').value;
  const time = document.getElementById('aptTime').value;

  let errorMsg = '';
  if (!name || name.length < 2) {
    errorMsg = 'Please enter your full name.';
  } else if (!phone || phone.replace(/\\D/g, '').length < 10) {
    errorMsg = 'Please enter a valid 10-digit phone number.';
  } else if (!service) {
    errorMsg = 'Please select a service.';
  } else if (!date) {
    errorMsg = 'Please select an appointment date.';
  } else if (!time) {
    errorMsg = 'Please select an appointment time.';
  }

  if (errorMsg) {
    aptAlert.textContent = errorMsg;
    aptAlert.className = 'apt-alert error';
    return;
  }

  aptAlert.style.display = 'none';
  aptSubmitBtn.disabled = true;
  aptSubmitBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> <span>PROCESSING...</span>';

  try {
    const response = await fetch('/api/appointment', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        customer_name: name,
        customer_phone: phone,
        service: service,
        appointment_date: date,
        appointment_time: time
      })
    });

    const data = await response.json();

    if (response.ok && data.success) {
      aptFormView.style.display = 'none';
      aptSuccessView.style.display = 'block';
      appointmentForm.reset();
    } else {
      aptAlert.textContent = data.error || 'Something went wrong. Please try again or contact the salon directly.';
      aptAlert.className = 'apt-alert error';
    }
  } catch (err) {
    console.error('Appointment API Submission error:', err);
    aptFormView.style.display = 'none';
    aptSuccessView.style.display = 'block';
    appointmentForm.reset();
  } finally {
    aptSubmitBtn.disabled = false;
    aptSubmitBtn.innerHTML = '<span>BOOK APPOINTMENT</span>';
  }
});"""

new_script = """const aptOverlay = document.getElementById('aptOverlay');
const aptClose = document.getElementById('aptClose');
const appointmentForm = document.getElementById('appointmentForm');
const aptFormView = document.getElementById('aptFormView');
const aptSuccessView = document.getElementById('aptSuccessView');
const aptAlert = document.getElementById('aptAlert');
const aptSubmitBtn = document.getElementById('aptSubmitBtn');
const aptDate = document.getElementById('aptDate');

// Dynamic Local Date Restriction (Block Past Dates)
function updateMinAppointmentDate() {
  if (aptDate) {
    const now = new Date();
    const yyyy = now.getFullYear();
    const mm = String(now.getMonth() + 1).padStart(2, '0');
    const dd = String(now.getDate()).padStart(2, '0');
    const todayStr = `${yyyy}-${mm}-${dd}`;
    aptDate.min = todayStr;
  }
}
updateMinAppointmentDate();

function openAppointmentModal(defaultService) {
  updateMinAppointmentDate();
  if (defaultService) {
    const select = document.getElementById('aptService');
    if (select) {
      for (let opt of select.options) {
        if (opt.value.toLowerCase().includes(defaultService.toLowerCase())) {
          opt.selected = true;
          break;
        }
      }
    }
  }
  aptFormView.style.display = 'block';
  aptSuccessView.style.display = 'none';
  aptAlert.style.display = 'none';
  aptAlert.className = 'apt-alert';
  aptOverlay.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeAppointmentModal() {
  aptOverlay.classList.remove('open');
  document.body.style.overflow = '';
}

aptClose?.addEventListener('click', closeAppointmentModal);
aptOverlay?.addEventListener('click', (e) => {
  if (e.target === aptOverlay) closeAppointmentModal();
});
document.getElementById('aptDoneBtn')?.addEventListener('click', closeAppointmentModal);

// Attach event listener strictly to existing appointment buttons on the website
document.querySelectorAll('.trigger-apt-modal, .btn-solid, .hero-actions a, .whatsapp-float').forEach(el => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    openAppointmentModal();
  });
});

// Form Submission & WhatsApp Integration
appointmentForm?.addEventListener('submit', async function(e) {
  e.preventDefault();
  
  const name = document.getElementById('aptName').value.trim();
  const phone = document.getElementById('aptPhone').value.trim();
  const service = document.getElementById('aptService').value;
  const date = document.getElementById('aptDate').value;
  const time = document.getElementById('aptTime').value;

  // Validate inputs
  let errorMsg = '';

  // Validate Date (Programmatically block past dates)
  const selectedDate = new Date(date + 'T00:00:00');
  const todayMidnight = new Date();
  todayMidnight.setHours(0, 0, 0, 0);

  if (!name || name.length < 2) {
    errorMsg = 'Please enter your full name.';
  } else if (!phone || phone.replace(/\\D/g, '').length < 10) {
    errorMsg = 'Please enter a valid 10-digit phone number.';
  } else if (!service) {
    errorMsg = 'Please select a service.';
  } else if (!date || isNaN(selectedDate.getTime()) || selectedDate < todayMidnight) {
    errorMsg = 'Appointment date cannot be in the past.';
  } else if (!time) {
    errorMsg = 'Please select an appointment time.';
  }

  if (errorMsg) {
    aptAlert.textContent = errorMsg;
    aptAlert.className = 'apt-alert error';
    return;
  }

  aptAlert.style.display = 'none';
  aptSubmitBtn.disabled = true;
  aptSubmitBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> <span>PROCESSING...</span>';

  // Format WhatsApp message for owner (+91 93094 19028)
  const ownerNumber = '919309419028';
  const whatsappMsg = 
`✨ *NEW APPOINTMENT BOOKING*

*Salon:* Ruth Magma Unisex Salon
*Customer Name:* ${name}
*Phone Number:* ${phone}
*Selected Service:* ${service}
*Appointment Date:* ${date}
*Appointment Time:* ${time}

Please confirm my appointment.`;

  const waUrl = `https://wa.me/${ownerNumber}?text=${encodeURIComponent(whatsappMsg)}`;

  // Open WhatsApp in new tab for customer to send pre-filled message
  window.open(waUrl, '_blank');

  // Save to database & API in background
  try {
    await fetch('/api/appointment', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        customer_name: name,
        customer_phone: phone,
        service: service,
        appointment_date: date,
        appointment_time: time
      })
    });
  } catch (err) {
    console.warn('Background DB sync warning:', err);
  } finally {
    aptFormView.style.display = 'none';
    aptSuccessView.style.display = 'block';
    appointmentForm.reset();
    aptSubmitBtn.disabled = false;
    aptSubmitBtn.innerHTML = '<span>BOOK APPOINTMENT</span>';
  }
});"""

if old_script in html:
    html = html.replace(old_script, new_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully cleaned up index.html script and re-used Ruth Magma modal!')
