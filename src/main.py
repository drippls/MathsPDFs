#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from fpdf import FPDF
from PIL import Image


def makePdf(pdfFileName, imagelist): 
    dir = "../imgs/"
    cover = Image.open(dir + str(imagelist[0]))
    width, height = cover.size
    pdf = FPDF(unit = "pt", format = [width, height])

    for page in imagelist:
        pdf.add_page()
        pdf.image(dir + str(page), 0, 0)

    pdf.output("../../"+ pdfFileName + ".pdf", "F")

imagelist = sorted([file for file in os.listdir("../imgs") if file.endswith(".jpg")])
makePdf(sys.argv[1], imagelist)

