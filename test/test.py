# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_full_adder(dut):
    dut._log.info("Starting Full Adder Test")

    # Start clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Apply reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    # Full Adder Truth Table Test Loop
    # Inputs: (A, B, Cin) -> Expected: (Cout, Sum)
    test_cases = [
        # (A, B, Cin, Expected_Cout, Expected_Sum)
        (0, 0, 0, 0, 0),
        (0, 0, 1, 0, 1),
        (0, 1, 0, 0, 1),
        (0, 1, 1, 1, 0),
        (1, 0, 0, 0, 1),
        (1, 0, 1, 1, 0),
        (1, 1, 0, 1, 0),
        (1, 1, 1, 1, 1),
    ]

    for a, b, cin, exp_cout, exp_sum in test_cases:
        # Construct ui_in value: bit0 = A, bit1 = B, bit2 = Cin
        input_val = a | (b << 1) | (cin << 2)
        dut.ui_in.value = input_val

        await ClockCycles(dut.clk, 1)

        # Extract output bits: bit0 = Sum, bit1 = Cout
        output_val = dut.uo_out.value.integer
        actual_sum = output_val & 1
        actual_cout = (output_val >> 1) & 1

        dut._log.info(f"Input A={a} B={b} Cin={cin} -> Sum={actual_sum} Cout={actual_cout}")

        assert actual_sum == exp_sum, f"Failed Sum: A={a} B={b} Cin={cin}"
        assert actual_cout == exp_cout, f"Failed Cout: A={a} B={b} Cin={cin}"
