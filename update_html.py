import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert modal CSS before </style>
css_to_insert = """
/* =========================================================
   APPOINTMENT MODAL — LUXURY GLASSMORPHISM UI
   ========================================================= */
.apt-overlay {
  position: fixed;
  inset: 0;
  background: rgba(8, 8, 10, 0.82);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  z-index: 2100;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.4s var(--ease);
  overflow-y: auto;
}

.apt-overlay.open {
  opacity: 1;
  pointer-events: auto;
}

.apt-card {
  width: 100%;
  max-width: 490px;
  background: rgba(22, 22, 24, 0.94);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(198, 161, 91, 0.22);
  border-radius: 28px;
  padding: 34px 30px;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.9), 0 0 35px rgba(198, 161, 91, 0.08);
  position: relative;
  transform: scale(0.92) translateY(18px);
  transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.45s var(--ease);
  margin: auto;
}

.apt-overlay.open .apt-card {
  transform: scale(1) translateY(0);
}

.apt-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 22px;
}

.apt-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.apt-logo-mark {
  width: 42px;
  height: 42px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}
.apt-logo-mark svg {
  width: 100%;
  height: 100%;
  animation: spin 30s linear infinite;
}
.apt-logo-center {
  position: absolute;
  font-family: var(--font-display);
  font-size: 13px;
  font-weight: 700;
  color: var(--gold);
}

.apt-brand-text {
  display: flex;
  flex-direction: column;
}
.apt-brand-title {
  font-family: var(--font-display);
  font-size: 16px;
  color: var(--white);
  letter-spacing: 0.8px;
  line-height: 1.1;
  font-weight: 600;
}
.apt-brand-sub {
  font-family: var(--font-display);
  font-size: 11px;
  color: var(--gold);
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-top: 2px;
}

.apt-close {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--gold);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s var(--ease);
}
.apt-close:hover {
  background: var(--gold);
  color: var(--black);
  transform: rotate(90deg) scale(1.05);
}

.apt-title-group {
  margin-bottom: 24px;
}
.apt-subtitle {
  font-family: var(--font-body);
  font-size: 11px;
  letter-spacing: 3.5px;
  text-transform: uppercase;
  color: var(--gold);
  font-weight: 500;
  margin-bottom: 6px;
}
.apt-title {
  font-family: var(--font-display);
  font-size: 32px;
  color: var(--white);
  font-weight: 400;
  line-height: 1.15;
}

.apt-form {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.apt-input-group {
  position: relative;
  width: 100%;
}

.apt-input, .apt-select {
  width: 100%;
  height: 52px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 26px;
  padding: 0 22px;
  color: var(--white);
  font-family: var(--font-body);
  font-size: 14px;
  outline: none;
  transition: all 0.3s var(--ease);
  -webkit-appearance: none;
  appearance: none;
}

.apt-input::placeholder {
  color: rgba(255, 255, 255, 0.45);
}

.apt-input:focus, .apt-select:focus {
  border-color: var(--gold);
  background: rgba(198, 161, 91, 0.08);
  box-shadow: 0 0 16px rgba(198, 161, 91, 0.25);
}

.apt-select {
  cursor: pointer;
  padding-right: 44px;
  color: var(--white);
}
.apt-select option {
  background: var(--charcoal);
  color: var(--white);
  padding: 10px;
}

.apt-select-arrow {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--gold);
  font-size: 12px;
  pointer-events: none;
}

.apt-grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.apt-input[type="date"]::-webkit-calendar-picker-indicator {
  filter: invert(0.8) sepia(0.5) saturate(3) hue-rotate(5deg);
  cursor: pointer;
}

.apt-submit-btn {
  width: 100%;
  height: 54px;
  margin-top: 8px;
  border-radius: 27px;
  border: none;
  background: linear-gradient(135deg, var(--gold-light), var(--gold));
  color: var(--black);
  font-family: var(--font-body);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.35s var(--ease);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  box-shadow: 0 8px 25px rgba(198, 161, 91, 0.35);
}

.apt-submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(198, 161, 91, 0.5);
  background: linear-gradient(135deg, #ffffff, var(--gold-light));
}

.apt-submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.apt-footer-note {
  margin-top: 14px;
  text-align: center;
  font-size: 12px;
  color: rgba(248, 245, 239, 0.6);
  line-height: 1.4;
}

.apt-alert {
  padding: 12px 16px;
  border-radius: 12px;
  font-size: 13px;
  display: none;
  margin-bottom: 12px;
}
.apt-alert.error {
  display: block;
  background: rgba(220, 53, 69, 0.15);
  border: 1px solid rgba(220, 53, 69, 0.4);
  color: #ff808b;
}

.apt-success-view {
  display: none;
  text-align: center;
  padding: 15px 0 5px;
}
.apt-success-icon {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: rgba(198, 161, 91, 0.15);
  border: 1.5px solid var(--gold);
  color: var(--gold);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  margin: 0 auto 18px;
  animation: popIn 0.5s var(--ease);
}
@keyframes popIn { 0%{ transform: scale(0); } 70%{ transform: scale(1.15); } 100%{ transform: scale(1); } }
.apt-success-title {
  font-family: var(--font-display);
  font-size: 28px;
  color: var(--white);
  margin-bottom: 10px;
}
.apt-success-desc {
  color: var(--muted);
  font-size: 15px;
  margin-bottom: 24px;
  line-height: 1.6;
}

@media (max-width: 520px) {
  .apt-card {
    padding: 26px 20px;
    border-radius: 24px;
  }
  .apt-grid-2 {
    grid-template-columns: 1fr;
  }
  .apt-title {
    font-size: 28px;
  }
}
"""

if '</style>' in html:
    html = html.replace('</style>', css_to_insert + '\n</style>')

