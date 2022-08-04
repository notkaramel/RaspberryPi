> Most wiring is identical to 3-digit 7-segment 5631BH, with an additional 6th pin for the fourth digit. 
## Transistors: NPN
### C1815 (E-C-B type)
- Use with the segmented display.
- Wire as follows:
  - E: GND
  - C: segment anode (green wire)
  - B: GPIO pin/wire (GPIO colorful)

### 2222A (E-B-C type)
- Use to separate the digits on the segmented display.
- Also because there was a shortage of transistors :D
- Wire as follows:
  - E: Segment cathode (white wire)
  - B: GPIO pin/wire (GPIO colorful)
  - C: Vcc (3V3) (brown wire)

## Segmented display
### 7 segments:
- A (RED) 	: 11 -> GPIO14
- B (ORANGE) 	: 7  -> GPIO15
- C (YELLOW) 	: 4  -> GPIO18
- D (BLUE) 	: 1  -> GPIO23
- E (GREEN) 	: 2  -> GPIO24
- F (PURPLE) 	: 10 -> GPIO25
- G (GRAY) 	: 5  -> GPIO8
- DP (BROWN) 	: 3  -> GPIO7

### 3 digits: (all white wires)
- D1 (RED)	: 12 -> GPIO17
- D2 (ORANGE)	: 9 -> GPIO10
- D3 (BLUE)	: 8 -> GPIO5
- D4 (PURPLE)	: 6 -> GPIO26 


