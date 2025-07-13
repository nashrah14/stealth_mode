# 📄 Report: Player Re-Identification in Single Video Feed

### 👤 Author: Nashrah Fathima
### 📅 Date: July 2025

---

## 🔍 Objective
To build a real-time system that can:
- Detect football players in a 15-second video.
- Assign and maintain unique IDs per player.
- Re-identify players if they leave and re-enter the frame.

---

## 🧠 Approach
- **Detection:** Used the provided YOLOv11 model fine-tuned for football players.
- **Tracking & Re-ID:** Used Deep SORT for associating and tracking players over frames.
  - Appearance descriptors + motion tracking
  - `max_age=30` ensures short absences don't reset IDs

---

## 🧪 Techniques & Tools
| Component     | Tool Used         |
|---------------|-------------------|
| Detection     | YOLOv11 (Ultralytics) |
| Tracking      | Deep SORT Realtime |
| Video I/O     | OpenCV             |
| Language      | Python 3.11        |

---

## ⚙️ Pipeline Summary
1. Load YOLOv11 model and Deep SORT tracker.
2. Read video frame-by-frame.
3. Detect player bounding boxes.
4. Feed detections into tracker.
5. Draw bounding boxes and IDs.
6. Save output to a new video.

---

## 📌 Key Insights
- Re-ID performance depends on appearance consistency (clothes, size, etc.).
- Players staying out of frame for long can break ID tracking — `max_age` tuning helps.
- Deep SORT provides robust re-identification without heavy embedding models.

---
## ⚠️ Download the Model

Due to GitHub file size limits, the model is not included in this repo.

📦 [Download best.pt](https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view)

---

## ❗ Challenges
- Couldn’t download model initially — used YOLOv8 placeholder.
- Had to assume class 0 = player in absence of label map.
- Limited video duration made it tricky to validate long-term ID consistency.

---


## ✅ Outcome
- Successfully tracked players across 15-second footage.
- Maintained consistent IDs even after temporary exits.
- Delivered real-time performance with saved video output.

---

## 🔚 Conclusion
This task showcases my ability to apply object detection and tracking in real-time scenarios. The solution is modular and scalable, and with a richer dataset and longer footage, could extend to full-match player analytics.

---

## 📎 Next Steps (Optional Improvements)
- Track ball (if class available in model).
- Add goal/event timestamps in overlay.
- Enhance player trajectory visualizations.

---

Thank you for the opportunity to demonstrate my skills.
