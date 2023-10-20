from spectrums import Spectrum, show_spectra

if __name__ == "__main__":
    s1 = Spectrum(path="data/Serum_Turtle_1_1.0")
    s2 = Spectrum(path="data/Serum_Turtle_1_1.2")
    s1.clss = "first"
    s2.clss = "second"
    show_spectra([s1, s2])
