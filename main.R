options(warn = -1)
library(audio)
library(tuneR, warn.conflicts = FALSE)
library(fftw)
library(seewave)
sample_rate <- 44100
record_length <- 0.5

x <- rep(NA_real_, sample_rate * record_length)
# start recording into x

out <- record(x, sample_rate, 1)
# monitor the recording progress
wait(record_length)
#while (is.null(x[0]) | is.na(x[0]) | is.nan(x[0]))
#{
#
#}
y <- as.vector(x)

wave <- Wave(left = y, samp.rate = sample_rate)


#turn off warnings
options(warn = -1)

bandpass_range_basic <- c(0, 44000)
window_length <- 2048
threshold <- 5

bandpass_range <- bandpass_range_basic #in case bp its higher than can be due to sampling rate
if (bandpass_range[2] > ceiling(wave@samp.rate / 2) - 1) bandpass_range[2] <- ceiling(wave@samp.rate / 2) - 1

songspec <- seewave::spec(wave, f = wave@samp.rate, plot = FALSE)

spectral_analysis <- seewave::specprop(songspec, f = wave@samp.rate, plot = FALSE)

#save parameters
meanfreq <- spectral_analysis$mean / 1000
sd <- spectral_analysis$sd / 1000
median <- spectral_analysis$median / 1000
Q25 <- spectral_analysis$Q25 / 1000
Q75 <- spectral_analysis$Q75 / 1000
IQR <- spectral_analysis$IQR / 1000
skew <- spectral_analysis$skewness
kurt <- spectral_analysis$kurtosis
sp.ent <- spectral_analysis$sh
sfm <- spectral_analysis$sfm
mode <- spectral_analysis$mode / 1000
centroid <- spectral_analysis$cent / 1000

# Fundamental frequency parameters
ff <- seewave::fund(wave, f = wave@samp.rate, ovlp = 50, threshold = threshold,
                    plot = FALSE, wl = window_length)[, 2]

meanfun <- mean(ff, na.rm = TRUE)
minfun <- min(ff, na.rm = TRUE)
maxfun <- max(ff, na.rm = TRUE)

#Dominant frecuency parameters (Highest amplitude)
dominant_frequencies <- seewave::dfreq(wave, f = wave@samp.rate, wl = window_length, ovlp = 0, threshold = threshold, bandpass = bandpass_range, fftw = TRUE, plot = FALSE)[, 2]
meandom <- mean(dominant_frequencies, na.rm = TRUE)
mindom <- min(dominant_frequencies, na.rm = TRUE)
maxdom <- max(dominant_frequencies, na.rm = TRUE)
dfrange <- (maxdom - mindom)
duration <- length(wave@left) / wave@samp.rate

#modulation index calculation
changes <- vector()
for (j in which(!is.na(dominant_frequencies))) {
  change <- abs(dominant_frequencies[j] - dominant_frequencies[j + 1])
  changes <- append(changes, change)
}

if (mindom == maxdom) modindx <- 0 else modindx <- mean(changes, na.rm = T) / dfrange

paste(c(duration, meanfreq, sd, median, Q25, Q75, IQR, skew, kurt, sp.ent, sfm, mode,
            centroid, meanfun, minfun, maxfun, meandom, mindom, maxdom, dfrange, modindx), collapse = " ")
#row_names <- c("duration", "meanfreq", "sd", "median", "Q25", "Q75", "IQR", "skew", "kurt", "sp.ent",
#               "sfm", "mode", "centroid", "meanfun", "minfun", "maxfun", "meandom", "mindom", "maxdom", "dfrange", "modindx")
#paste(c("duration", duration, ", meanfreq", meanfreq, ", sd", sd, " ,median", median, ", Q25", Q25, ", Q75", Q75, ", IQR", IQR, ", skew", skew, ", kurt", kurt, ", sp.ent", sp.ent,
#        ", sfm", sfm, ", mode", mode, ", centroid", centroid, ", meanfun", meanfun, ", minfun", minfun, ", maxfun", maxfun, ", meandom", meandom, ", mindom", mindom, ", maxdom", maxdom, ", dfrange", dfrange, ", modindx", modindx), collapse = " ")
#"oko, nos, witam"
#values
#print(duration, meanfreq, sd, median, Q25, Q75, IQR, skew, kurt, sp.ent, sfm, mode,
#            centroid, meanfun, minfun, maxfun, meandom, mindom, maxdom, dfrange, modindx)