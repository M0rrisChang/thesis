# ---------------------------------------------US---------------------------------------------
Cases <- c(382, 516, 547, 773, 1133, 1789, 1365, 5894, 5421, 6413, 8334, 9819,
           10073, 12038, 18058, 17821, 19808, 19444, 20922, 26341, 25200, 30227,
           31987, 33267, 28219, 29595, 29556, 32829, 32385, 35098)
N = length(Cases)
T_day <- 1:N
Bass.nls <- nls(
  Cases ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
  start=list(M=806300, P=0.003, Q=0.38)
)
summary(Bass.nls)

Bcoef <- coef(Bass.nls)
m <- Bcoef[1]
p <- Bcoef[2]
q <- Bcoef[3]
# setting the starting value for M to the recorded total sales.

# simulation
Tdelt <- (1:(N * 10)) / 10
ngete <- exp(-(p + q) * Tdelt)
Bpdf <- m * ((p + q) ^ 2 / p) * ngete / (1 + (q / p) * ngete) ^ 2
# plot pdf
plot(Tdelt, Bpdf, xlab = "Day from 3/11", ylab = "Cases per day", type = "l", main = "Coronavirus in US")
points(T_day, Cases)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 3/11", ylab = "Cumulative cases", type = "l", main = "Coronavirus in US")
points(T_day, cumsum(Cases))
# ---------------------------------------------US---------------------------------------------


# ---------------------------------------------UK---------------------------------------------
Cases <- c(459, 590, 342, 342, 1, 407, 409, 682, 74, 1298, 1053, 674,
           985, 1438, 1476, 2172, 2933, 2567, 2468, 2673, 3028, 4384,
           4308, 4516, 3788, 5959, 3843, 3670, 5525, 4398, 8733)
N = length(Cases)
T_day <- 1:N
Bass.nls <- nls(
  Cases ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
  start=list(M=86300, P=0.003, Q=0.38)
)
summary(Bass.nls)

Bcoef <- coef(Bass.nls)
m <- Bcoef[1]
p <- Bcoef[2]
q <- Bcoef[3]
# setting the starting value for M to the recorded total sales.

# simulation
Tdelt <- (1:(N * 10)) / 10
ngete <- exp(-(p + q) * Tdelt)
Bpdf <- m * ((p + q) ^ 2 / p) * ngete / (1 + (q / p) * ngete) ^ 2
# plot pdf
plot(Tdelt, Bpdf, xlab = "Day from 3/10", ylab = "Cases per day", type = "l", main = "Coronavirus in UK")
points(T_day, Cases)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 3/10", ylab = "Cumulative cases", type = "l", main = "Coronavirus in UK")
points(T_day, cumsum(Cases))
# ---------------------------------------------UK---------------------------------------------

# ---------------------------------------------CA---------------------------------------------
Cases <- c(165, 63, 179, 143, 143, 335, 192, 618, 702, 461, 791, 640,
           894, 704, 1118, 1129, 1033, 1724, 1153, 541, 2778, 807,
           1309, 1269, 1513, 1405)
N = length(Cases)
T_day <- 1:N
Bass.nls <- nls(
  Cases ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
  start=list(M=86300, P=0.003, Q=0.38)
)
summary(Bass.nls)

Bcoef <- coef(Bass.nls)
m <- Bcoef[1]
p <- Bcoef[2]
q <- Bcoef[3]
# setting the starting value for M to the recorded total sales.

# simulation
Tdelt <- (1:(N * 10)) / 10
ngete <- exp(-(p + q) * Tdelt)
Bpdf <- m * ((p + q) ^ 2 / p) * ngete / (1 + (q / p) * ngete) ^ 2
# plot pdf
plot(Tdelt, Bpdf, xlab = "Day from 3/15", ylab = "Cases per day", type = "l", main = "Coronavirus in CA")
points(T_day, Cases)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 3/15", ylab = "Cumulative cases", type = "l", main = "Coronavirus in CA")
points(T_day, cumsum(Cases))
# ---------------------------------------------CA---------------------------------------------


