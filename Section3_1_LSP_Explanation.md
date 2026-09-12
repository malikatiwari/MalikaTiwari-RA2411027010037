# Section 3.1 — LSP Warm-up Explanation

The Square/Rectangle example breaks LSP because code using a Rectangle assumes that width and height can be changed independently. A Square violates that assumption because changing one side must also change the other side. Therefore, a Square cannot safely substitute for a Rectangle when the caller relies on independent width and height behavior.
