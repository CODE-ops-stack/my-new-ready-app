# 🌐 Tayaari Pakki — Cloud Headless Question Bank & CDN

Welcome to the centralized, high-performance cloud question bank for **Tayaari Pakki**. This repository serves as the single source of truth for both the **Android Mobile App** and future **Web Applications / Desktop Mock Test Portals**.

---

## 📡 Live Production Endpoints

### 1. Primary High-Speed Worldwide CDN (jsDelivr Edge Cache)
* **All Questions (JSON):**  
  `https://cdn.jsdelivr.net/gh/CODE-ops-stack/my-new-ready-app@main/questions.json`
* **Metadata & Versioning:**  
  `https://cdn.jsdelivr.net/gh/CODE-ops-stack/my-new-ready-app@main/metadata.json`
* **Map & Diagram Assets (Base URL):**  
  `https://cdn.jsdelivr.net/gh/CODE-ops-stack/my-new-ready-app@main/images/{image_name}.png`

### 2. Secondary Direct Raw GitHub Endpoint (Instant Fallback)
* **All Questions (JSON):**  
  `https://raw.githubusercontent.com/CODE-ops-stack/my-new-ready-app/main/questions.json`
* **Metadata & Versioning:**  
  `https://raw.githubusercontent.com/CODE-ops-stack/my-new-ready-app/main/metadata.json`

---

## 💻 How to Consume in a Web Application (Next.js / React / Vanilla JS)

Because this repository is public, **CORS is enabled worldwide**. Any website can fetch data without an API key or backend proxy:

```javascript
// Example: Fetching 2,821 MCQs with full trap dissections in React/Next.js
async function loadQuestionBank() {
  const url = "https://cdn.jsdelivr.net/gh/CODE-ops-stack/my-new-ready-app@main/questions.json";
  try {
    const res = await fetch(url);
    const questions = await res.json();
    console.log(`Loaded ${questions.length} questions from cloud!`);
    return questions;
  } catch (error) {
    console.error("Cloud fetch failed, using fallback:", error);
  }
}
```

---

## 📱 How the Android App Consumes this Cloud Feed

The Android application uses `CloudQuestionSyncService.kt` with OkHttp:
1. On app startup, checks `metadata.json` for the remote version.
2. If a newer question version exists or local database is empty, streams the JSON directly into the Room SQLite database.
3. Completely decouples the mobile APK size from the question bank size.

---

## 📊 Dataset Statistics
* **Total Questions:** 2,821
* **Metacognitive Trap Dissection Coverage:** 100%
* **Syllabus Chapters:** 23 Standard Physical, Human, and Indian Geography Modules
* **Map & Spatial Diagrams:** 77 Vector & Raster Assets hosted in `/images`
