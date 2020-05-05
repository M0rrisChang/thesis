# ---------------------------------------------US---------------------------------------------
# 20243 news read
# 3071 news got kicked out
# 4729 news are related to coronavirus
# 1347 news may lead to outrage
# starts from 1/6
News <- c(2, 2, 4, 1, 1, 1, 1, 1, 4, 7, 7, 9, 8, 1, 7, 12, 9, 14, 13, 14, 7, 11, 8, 9, 9, 19, 13, 9, 6, 7, 11, 5, 9, 5, 3, 3, 5, 2, 4, 5, 6, 4, 1, 11, 14, 13, 17, 18, 16, 10, 22, 20, 22, 15, 29, 16, 13, 29, 28, 28, 38, 31, 19, 22, 43, 45, 38, 39, 38, 13, 17, 30, 47, 28, 37, 36, 17, 26, 38, 55, 33, 32, 21, 2, 1, 1)

# 3/12 ~ 4/3
News <- c(38, 31, 19, 22, 43, 45, 38, 39, 38, 13, 17, 30, 47, 28, 37, 36, 17, 26, 38, 55, 33, 32, 21)
N = length(News)
T_day <- 1:N
plot(News ~ T_day)
Bass.nls <- nls(
  News ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
  start=list(M=500, P=0.003, Q=0.38)
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
subtitle = paste(p, q, sep = ", ")
plot(Tdelt, Bpdf, xlab = "Day from 3/11", ylab = "News per day", type = "l", main = "Outrage components in US", sub = subtitle)
points(T_day, News)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 3/11", ylab = "Cumulative news", type = "l", main = "Outrage components in US", sub = subtitle)
points(T_day, cumsum(News))
# ---------------------------------------------US---------------------------------------------


# ---------------------------------------------UK---------------------------------------------
# 25465 news read
# 5964 news got kicked out
# 9268 news are related to coronavirus
# 2619 news may lead to outrage
# starts from 1/3
News <- c(2, 2, 2, 1, 1, 2, 5, 4, 16, 15, 8, 13, 8, 21, 18, 16, 19, 10, 7, 12, 14, 9, 8, 16, 9, 5, 12, 17, 14, 19, 18, 6, 2, 5, 5, 8, 5, 11, 5, 8, 35, 28, 36, 29, 41, 35, 27, 54, 54, 62, 47, 63, 29, 35, 79, 63, 62, 68, 63, 58, 40, 77, 63, 64, 59, 48, 42, 48, 61, 75, 77, 84, 88, 55, 59, 66, 86, 79, 92, 10)

# 3/11 ~ 4/3
#News <- c(62, 68, 63, 58, 40, 77, 63, 64, 59, 48, 42, 48, 61, 75, 77, 84, 88, 55, 59, 66, 86, 79, 92, 10)
N = length(News)
T_day <- 1:N
Bass.nls <- nls(
  News ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
  start=list(M=6300, P=0.004, Q=0.08)
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
subtitle = paste(p, q, sep = ", ")
plot(Tdelt, Bpdf, xlab = "Day from 3/10", ylab = "News per day", type = "l", main = "Outrage components in UK", sub = subtitle)
points(T_day, News)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 3/10", ylab = "Cumulative news", type = "l", main = "Outrage components in UK", sub = subtitle)
points(T_day, cumsum(News))
# ---------------------------------------------UK---------------------------------------------

# ---------------------------------------------CA---------------------------------------------
# 19619 news read
# 2633 news got kicked out
# 7229 news are related to coronavirus
# 1965 news may lead to outrage
# starts from 1/9
News <- c(1, 1, 2, 28, 24, 30, 28, 37, 18, 18, 29, 21, 25, 26, 21, 18, 16, 7, 34, 11, 26, 15, 10, 10, 19, 17, 12, 22, 13, 9, 12, 10, 15, 9, 3, 8, 7, 27, 24, 17, 18, 37, 14, 21, 25, 33, 26, 50, 28, 30, 14, 29, 25, 30, 30, 26, 20, 21, 49, 33, 38, 56, 47, 15, 24, 49, 49, 43, 30, 34, 18, 22, 51, 40, 30, 36, 24, 12, 15, 18, 21, 27, 3, 15, 9)

#
News <- c(49, 33, 38, 56, 47, 15, 24, 49, 49, 43, 30, 34, 18, 22, 51, 40, 30, 36, 24, 12, 15, 18, 21, 27, 3, 15, 9)
N = length(News)
T_day <- 1:N
plot(News ~ T_day)
Bass.nls <- nls(
  News ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
  start=list(M=100, P=0.003, Q=-0.0038)
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
subtitle = paste(p, q, sep = ", ")
plot(Tdelt, Bpdf, xlab = "Day from 3/15", ylab = "News per day", type = "l", main = "Outrage components in CA", sub = subtitle)
points(T_day, News)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 3/15", ylab = "Cumulative news", type = "l", main = "Outrage components in CA", sub = subtitle)
points(T_day, cumsum(News))
# ---------------------------------------------CA---------------------------------------------


# ---------------------------------------------AU---------------------------------------------
# 29790 news read
# 494 news got kicked out
# 7654 news are related to coronavirus
# 1892 news may lead to outrage
# starts from 1/20
News <- c(1, 5, 3, 5, 5, 4, 8, 10, 11, 6, 13, 13, 12, 7, 13, 14, 16, 13, 12, 4, 5, 10, 21, 17, 16, 8, 8, 7, 7, 5, 8, 9, 3, 6, 11, 15, 17, 34, 23, 16, 12, 19, 39, 39, 37, 42, 39, 15, 23, 36, 46, 46, 39, 51, 24, 33, 45, 65, 62, 55, 44, 29, 24, 60, 65, 61, 64, 42, 40, 32, 42, 33, 40, 30, 31, 19, 3, 15, 11, 9, 5, 5)

# 3/16 ~ 4/10
News <- c(45, 65, 62, 55, 44, 29, 24, 60, 65, 61, 64, 42, 40, 32, 42, 33, 40, 30, 31, 19, 3, 15, 11, 9, 5, 5)
N = length(News)
T_day <- 1:N
Bass.nls <- nls(
  News ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
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
subtitle = paste(p, q, sep = ", ")
plot(Tdelt, Bpdf, xlab = "Day from 3/15", ylab = "News per day", type = "l", main = "Outrage components in AU", sub = subtitle)
points(T_day, News)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 3/15", ylab = "Cumulative news", type = "l", main = "Outrage components in AU", sub = subtitle)
points(T_day, cumsum(News))
# ---------------------------------------------AU---------------------------------------------


# ---------------------------------------------TW---------------------------------------------
# 41841 news read
# 281 news got kicked out
# 26143 news are related to coronavirus
# 7541 news may lead to outrage
# starts from 1/1
News <- c(5, 5, 1, 6, 6, 17, 41, 19, 36, 16, 10, 6, 1, 26, 23, 55, 51, 109, 192, 281, 138, 107, 135, 169, 130, 64, 112, 186, 151, 61, 45, 31, 61, 49, 49, 36, 43, 30, 53, 51, 30, 135, 159, 151, 98, 159, 139, 103, 101, 114, 99, 94, 94, 96, 97, 95, 105, 96, 129, 103, 110, 155, 207, 130, 93, 34, 58, 84, 108, 109, 62, 76, 68, 84, 95, 75, 87, 88, 78, 82, 82, 61, 91, 117, 63, 69, 63, 129, 107, 20, 15, 8, 10, 2, 6, 7, 3, 1)

# 3/15 ~ 4/10
News <- c(84, 95, 75, 87, 88, 78, 82, 82, 61, 91, 117, 63, 69, 63, 129, 107, 20, 15, 8, 10, 2, 6, 7, 3, 1)
N = length(News)
T_day <- 1:N
Bass.nls <- nls(
  News ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
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
subtitle = paste(p, q, sep = ", ")
plot(Tdelt, Bpdf, xlab = "Day from 3/15", ylab = "News per day", type = "l", main = "Outrage components in TW", sub = subtitle)
points(T_day, News)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 3/15", ylab = "Cumulative news", type = "l", main = "Outrage components in TW", sub = subtitle)
points(T_day, cumsum(News))
# ---------------------------------------------TW---------------------------------------------


# ---------------------------------------------CN---------------------------------------------
# row_count 48437
# 21079 news are related to coronavirus
# 6166 news may lead to outrage
# starts from 1/5
News <- c(4, 6, 1, 1, 15, 1, 19, 2, 4, 2, 4, 3, 10, 8, 16, 62, 74, 103, 108, 80, 94, 107, 94, 149, 134, 132, 131, 114, 140, 162, 155, 155, 152, 125, 147, 148, 148, 143, 128, 163, 146, 121, 118, 132, 115, 112, 123, 180, 119, 104, 86, 134, 124, 125, 119, 93, 146, 116, 101, 115, 132, 117, 80, 84, 80)
News <- c(103, 108, 80, 94, 107, 94, 149, 134, 132, 131, 114, 140, 162, 155, 155, 152, 125, 147, 148, 148, 143, 128, 163, 146, 121, 118, 132, 115, 112, 123, 180, 119, 104, 86, 134, 124, 125, 119, 93, 146, 116, 101, 115, 132, 117, 80, 84, 80)
N = length(News)
T_day <- 1:N
Bass.nls <- nls(
  News ~ M * (((P + Q) ^ 2 / P) * exp(-(P + Q) * T_day)) / (1 + (Q / P) * exp(-(P + Q) * T_day)) ^ 2,
  start=list(M=6300, P=0.003, Q=0.38)
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
subtitle = paste(p, q, sep = ", ")
plot(Tdelt, Bpdf, xlab = "Day from 1/22", ylab = "News per day", type = "l", main = "Outrage components in CN", sub = subtitle)
points(T_day, News)


# simulation
Bcdf <- m * (1 - ngete)/(1 + (q / p) * ngete)
# plot cdf
plot(Tdelt, Bcdf, xlab = "Day from 1/22", ylab = "Cumulative news", type = "l", main = "Outrage components in CN", sub = subtitle)
points(T_day, cumsum(News))
# ---------------------------------------------CN---------------------------------------------

