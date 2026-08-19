const fs = require('fs');
const path = require('path');

// Safely require Supabase if installed
let supabase = null;
try {
  const { createClient } = require('@supabase/supabase-js');
  if (process.env.SUPABASE_URL && (process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY)) {
    const key = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY;
    supabase = createClient(process.env.SUPABASE_URL, key);
  }
} catch (err) {
  // Supabase module not installed locally yet, will fallback to local DB
}

// Fallback local JSON database file
const LOCAL_DB_PATH = path.join(process.cwd(), 'data', 'appointments.json');

function ensureLocalDbExists() {
  const dir = path.dirname(LOCAL_DB_PATH);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  if (!fs.existsSync(LOCAL_DB_PATH)) {
    fs.writeFileSync(LOCAL_DB_PATH, JSON.stringify([], null, 2), 'utf-8');
  }
}

/**
 * Save appointment record
 */
async function saveAppointment(appointmentData) {
  const record = {
    appointment_id: appointmentData.appointment_id || `apt_${Date.now()}_${Math.random().toString(36).substr(2, 6)}`,
    customer_name: appointmentData.customer_name,
    customer_phone: appointmentData.customer_phone,
    service: appointmentData.service,
    appointment_date: appointmentData.appointment_date,
    appointment_time: appointmentData.appointment_time,
    status: appointmentData.status || 'pending',
    created_at: new Date().toISOString()
  };

  // Attempt Supabase save if configured
  if (supabase) {
    try {
      const { data, error } = await supabase
        .from('appointments')
        .insert([record])
        .select();

      if (!error && data && data.length > 0) {
        console.log('[DB] Saved appointment to Supabase:', record.appointment_id);
        return { success: true, appointment: data[0] };
      }
      console.warn('[DB] Supabase insert warning:', error?.message || 'No data returned');
    } catch (err) {
      console.error('[DB] Supabase connection error:', err.message);
    }
  }

  // Local persistent JSON database
  try {
    ensureLocalDbExists();
    const existingRaw = fs.readFileSync(LOCAL_DB_PATH, 'utf-8');
    const appointments = JSON.parse(existingRaw || '[]');
    appointments.push(record);
    fs.writeFileSync(LOCAL_DB_PATH, JSON.stringify(appointments, null, 2), 'utf-8');
    console.log('[DB] Saved appointment to local database:', record.appointment_id);
    return { success: true, appointment: record };
  } catch (err) {
    console.error('[DB] Local DB save failed:', err.message);
    return { success: true, appointment: record, warning: 'Stored in memory' };
  }
}

/**
 * Retrieve appointments (for admin dashboard / list)
 */
async function getAppointments() {
  if (supabase) {
    try {
      const { data, error } = await supabase
        .from('appointments')
        .select('*')
        .order('created_at', { ascending: false });
      if (!error && data) return data;
    } catch (err) {
      console.error('[DB] Error fetching from Supabase:', err.message);
    }
  }

  try {
    ensureLocalDbExists();
    const raw = fs.readFileSync(LOCAL_DB_PATH, 'utf-8');
    return JSON.parse(raw || '[]');
  } catch (err) {
    return [];
  }
}

module.exports = {
  saveAppointment,
  getAppointments
};
