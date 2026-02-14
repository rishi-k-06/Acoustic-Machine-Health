// For Raspberry Pi Pico using Arduino Mbed Core
#include "arduinoFFT.h"

#define SAMPLES 128
#define SAMPLING_FREQ 40000 

arduinoFFT FFT = arduinoFFT();
unsigned int sampling_period_us;
double vReal[SAMPLES];
double vImag[SAMPLES];

void setup() {
  Serial.begin(115200);
  sampling_period_us = round(1000000 * (1.0 / SAMPLING_FREQ));
}

void loop() {
  // Sample audio on Core 0
  for (int i = 0; i < SAMPLES; i++) {
    unsigned long microsec = micros();
    vReal[i] = analogRead(26); // ADC0 on Pico
    vImag[i] = 0;
    while (micros() < (microsec + sampling_period_us));
  }

  FFT.Windowing(vReal, SAMPLES, FFT_WIN_TYP_HAMMING, FFT_FORWARD);
  FFT.Compute(vReal, vImag, SAMPLES, FFT_FORWARD);
  FFT.ComplexToMagnitude(vReal, vImag, SAMPLES);

  // Send peak magnitude to Python
  double peak = FFT.MajorPeak(vReal, SAMPLES, SAMPLING_FREQ);
  Serial.println(peak);
  delay(500);
}
