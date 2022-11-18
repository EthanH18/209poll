#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## 209poll
## File description:
## calc_209
##

import math

def calc_209(psize, ssize, p):
    percent_p = p / 100
    variance = (percent_p * (1 - percent_p) / ssize) * ((psize - ssize) / (psize - 1))
    confidence95 = 196 * math.sqrt(variance)
    confidence99 = 258 * math.sqrt(variance)
    confid_inter95 = [max(p - confidence95, 0), min(p + confidence95, 100)]
    confid_inter99 = [max(p - confidence99, 0), min(p + confidence99, 100)]
    print(f"Population size:\t{psize:d}")
    print(f"Sample size:\t\t{ssize:d}")
    display_result209(p, variance, confid_inter95, confid_inter99)

def display_result209(p, variance, confid_inter95, confid_inter99):
    print(f"Voting intentions:\t{p:.2f}%")
    print(f"Variance:\t\t{variance:.6f}")
    print("95%% confidence interval:\t[%s]" % "; ".join(map(lambda x: "%.2f%%" % x, confid_inter95)))
    print("99%% confidence interval:\t[%s]" % "; ".join(map(lambda x: "%.2f%%" % x, confid_inter99)))