# ---------------------------------------------AU---------------------------------------------
Cases <- c(80, 75, 116, 113, 110, 280, 419, 192, 362, 320, 446, 333, 497,
           344, 377, 198, 303, 254, 214, 220, 137, 110, 98, 115, 98, 107)
N = length(Cases)
T_day <- 1:N
Bass.nls <- nls(
  Cases ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
  start=list(M=10300, P=0.003, Q=0.38)
)
summary(Bass.nls)

Bcoef <- coef(Bass.nls)
m <- Bcoef[1]
p <- Bcoef[2]
q <- Bcoef[3]
# setting the starting value for M to the recorded total sales.

# simulation
Tdelt <- (1:(N * 10)) / 10
ngete <- exp(-(p + q) * Tdelt)
Bpdf <- m * ((p + q) ^ 2 / p) * ngete / (1 + (q / p) * ngete) ^ 2
# plot pdf
plot(Tdelt, Bpdf, xlab = "Day from 3/15", ylab = "Cases per day", type = "l", main = "Coronavirus in AU")
points(T_day, Cases)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 3/15", ylab = "Cumulative cases", type = "l", main = "Coronavirus in AU")
points(T_day, cumsum(Cases))
# ---------------------------------------------AU---------------------------------------------


# ---------------------------------------------TW---------------------------------------------
Cases <- c(2, 1, 1, 1, 3, 6, 8, 10, 23, 8, 27, 18, 16, 26,
           20, 20, 17, 15, 16, 15, 8, 16, 7, 10, 9, 7, 8, 10, 3, 3, 1, 2)
N = length(Cases)
T_day <- 1:N
Bass.nls <- nls(
  Cases ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
  start=list(M=1000, P=0.003, Q=0.38)
)
summary(Bass.nls)

Bcoef <- coef(Bass.nls)
m <- Bcoef[1]
p <- Bcoef[2]
q <- Bcoef[3]
# setting the starting value for M to the recorded total sales.

# simulation
Tdelt <- (1:(N * 10)) / 10
ngete <- exp(-(p + q) * Tdelt)
Bpdf <- m * ((p + q) ^ 2 / p) * ngete / (1 + (q / p) * ngete) ^ 2
# plot pdf
plot(Tdelt, Bpdf, xlab = "Day from 3/09", ylab = "Cases per day", type = "l", main = "Coronavirus in TW")
points(T_day, Cases)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 3/09", ylab = "Cumulative cases", type = "l", main = "Coronavirus in TW")
points(T_day, cumsum(Cases))
# ---------------------------------------------TW---------------------------------------------


# ---------------------------------------------CN---------------------------------------------
Cases <- c(95, 277, 486, 669, 802, 2632, 578, 2054, 1661, 2089, 4739, 3086,
           3991, 3733, 3147, 3523, 2704, 3015, 2525, 2032, 373, 15136, 6463,
           2055, 2100, 1921, 1777, 408, 458, 473, 1451, 21, 219, 513, 412, 434,
           328, 428, 576, 204, 125, 125, 151, 153, 80, 53, 37, 103, 164, 11,
           13, 32, 26, 30, 25, 44, 54, 94, 55, 92, 99, 95, 70, 121, 115, 102,
           123, 76, 81, 82, 71, 79, 32, 59, 63, 53, 91, 74, 58)
N = length(Cases)
T_day <- 1:N
Bass.nls <- nls(
  Cases ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
  start=list(M=86300, P=0.003, Q=0.38)
)
summary(Bass.nls)

Bcoef <- coef(Bass.nls)
m <- Bcoef[1]
p <- Bcoef[2]
q <- Bcoef[3]
# setting the starting value for M to the recorded total sales.

# simulation
Tdelt <- (1:(N * 10)) / 10
ngete <- exp(-(p + q) * Tdelt)
Bpdf <- m * ((p + q) ^ 2 / p) * ngete / (1 + (q / p) * ngete) ^ 2
# plot pdf
plot(Tdelt, Bpdf, xlab = "Day from 1/22", ylab = "Cases per day", type = "l", main = "Coronavirus in CN")
points(T_day, Cases)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 1/22", ylab = "Cumulative cases", type = "l", main = "Coronavirus in CN")
points(T_day, cumsum(Cases))
# ---------------------------------------------CN---------------------------------------------






