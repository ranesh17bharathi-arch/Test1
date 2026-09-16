<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a single-bit 1-bit **Full Adder** circuit digital logic design. It takes three 1-bit binary inputs—operand `A`, operand `B`, and an incoming carry bit `Cin`—and calculates their 2-bit binary sum:

* **Sum output (`S`)**: Calculated using three-input XOR logic:
  `Sum = A ^ B ^ Cin`
* **Carry-out (`Cout`)**: Calculated using majority logic:
  `Cout = (A & B) | (B & Cin) | (A & Cin)` 

## How to test

1. Toggle the input pins using the DIP switches on the Tiny Tapeout demo board:
   * **`ui_in[0]`**: Input bit `A`
   * **`ui_in[1]`**: Input bit `B`
   * **`ui_in[2]`**: Input bit `Cin`
2. Observe the output LEDs on the board to verify the results:
   * **`uo_out[0]`**: `Sum` bit
   * **`uo_out[1]`**: `Cout` bit
3. Test combinations (e.g., set `ui_in[0]` and `ui_in[1]` to High (1): `uo_out[0]` (Sum) will turn OFF (0) and `uo_out[1]` (Cout) will turn ON (1), representing binary `10` / decimal `2`).

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any
