#  Player Re-Identification

This project demonstrates real-time player detection and re-identification in a single 15-second football match video. Each player is consistently assigned a unique ID, even if they leave the frame and re-enter later.

---

## 🧩 Objective
- Detect players using a fine-tuned YOLOv11 model.
- Assign unique IDs to players based on their initial appearance.
- Maintain the same IDs for players throughout the video, including when they temporarily leave the frame.

---

## 📁 File Structure
📁 Player-ReID-Assignment/
├── main.py                      
├── requirements.txt             
├── README.md                    
├── report.md                    
├── .gitignore                   
├── 15sec_input_720p.mp4         
└── output_reid.mp4              


---

## 🚀 Setup
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Code
Ensure the model file (e.g., `best.pt`) and input video (`15sec_input_720p.mp4`) are in the same directory as `main.py`.

```bash
python main.py
```

This will display real-time results and generate `output_reid.mp4`.

---

## 🔍 Dependencies
- [Ultralytics YOLOv8/11](https://docs.ultralytics.com/)
- [OpenCV](https://opencv.org/)
- [Deep SORT Realtime](https://pypi.org/project/deep-sort-realtime/)
- NumPy

---

## 📌 Notes
- The current logic assumes class ID `0` corresponds to players.
- Tracking is handled using Deep SORT with appearance-based re-identification.
- This project simulates real-time detection and re-ID frame-by-frame.

---

## 👤 Author
This project was developed as part of the selection process for the AI Internship at Liat.ai (Stealth Mode)
