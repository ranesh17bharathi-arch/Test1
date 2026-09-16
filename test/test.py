import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_full_adder(dut):
    dut._log.info("Starting Full Adder Test")

    # Start clock (100 KHz)
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

        # Wait one clock cycle for the output to settle
        await ClockCycles(dut.clk, 1)

        # Extract output bits from uo_out
        output_val = dut.uo_out.value.integer
        actual_sum = output_val & 1           # bit 0
        actual_cout = (output_val >> 1) & 1   # bit 1

        # Log the current test state
        dut._log.info(f"Input A={a} B={b} Cin={cin} -> Expected: Sum={exp_sum} Cout={exp_cout} | Actual: Sum={actual_sum} Cout={actual_cout}")

        # Assertions
        assert actual_sum == exp_sum, f"Failed Sum for A={a}, B={b}, Cin={cin}. Expected {exp_sum}, got {actual_sum}."
        assert actual_cout == exp_cout, f"Failed Cout for A={a}, B={b}, Cin={cin}. Expected {exp_cout}, got {actual_cout}."
