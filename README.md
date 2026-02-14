# 🔊 Acoustic Machine Health Monitor

A predictive maintenance tool that "listens" to industrial motors. By analyzing frequency patterns, it identifies abnormal vibrations and sound signatures indicative of mechanical wear.

## 🚀 Features
- **Frequency Analysis:** Performs Fast Fourier Transform (FFT) on the edge.
- **Anomaly Detection:** Flags high-frequency "screeching" or low-frequency "thumping."
- **Dual-Core Processing:** Core 0 handles audio sampling; Core 1 handles data transmission.
- **Predictive Alerts:** Predicts bearing life based on noise floor increases.

## ⚙️ Engineering Logic
- **Hardware:** Raspberry Pi Pico samples a high-sensitivity microphone module via ADC.
- **Software:** Python visualizes the sound spectrum and calculates the "Health Score" based on deviation from the baseline noise.
