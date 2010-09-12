cat("hello world :-)\n")


# Let's graph the waveform of the mp3 we made earlier...
require(tuneR, quiet=TRUE)
require(seewave, quiet=TRUE)
w <- readMP3("artifacts/{{ d['filename']['hello.txt|jinja|voice']  }}")
png(file="{{ a.create_input_file('waveform', 'png') }}", width=550, height=550)
spectro(w, osc=TRUE)
dev.off()