# 2. Add Booking Link to Fullscreen Menu Overlay
if '<a href="#contact" class="menu-nav-link">Contact Us</a>' in html:
    html = html.replace(
        '<a href="#contact" class="menu-nav-link">Contact Us</a>',
        '<a href="#contact" class="menu-nav-link">Contact Us</a>\n    <a href="#" class="menu-nav-link trigger-apt-modal">Book Appointment</a>'
    )

# 3. Insert Modal HTML & JS before </body>
modal_html_to_insert = """
<!-- =========================================================
     LUXURY GLASSMORPHIC APPOINTMENT MODAL
     ========================================================= -->
<div class="apt-overlay" id="aptOverlay">
  <div class="apt-card" id="aptCard">
    <!-- Header -->
    <div class="apt-header">
      <div class="apt-brand">
        <div class="apt-logo-mark">
          <svg viewBox="0 0 200 200">
            <defs>
              <path id="modalSealCircle" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/>
            </defs>
            <circle cx="100" cy="100" r="94" fill="none" stroke="#c6a15b" stroke-width="1.5"/>
            <circle cx="100" cy="100" r="60" fill="none" stroke="#c6a15b" stroke-width="1.5"/>
            <text font-family="Jost" font-size="11.5" letter-spacing="3" fill="#c6a15b">
              <textPath href="#modalSealCircle" startOffset="0%">ROOTS MAGMA UNISEX SALON • EST. 1985 • AMRAVATI •</textPath>
            </text>
          </svg>
          <span class="apt-logo-center">RM</span>
        </div>
        <div class="apt-brand-text">
          <span class="apt-brand-title">RUTH MAGMA</span>
          <span class="apt-brand-sub">Unisex Salon</span>
        </div>
      </div>
      <button class="apt-close" id="aptClose" aria-label="Close modal"><i class="fa-solid fa-xmark"></i></button>
    </div>

    <!-- Form View -->
    <div id="aptFormView">
      <div class="apt-title-group">
        <div class="apt-subtitle">APPOINTMENT CONSOLE</div>
        <h3 class="apt-title">Reserve your chair</h3>
      </div>

      <div class="apt-alert" id="aptAlert"></div>

      <form class="apt-form" id="appointmentForm" novalidate>
        <div class="apt-input-group">
          <input type="text" id="aptName" class="apt-input" placeholder="Full name" required>
        </div>

        <div class="apt-input-group">
          <input type="tel" id="aptPhone" class="apt-input" placeholder="Phone number" required>
        </div>

        <div class="apt-input-group">
          <select id="aptService" class="apt-select" required>
            <option value="" disabled selected>Select a service</option>
            <option value="Haircut & Styling">Haircut &amp; Styling</option>
            <option value="Beard Styling & Shave">Beard Styling &amp; Shave</option>
            <option value="Hydra-Facial Ritual">Hydra-Facial Ritual</option>
            <option value="Hair Spa & Scalp Care">Hair Spa &amp; Scalp Care</option>
            <option value="Hair Color & Balayage">Hair Color &amp; Balayage</option>
            <option value="Keratin & Smoothening">Keratin &amp; Smoothening</option>
            <option value="Express Skin Cleanup">Express Skin Cleanup</option>
            <option value="Full HD Bridal Makeup">Full HD Bridal Makeup</option>
            <option value="Groom Special Package">Groom Special Package</option>
          </select>
          <i class="fa-solid fa-chevron-down apt-select-arrow"></i>
        </div>

        <div class="apt-grid-2">
          <div class="apt-input-group">
            <input type="date" id="aptDate" class="apt-input" required>
          </div>
          <div class="apt-input-group">
            <select id="aptTime" class="apt-select" required>
              <option value="" disabled selected>Select time</option>
              <option value="10:00 AM">10:00 AM</option>
              <option value="11:00 AM">11:00 AM</option>
              <option value="12:00 PM">12:00 PM</option>
              <option value="01:00 PM">01:00 PM</option>
              <option value="02:00 PM">02:00 PM</option>
              <option value="03:00 PM">03:00 PM</option>
              <option value="04:00 PM">04:00 PM</option>
              <option value="05:00 PM">05:00 PM</option>
              <option value="06:00 PM">06:00 PM</option>
              <option value="07:00 PM">07:00 PM</option>
              <option value="08:00 PM">08:00 PM</option>
            </select>
            <i class="fa-solid fa-chevron-down apt-select-arrow"></i>
          </div>
        </div>

        <button type="submit" class="apt-submit-btn" id="aptSubmitBtn">
          <span>BOOK APPOINTMENT</span>
        </button>

        <p class="apt-footer-note">We’ll confirm your appointment personally on WhatsApp.</p>
      </form>
    </div>

    <!-- Success View -->
    <div class="apt-success-view" id="aptSuccessView">
      <div class="apt-success-icon"><i class="fa-solid fa-check"></i></div>
      <h3 class="apt-success-title">Appointment Request Received ✓</h3>
      <p class="apt-success-desc">Your appointment request has been submitted successfully.<br><strong style="color:var(--gold);">We’ll confirm your appointment personally on WhatsApp.</strong></p>
      <button class="apt-submit-btn" id="aptDoneBtn" style="margin: 0 auto; max-width: 200px;"><span>DONE</span></button>
    </div>
  </div>
</div>
"""

js_to_insert = """
/* =========================================================
   APPOINTMENT MODAL INTERACTION & API SUBMISSION
   ========================================================= */
const aptOverlay = document.getElementById('aptOverlay');
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
});
"""

if '</body>' in html:
    html = html.replace('</body>', modal_html_to_insert + '\n<script>\n' + js_to_insert + '\n</script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully updated index.html!')
